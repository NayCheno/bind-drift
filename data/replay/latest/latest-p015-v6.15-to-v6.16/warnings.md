# BindDrift Ranked Warnings

## W-000319 SignatureDrift

- Risk: High
- Score: 14.0
- Symbol: drm_ioctl
- Explanation: drm_ioctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `17`

## W-000059 SignatureDrift

- Risk: High
- Score: 13.8
- Symbol: clk_get
- Explanation: clk_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `16`

## W-001093 AllocationFreePairingDrift

- Risk: High
- Score: 13.7
- Symbol: auxiliary_device_uninit
- Explanation: auxiliary_device_uninit has FREE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['FREE', 'REFCOUNT_PUT']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/auxiliary_bus.h:241 `mutex_destroy(&auxdev->sysfs.lock);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:331 `Registration::new` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:354 `drop` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:329 `// SAFETY: `adev` is guaranteed to be a valid pointer to a `struct auxiliary_device`,`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:336 `// SAFETY: `adev` is guaranteed to be non-null, since the `KBox` was allocated successfully.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:352 `// SAFETY: By the type invariant of `Self`, `self.0.as_ptr()` is a valid registered`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:352 `AS_PTR`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:354 `AS_PTR`

## W-001094 OwnershipRefcountDrift

- Risk: High
- Score: 13.7
- Symbol: auxiliary_device_uninit
- Explanation: auxiliary_device_uninit has REFCOUNT_PUT C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['FREE', 'REFCOUNT_PUT']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/auxiliary_bus.h:242 `put_device(&auxdev->dev);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:331 `Registration::new` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:354 `drop` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:329 `// SAFETY: `adev` is guaranteed to be a valid pointer to a `struct auxiliary_device`,`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:336 `// SAFETY: `adev` is guaranteed to be non-null, since the `KBox` was allocated successfully.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:352 `// SAFETY: By the type invariant of `Self`, `self.0.as_ptr()` is a valid registered`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:352 `AS_PTR`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/auxiliary.rs:354 `AS_PTR`

## W-000433 SignatureDrift

- Risk: High
- Score: 13.4
- Symbol: mmget
- Explanation: mmget changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `14`

## W-000043 SignatureDrift

- Risk: High
- Score: 13.2
- Symbol: auxiliary_device_uninit
- Explanation: auxiliary_device_uninit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `13`

## W-001101 OwnershipRefcountDrift

- Risk: High
- Score: 13.2
- Symbol: clk_put
- Explanation: clk_put has REFCOUNT_PUT C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['REFCOUNT_PUT']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/clk.h:1051 `static inline void clk_put(struct clk *clk) {}`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:251 `drop` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:250 `// SAFETY: By the type invariants, self.as_raw() is a valid argument for [`clk_put`].`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:255 `/// A reference-counted optional clock.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:256 `///`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:248 `IMPL_DROP`

## W-001103 NullabilityDrift

- Risk: High
- Score: 13.2
- Symbol: cpufreq_cpu_get
- Explanation: cpufreq_cpu_get has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/cpufreq.h:217 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/cpufreq.rs:685 `from_cpu` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/cpufreq.rs:684 `// SAFETY: It is safe to call `cpufreq_cpu_get` for any valid CPU.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/cpufreq.rs:688 `// SAFETY: The `ptr` is guaranteed to be valid and remains valid for the lifetime of`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/cpufreq.rs:683 `RESULT_RETURN`

## W-001104 OwnershipRefcountDrift

- Risk: High
- Score: 13.2
- Symbol: cpufreq_cpu_put
- Explanation: cpufreq_cpu_put has REFCOUNT_PUT C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['REFCOUNT_PUT']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/cpufreq.h:219 `static inline void cpufreq_cpu_put(struct cpufreq_policy *policy) { }`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/cpufreq.rs:712 `drop` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/cpufreq.rs:711 `// SAFETY: The underlying pointer is guaranteed to be valid for the lifetime of `self`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/cpufreq.rs:716 `/// CPU frequency driver.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/cpufreq.rs:717 `///`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/cpufreq.rs:709 `IMPL_DROP`

## W-000062 SignatureDrift

- Risk: High
- Score: 13.0
- Symbol: clk_prepare
- Explanation: clk_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `12`

## W-001095 NullabilityDrift

- Risk: High
- Score: 13.0
- Symbol: clk_get
- Explanation: clk_get has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/clk.h:957 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:145 `Clk::get` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:141 `// SAFETY: It is safe to call [`clk_get`] for a valid device pointer.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:144 `ERR_PTR_MAPPING`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:145 `LIFETIME_NAMING_PATTERN`

## W-001097 NullabilityDrift

- Risk: High
- Score: 13.0
- Symbol: clk_get_optional
- Explanation: clk_get_optional has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN', 'NULL_RETURN', 'REFCOUNT_GET']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/clk.h:1209 `if (clk == ERR_PTR(-ENOENT))`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:318 `OptionalClk::get` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:313 `// SAFETY: It is safe to call [`clk_get_optional`] for a valid device pointer.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:317 `ERR_PTR_MAPPING`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:318 `LIFETIME_NAMING_PATTERN`

## W-001098 NullabilityDrift

- Risk: High
- Score: 13.0
- Symbol: clk_get_optional
- Explanation: clk_get_optional has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN', 'NULL_RETURN', 'REFCOUNT_GET']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/clk.h:1210 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:318 `OptionalClk::get` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:313 `// SAFETY: It is safe to call [`clk_get_optional`] for a valid device pointer.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:317 `ERR_PTR_MAPPING`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:318 `LIFETIME_NAMING_PATTERN`

## W-001099 OwnershipRefcountDrift

- Risk: High
- Score: 13.0
- Symbol: clk_get_optional
- Explanation: clk_get_optional has REFCOUNT_GET C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN', 'NULL_RETURN', 'REFCOUNT_GET']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/clk.h:1207 `struct clk *clk = clk_get(dev, id);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:318 `OptionalClk::get` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:313 `// SAFETY: It is safe to call [`clk_get_optional`] for a valid device pointer.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:317 `ERR_PTR_MAPPING`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:318 `LIFETIME_NAMING_PATTERN`

## W-001116 OwnershipRefcountDrift

- Risk: High
- Score: 13.0
- Symbol: dev_pm_opp_put
- Explanation: dev_pm_opp_put has REFCOUNT_PUT C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['REFCOUNT_PUT']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/pm_opp.h:358 `static inline void dev_pm_opp_put(struct dev_pm_opp *opp) {}`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:1053 `dec_ref` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:1052 `// SAFETY: The safety requirements guarantee that the refcount is nonzero.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:1058 `/// Creates an owned reference to a [`OPP`] from a valid pointer.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:1053 `AS_PTR`

## W-000434 SignatureDrift

- Risk: High
- Score: 12.8
- Symbol: mmget_not_zero
- Explanation: mmget_not_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `11`

## W-001106 NullabilityDrift

- Risk: High
- Score: 12.8
- Symbol: dev_pm_opp_find_bw_floor
- Explanation: dev_pm_opp_find_bw_floor has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/pm_opp.h:350 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:931 `Table::opp_from_bw` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:928 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:935 `// SAFETY: The `ptr` is guaranteed by the C code to be valid.`

## W-001109 NullabilityDrift

- Risk: High
- Score: 12.8
- Symbol: dev_pm_opp_find_freq_floor_indexed
- Explanation: dev_pm_opp_find_freq_floor_indexed has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/pm_opp.h:308 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:880 `Table::set_opp` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:877 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:884 `// SAFETY: The `ptr` is guaranteed by the C code to be valid.`

## W-001111 NullabilityDrift

- Risk: High
- Score: 12.8
- Symbol: dev_pm_opp_find_level_exact
- Explanation: dev_pm_opp_find_level_exact has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/pm_opp.h:326 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:895 `Table::opp_from_level` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:893 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:892 `ERR_PTR_MAPPING`

## W-001112 NullabilityDrift

- Risk: High
- Score: 12.8
- Symbol: dev_pm_opp_find_level_floor
- Explanation: dev_pm_opp_find_level_floor has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/pm_opp.h:338 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:906 `Table::opp_from_level` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:903 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:910 `// SAFETY: The `ptr` is guaranteed by the C code to be valid.`

## W-001113 NullabilityDrift

- Risk: High
- Score: 12.8
- Symbol: dev_pm_opp_get_opp_table
- Explanation: dev_pm_opp_get_opp_table has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/pm_opp.h:204 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:645 `Table::from_dev` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:640 `// SAFETY: The requirements are satisfied by the existence of the [`Device`] and its safety`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:645 `ERR_PTR_MAPPING`

## W-000056 SignatureDrift

- Risk: High
- Score: 12.6
- Symbol: clk_disable
- Explanation: clk_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `10`

## W-000072 SignatureDrift

- Risk: High
- Score: 12.6
- Symbol: config_group_init_type_name
- Explanation: config_group_init_type_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `10`

## W-000099 SignatureDrift

- Risk: High
- Score: 12.6
- Symbol: cpufreq_cpu_get
- Explanation: cpufreq_cpu_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `10`

## W-000295 SignatureDrift

- Risk: High
- Score: 12.6
- Symbol: drm_gem_object_init
- Explanation: drm_gem_object_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `10`

## W-000349 SignatureDrift

- Risk: High
- Score: 12.6
- Symbol: drm_open
- Explanation: drm_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000546 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: bio
- Explanation: bio changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bi_next', 'type': '*mut bio'}, {'name': 'bi_bdev', 'type': '*mut block_device'}, {'name': 'bi_opf', 'type': 'blk_opf_t'}, {'name': 'bi_flags', 'type': 'ffi::c_ushort'}, {'name': 'bi_ioprio', 'type': 'ffi::c_ushort'}, {'name': 'bi_write_hint', 'type': 'rw_hint'}, {'name': 'bi_status', 'type': 'blk_status_t'}, {'name': '__bi_remaining', 'type': 'atomic_t'}, {'name': 'bi_iter', 'type': 'bvec_iter'}, {'name': '__bindgen_anon_1', 'type': 'bio__bindgen_ty_1'}, {'name': 'bi_end_io', 'type': 'bio_end_io_t'}, {'name': 'bi_private', 'type': '*mut ffi::c_void'}, {'name': 'bi_blkg', 'type': '*mut blkcg_gq'}, {'name': 'bi_issue', 'type': 'bio_issue'}, {'name': 'bi_iocost_cost', 'type': 'u64_'}, {'name': 'bi_vcnt', 'type': 'ffi::c_ushort'}, {'name': 'bi_max_vecs', 'type': 'ffi::c_ushort'}, {'name': '__bi_cnt', 'type': 'atomic_t'}, {'name': 'bi_io_vec', 'type': '*mut bio_vec'}, {'name': 'bi_pool', 'type': '*mut bio_set'}, {'name': 'bi_inline_vecs', 'type': '__IncompleteArrayField<bio_vec>'}]`
- New: `[{'name': 'bi_next', 'type': '*mut bio'}, {'name': 'bi_bdev', 'type': '*mut block_device'}, {'name': 'bi_opf', 'type': 'blk_opf_t'}, {'name': 'bi_flags', 'type': 'ffi::c_ushort'}, {'name': 'bi_ioprio', 'type': 'ffi::c_ushort'}, {'name': 'bi_write_hint', 'type': 'rw_hint'}, {'name': 'bi_write_stream', 'type': 'u8_'}, {'name': 'bi_status', 'type': 'blk_status_t'}, {'name': '__bi_remaining', 'type': 'atomic_t'}, {'name': 'bi_iter', 'type': 'bvec_iter'}, {'name': '__bindgen_anon_1', 'type': 'bio__bindgen_ty_1'}, {'name': 'bi_end_io', 'type': 'bio_end_io_t'}, {'name': 'bi_private', 'type': '*mut ffi::c_void'}, {'name': 'bi_blkg', 'type': '*mut blkcg_gq'}, {'name': 'bi_issue', 'type': 'bio_issue'}, {'name': 'bi_iocost_cost', 'type': 'u64_'}, {'name': 'bi_vcnt', 'type': 'ffi::c_ushort'}, {'name': 'bi_max_vecs', 'type': 'ffi::c_ushort'}, {'name': '__bi_cnt', 'type': 'atomic_t'}, {'name': 'bi_io_vec', 'type': '*mut bio_vec'}, {'name': 'bi_pool', 'type': '*mut bio_set'}, {'name': 'bi_inline_vecs', 'type': '__IncompleteArrayField<bio_vec>'}]`

### Rust Evidence

- Graph edges: `50`

## W-000549 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: cgroup
- Explanation: cgroup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'self_', 'type': 'cgroup_subsys_state'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'max_depth', 'type': 'ffi::c_int'}, {'name': 'nr_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_dying_descendants', 'type': 'ffi::c_int'}, {'name': 'max_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_populated_csets', 'type': 'ffi::c_int'}, {'name': 'nr_populated_domain_children', 'type': 'ffi::c_int'}, {'name': 'nr_populated_threaded_children', 'type': 'ffi::c_int'}, {'name': 'nr_threaded_children', 'type': 'ffi::c_int'}, {'name': 'kill_seq', 'type': 'ffi::c_uint'}, {'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'procs_file', 'type': 'cgroup_file'}, {'name': 'events_file', 'type': 'cgroup_file'}, {'name': 'psi_files', 'type': '__IncompleteArrayField<cgroup_file>'}, {'name': 'subtree_control', 'type': 'u16_'}, {'name': 'subtree_ss_mask', 'type': 'u16_'}, {'name': 'old_subtree_control', 'type': 'u16_'}, {'name': 'old_subtree_ss_mask', 'type': 'u16_'}, {'name': 'subsys', 'type': '[*mut cgroup_subsys_state; 14usize]'}, {'name': 'nr_dying_subsys', 'type': '[ffi::c_int; 14usize]'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'cset_links', 'type': 'list_head'}, {'name': 'e_csets', 'type': '[list_head; 14usize]'}, {'name': 'dom_cgrp', 'type': '*mut cgroup'}, {'name': 'old_dom_cgrp', 'type': '*mut cgroup'}, {'name': 'rstat_cpu', 'type': '*mut cgroup_rstat_cpu'}, {'name': 'rstat_css_list', 'type': 'list_head'}, {'name': '__bindgen_padding_0', 'type': '[u64; 7usize]'}, {'name': '_pad_', 'type': 'cacheline_padding'}, {'name': 'rstat_flush_next', 'type': '*mut cgroup'}, {'name': 'last_bstat', 'type': 'cgroup_base_stat'}, {'name': 'bstat', 'type': 'cgroup_base_stat'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'pidlists', 'type': 'list_head'}, {'name': 'pidlist_mutex', 'type': 'mutex'}, {'name': 'offline_waitq', 'type': 'wait_queue_head_t'}, {'name': 'release_agent_work', 'type': 'work_struct'}, {'name': 'psi', 'type': '*mut psi_group'}, {'name': 'bpf', 'type': 'cgroup_bpf'}, {'name': 'freezer', 'type': 'cgroup_freezer_state'}, {'name': 'ancestors', 'type': '__IncompleteArrayField<*mut cgroup>'}]`
- New: `[{'name': 'self_', 'type': 'cgroup_subsys_state'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'level', 'type': 'ffi::c_int'}, {'name': 'max_depth', 'type': 'ffi::c_int'}, {'name': 'nr_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_dying_descendants', 'type': 'ffi::c_int'}, {'name': 'max_descendants', 'type': 'ffi::c_int'}, {'name': 'nr_populated_csets', 'type': 'ffi::c_int'}, {'name': 'nr_populated_domain_children', 'type': 'ffi::c_int'}, {'name': 'nr_populated_threaded_children', 'type': 'ffi::c_int'}, {'name': 'nr_threaded_children', 'type': 'ffi::c_int'}, {'name': 'kill_seq', 'type': 'ffi::c_uint'}, {'name': 'kn', 'type': '*mut kernfs_node'}, {'name': 'procs_file', 'type': 'cgroup_file'}, {'name': 'events_file', 'type': 'cgroup_file'}, {'name': 'psi_files', 'type': '__IncompleteArrayField<cgroup_file>'}, {'name': 'subtree_control', 'type': 'u16_'}, {'name': 'subtree_ss_mask', 'type': 'u16_'}, {'name': 'old_subtree_control', 'type': 'u16_'}, {'name': 'old_subtree_ss_mask', 'type': 'u16_'}, {'name': 'subsys', 'type': '[*mut cgroup_subsys_state; 14usize]'}, {'name': 'nr_dying_subsys', 'type': '[ffi::c_int; 14usize]'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'cset_links', 'type': 'list_head'}, {'name': 'e_csets', 'type': '[list_head; 14usize]'}, {'name': 'dom_cgrp', 'type': '*mut cgroup'}, {'name': 'old_dom_cgrp', 'type': '*mut cgroup'}, {'name': 'rstat_base_cpu', 'type': '*mut cgroup_rstat_base_cpu'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': '_pad_', 'type': 'cacheline_padding'}, {'name': 'last_bstat', 'type': 'cgroup_base_stat'}, {'name': 'bstat', 'type': 'cgroup_base_stat'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'pidlists', 'type': 'list_head'}, {'name': 'pidlist_mutex', 'type': 'mutex'}, {'name': 'offline_waitq', 'type': 'wait_queue_head_t'}, {'name': 'release_agent_work', 'type': 'work_struct'}, {'name': 'psi', 'type': '*mut psi_group'}, {'name': 'bpf', 'type': 'cgroup_bpf'}, {'name': 'freezer', 'type': 'cgroup_freezer_state'}, {'name': 'ancestors', 'type': '__IncompleteArrayField<*mut cgroup>'}]`

### Rust Evidence

- Graph edges: `50`

## W-000552 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: cpufreq_policy
- Explanation: cpufreq_policy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'cpus', 'type': 'cpumask_var_t'}, {'name': 'related_cpus', 'type': 'cpumask_var_t'}, {'name': 'real_cpus', 'type': 'cpumask_var_t'}, {'name': 'shared_type', 'type': 'ffi::c_uint'}, {'name': 'cpu', 'type': 'ffi::c_uint'}, {'name': 'clk', 'type': '*mut clk'}, {'name': 'cpuinfo', 'type': 'cpufreq_cpuinfo'}, {'name': 'min', 'type': 'ffi::c_uint'}, {'name': 'max', 'type': 'ffi::c_uint'}, {'name': 'cur', 'type': 'ffi::c_uint'}, {'name': 'suspend_freq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'last_policy', 'type': 'ffi::c_uint'}, {'name': 'governor', 'type': '*mut cpufreq_governor'}, {'name': 'governor_data', 'type': '*mut ffi::c_void'}, {'name': 'last_governor', 'type': '[ffi::c_char; 16usize]'}, {'name': 'update', 'type': 'work_struct'}, {'name': 'constraints', 'type': 'freq_constraints'}, {'name': 'min_freq_req', 'type': '*mut freq_qos_request'}, {'name': 'max_freq_req', 'type': '*mut freq_qos_request'}, {'name': 'freq_table', 'type': '*mut cpufreq_frequency_table'}, {'name': 'freq_table_sorted', 'type': 'cpufreq_table_sorting'}, {'name': 'policy_list', 'type': 'list_head'}, {'name': 'kobj', 'type': 'kobject'}, {'name': 'kobj_unregister', 'type': 'completion'}, {'name': 'rwsem', 'type': 'rw_semaphore'}, {'name': 'fast_switch_possible', 'type': 'bool_'}, {'name': 'fast_switch_enabled', 'type': 'bool_'}, {'name': 'strict_target', 'type': 'bool_'}, {'name': 'efficiencies_available', 'type': 'bool_'}, {'name': 'transition_delay_us', 'type': 'ffi::c_uint'}, {'name': 'dvfs_possible_from_any_cpu', 'type': 'bool_'}, {'name': 'boost_enabled', 'type': 'bool_'}, {'name': 'boost_supported', 'type': 'bool_'}, {'name': 'cached_target_freq', 'type': 'ffi::c_uint'}, {'name': 'cached_resolved_idx', 'type': 'ffi::c_uint'}, {'name': 'transition_ongoing', 'type': 'bool_'}, {'name': 'transition_lock', 'type': 'spinlock_t'}, {'name': 'transition_wait', 'type': 'wait_queue_head_t'}, {'name': 'transition_task', 'type': '*mut task_struct'}, {'name': 'stats', 'type': '*mut cpufreq_stats'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'cdev', 'type': '*mut thermal_cooling_device'}, {'name': 'nb_min', 'type': 'notifier_block'}, {'name': 'nb_max', 'type': 'notifier_block'}]`

### Rust Evidence

- Graph edges: `50`

## W-000553 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: dev_pm_qos
- Explanation: dev_pm_qos changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[{'name': 'resume_latency', 'type': 'pm_qos_constraints'}, {'name': 'latency_tolerance', 'type': 'pm_qos_constraints'}, {'name': 'freq', 'type': 'freq_constraints'}, {'name': 'flags', 'type': 'pm_qos_flags'}, {'name': 'resume_latency_req', 'type': '*mut dev_pm_qos_request'}, {'name': 'latency_tolerance_req', 'type': '*mut dev_pm_qos_request'}, {'name': 'flags_req', 'type': '*mut dev_pm_qos_request'}]`

### Rust Evidence

- Graph edges: `26`

## W-000563 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: module
- Explanation: module changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'state', 'type': 'module_state'}, {'name': 'list', 'type': 'list_head'}, {'name': 'name', 'type': '[ffi::c_char; 56usize]'}, {'name': 'mkobj', 'type': 'module_kobject'}, {'name': 'modinfo_attrs', 'type': '*mut module_attribute'}, {'name': 'version', 'type': '*const ffi::c_char'}, {'name': 'srcversion', 'type': '*const ffi::c_char'}, {'name': 'holders_dir', 'type': '*mut kobject'}, {'name': 'syms', 'type': '*mut kernel_symbol'}, {'name': 'crcs', 'type': '*const u32_'}, {'name': 'num_syms', 'type': 'ffi::c_uint'}, {'name': 'param_lock', 'type': 'mutex'}, {'name': 'kp', 'type': '*mut kernel_param'}, {'name': 'num_kp', 'type': 'ffi::c_uint'}, {'name': 'num_gpl_syms', 'type': 'ffi::c_uint'}, {'name': 'gpl_syms', 'type': '*const kernel_symbol'}, {'name': 'gpl_crcs', 'type': '*const u32_'}, {'name': 'using_gplonly_symbols', 'type': 'bool_'}, {'name': 'async_probe_requested', 'type': 'bool_'}, {'name': 'num_exentries', 'type': 'ffi::c_uint'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn() -> ffi::c_int>'}, {'name': 'mem', 'type': '[module_memory; 7usize]'}, {'name': 'arch', 'type': 'mod_arch_specific'}, {'name': 'taints', 'type': 'ffi::c_ulong'}, {'name': 'num_bugs', 'type': 'ffi::c_uint'}, {'name': 'bug_list', 'type': 'list_head'}, {'name': 'bug_table', 'type': '*mut bug_entry'}, {'name': 'kallsyms', 'type': '*mut mod_kallsyms'}, {'name': 'core_kallsyms', 'type': 'mod_kallsyms'}, {'name': 'sect_attrs', 'type': '*mut module_sect_attrs'}, {'name': 'notes_attrs', 'type': '*mut module_notes_attrs'}, {'name': 'args', 'type': '*mut ffi::c_char'}, {'name': 'percpu', 'type': '*mut ffi::c_void'}, {'name': 'percpu_size', 'type': 'ffi::c_uint'}, {'name': 'noinstr_text_start', 'type': '*mut ffi::c_void'}, {'name': 'noinstr_text_size', 'type': 'ffi::c_uint'}, {'name': 'num_tracepoints', 'type': 'ffi::c_uint'}, {'name': 'tracepoints_ptrs', 'type': '*const ffi::c_int'}, {'name': 'num_srcu_structs', 'type': 'ffi::c_uint'}, {'name': 'srcu_struct_ptrs', 'type': '*mut *mut srcu_struct'}, {'name': 'jump_entries', 'type': '*mut jump_entry'}, {'name': 'num_jump_entries', 'type': 'ffi::c_uint'}, {'name': 'num_trace_bprintk_fmt', 'type': 'ffi::c_uint'}, {'name': 'trace_bprintk_fmt_start', 'type': '*mut *const ffi::c_char'}, {'name': 'trace_events', 'type': '*mut *mut trace_event_call'}, {'name': 'num_trace_events', 'type': 'ffi::c_uint'}, {'name': 'trace_evals', 'type': '*mut *mut trace_eval_map'}, {'name': 'num_trace_evals', 'type': 'ffi::c_uint'}, {'name': 'kprobes_text_start', 'type': '*mut ffi::c_void'}, {'name': 'kprobes_text_size', 'type': 'ffi::c_uint'}, {'name': 'kprobe_blacklist', 'type': '*mut ffi::c_ulong'}, {'name': 'num_kprobe_blacklist', 'type': 'ffi::c_uint'}, {'name': 'num_static_call_sites', 'type': 'ffi::c_int'}, {'name': 'static_call_sites', 'type': '*mut static_call_site'}, {'name': 'source_list', 'type': 'list_head'}, {'name': 'target_list', 'type': 'list_head'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'refcnt', 'type': 'atomic_t'}, {'name': 'its_num_pages', 'type': 'ffi::c_int'}, {'name': 'its_page_array', 'type': '*mut *mut ffi::c_void'}]`
- New: `[{'name': 'state', 'type': 'module_state'}, {'name': 'list', 'type': 'list_head'}, {'name': 'name', 'type': '[ffi::c_char; 56usize]'}, {'name': 'mkobj', 'type': 'module_kobject'}, {'name': 'modinfo_attrs', 'type': '*mut module_attribute'}, {'name': 'version', 'type': '*const ffi::c_char'}, {'name': 'srcversion', 'type': '*const ffi::c_char'}, {'name': 'holders_dir', 'type': '*mut kobject'}, {'name': 'syms', 'type': '*mut kernel_symbol'}, {'name': 'crcs', 'type': '*const u32_'}, {'name': 'num_syms', 'type': 'ffi::c_uint'}, {'name': 'param_lock', 'type': 'mutex'}, {'name': 'kp', 'type': '*mut kernel_param'}, {'name': 'num_kp', 'type': 'ffi::c_uint'}, {'name': 'num_gpl_syms', 'type': 'ffi::c_uint'}, {'name': 'gpl_syms', 'type': '*const kernel_symbol'}, {'name': 'gpl_crcs', 'type': '*const u32_'}, {'name': 'using_gplonly_symbols', 'type': 'bool_'}, {'name': 'async_probe_requested', 'type': 'bool_'}, {'name': 'num_exentries', 'type': 'ffi::c_uint'}, {'name': 'extable', 'type': '*mut exception_table_entry'}, {'name': 'init', 'type': '::core::option::Option<unsafe extern "C" fn() -> ffi::c_int>'}, {'name': 'mem', 'type': '[module_memory; 7usize]'}, {'name': 'arch', 'type': 'mod_arch_specific'}, {'name': 'taints', 'type': 'ffi::c_ulong'}, {'name': 'num_bugs', 'type': 'ffi::c_uint'}, {'name': 'bug_list', 'type': 'list_head'}, {'name': 'bug_table', 'type': '*mut bug_entry'}, {'name': 'kallsyms', 'type': '*mut mod_kallsyms'}, {'name': 'core_kallsyms', 'type': 'mod_kallsyms'}, {'name': 'sect_attrs', 'type': '*mut module_sect_attrs'}, {'name': 'notes_attrs', 'type': '*mut module_notes_attrs'}, {'name': 'args', 'type': '*mut ffi::c_char'}, {'name': 'percpu', 'type': '*mut ffi::c_void'}, {'name': 'percpu_size', 'type': 'ffi::c_uint'}, {'name': 'noinstr_text_start', 'type': '*mut ffi::c_void'}, {'name': 'noinstr_text_size', 'type': 'ffi::c_uint'}, {'name': 'num_tracepoints', 'type': 'ffi::c_uint'}, {'name': 'tracepoints_ptrs', 'type': '*const ffi::c_int'}, {'name': 'num_srcu_structs', 'type': 'ffi::c_uint'}, {'name': 'srcu_struct_ptrs', 'type': '*mut *mut srcu_struct'}, {'name': 'jump_entries', 'type': '*mut jump_entry'}, {'name': 'num_jump_entries', 'type': 'ffi::c_uint'}, {'name': 'num_trace_bprintk_fmt', 'type': 'ffi::c_uint'}, {'name': 'trace_bprintk_fmt_start', 'type': '*mut *const ffi::c_char'}, {'name': 'trace_events', 'type': '*mut *mut trace_event_call'}, {'name': 'num_trace_events', 'type': 'ffi::c_uint'}, {'name': 'trace_evals', 'type': '*mut *mut trace_eval_map'}, {'name': 'num_trace_evals', 'type': 'ffi::c_uint'}, {'name': 'kprobes_text_start', 'type': '*mut ffi::c_void'}, {'name': 'kprobes_text_size', 'type': 'ffi::c_uint'}, {'name': 'kprobe_blacklist', 'type': '*mut ffi::c_ulong'}, {'name': 'num_kprobe_blacklist', 'type': 'ffi::c_uint'}, {'name': 'num_static_call_sites', 'type': 'ffi::c_int'}, {'name': 'static_call_sites', 'type': '*mut static_call_site'}, {'name': 'source_list', 'type': 'list_head'}, {'name': 'target_list', 'type': 'list_head'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'refcnt', 'type': 'atomic_t'}]`

### Rust Evidence

- Graph edges: `42`

## W-000566 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: pci_dev
- Explanation: pci_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': 'match_driver', 'type': 'bool_'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`
- New: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 11usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 11usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pri_cap', 'type': 'u16_'}, {'name': 'pri_reqs_alloc', 'type': 'u32_'}, {'name': '_bitfield_align_5', 'type': '[u8; 0]'}, {'name': '_bitfield_5', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`

### Rust Evidence

- Graph edges: `50`

## W-000568 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: phy_driver
- Explanation: phy_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mdiodrv', 'type': 'mdio_driver_common'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'name', 'type': '*mut ffi::c_char'}, {'name': 'phy_id_mask', 'type': 'u32_'}, {'name': 'features', 'type': '*const ffi::c_ulong'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'driver_data', 'type': '*const ffi::c_void'}, {'name': 'probe', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device) -> ffi::c_int>'}, {'name': 'inband_caps', 'type': '::core::option::Option<'}, {'name': 'config_inband', 'type': '::core::option::Option<'}, {'name': 'get_rate_matching', 'type': '::core::option::Option<'}, {'name': 'resume', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device) -> ffi::c_int>'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device)>'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'link_change_notify', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device)>'}, {'name': 'read_mmd', 'type': '::core::option::Option<'}, {'name': 'write_mmd', 'type': '::core::option::Option<'}, {'name': 'read_page', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device) -> ffi::c_int>'}, {'name': 'write_page', 'type': '::core::option::Option<'}, {'name': 'module_info', 'type': '::core::option::Option<'}, {'name': 'module_eeprom', 'type': '::core::option::Option<'}, {'name': 'cable_test_tdr_start', 'type': '::core::option::Option<'}, {'name': 'cable_test_get_status', 'type': '::core::option::Option<'}, {'name': 'get_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_link_stats', 'type': '::core::option::Option<'}, {'name': 'get_stats', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'set_loopback', 'type': '::core::option::Option<'}, {'name': 'get_sqi', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device) -> ffi::c_int>'}, {'name': 'get_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'set_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'get_plca_status', 'type': '::core::option::Option<'}, {'name': 'led_brightness_set', 'type': '::core::option::Option<'}, {'name': 'led_blink_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_is_supported', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_get', 'type': '::core::option::Option<'}, {'name': 'led_polarity_set', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'mdiodrv', 'type': 'mdio_driver_common'}, {'name': 'phy_id', 'type': 'u32_'}, {'name': 'name', 'type': '*mut ffi::c_char'}, {'name': 'phy_id_mask', 'type': 'u32_'}, {'name': 'features', 'type': '*const ffi::c_ulong'}, {'name': 'flags', 'type': 'u32_'}, {'name': 'driver_data', 'type': '*const ffi::c_void'}, {'name': 'probe', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device) -> ffi::c_int>'}, {'name': 'inband_caps', 'type': '::core::option::Option<'}, {'name': 'config_inband', 'type': '::core::option::Option<'}, {'name': 'get_rate_matching', 'type': '::core::option::Option<'}, {'name': 'resume', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device) -> ffi::c_int>'}, {'name': 'remove', 'type': '::core::option::Option<unsafe extern "C" fn(phydev: *mut phy_device)>'}, {'name': 'match_phy_device', 'type': '::core::option::Option<'}, {'name': 'set_wol', 'type': '::core::option::Option<'}, {'name': 'get_wol', 'type': '::core::option::Option<'}, {'name': 'link_change_notify', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device)>'}, {'name': 'read_mmd', 'type': '::core::option::Option<'}, {'name': 'write_mmd', 'type': '::core::option::Option<'}, {'name': 'read_page', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device) -> ffi::c_int>'}, {'name': 'write_page', 'type': '::core::option::Option<'}, {'name': 'module_info', 'type': '::core::option::Option<'}, {'name': 'module_eeprom', 'type': '::core::option::Option<'}, {'name': 'cable_test_tdr_start', 'type': '::core::option::Option<'}, {'name': 'cable_test_get_status', 'type': '::core::option::Option<'}, {'name': 'get_phy_stats', 'type': '::core::option::Option<'}, {'name': 'get_link_stats', 'type': '::core::option::Option<'}, {'name': 'get_stats', 'type': '::core::option::Option<'}, {'name': 'get_tunable', 'type': '::core::option::Option<'}, {'name': 'set_tunable', 'type': '::core::option::Option<'}, {'name': 'set_loopback', 'type': '::core::option::Option<'}, {'name': 'get_sqi', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut phy_device) -> ffi::c_int>'}, {'name': 'get_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'set_plca_cfg', 'type': '::core::option::Option<'}, {'name': 'get_plca_status', 'type': '::core::option::Option<'}, {'name': 'led_brightness_set', 'type': '::core::option::Option<'}, {'name': 'led_blink_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_is_supported', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_set', 'type': '::core::option::Option<'}, {'name': 'led_hw_control_get', 'type': '::core::option::Option<'}, {'name': 'led_polarity_set', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `31`

## W-000574 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: statx
- Explanation: statx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'stx_mask', 'type': '__u32'}, {'name': 'stx_blksize', 'type': '__u32'}, {'name': 'stx_attributes', 'type': '__u64'}, {'name': 'stx_nlink', 'type': '__u32'}, {'name': 'stx_uid', 'type': '__u32'}, {'name': 'stx_gid', 'type': '__u32'}, {'name': 'stx_mode', 'type': '__u16'}, {'name': '__spare0', 'type': '[__u16; 1usize]'}, {'name': 'stx_ino', 'type': '__u64'}, {'name': 'stx_size', 'type': '__u64'}, {'name': 'stx_blocks', 'type': '__u64'}, {'name': 'stx_attributes_mask', 'type': '__u64'}, {'name': 'stx_atime', 'type': 'statx_timestamp'}, {'name': 'stx_btime', 'type': 'statx_timestamp'}, {'name': 'stx_ctime', 'type': 'statx_timestamp'}, {'name': 'stx_mtime', 'type': 'statx_timestamp'}, {'name': 'stx_rdev_major', 'type': '__u32'}, {'name': 'stx_rdev_minor', 'type': '__u32'}, {'name': 'stx_dev_major', 'type': '__u32'}, {'name': 'stx_dev_minor', 'type': '__u32'}, {'name': 'stx_mnt_id', 'type': '__u64'}, {'name': 'stx_dio_mem_align', 'type': '__u32'}, {'name': 'stx_dio_offset_align', 'type': '__u32'}, {'name': 'stx_subvol', 'type': '__u64'}, {'name': 'stx_atomic_write_unit_min', 'type': '__u32'}, {'name': 'stx_atomic_write_unit_max', 'type': '__u32'}, {'name': 'stx_atomic_write_segments_max', 'type': '__u32'}, {'name': 'stx_dio_read_offset_align', 'type': '__u32'}, {'name': '__spare3', 'type': '[__u64; 9usize]'}]`
- New: `[{'name': 'stx_mask', 'type': '__u32'}, {'name': 'stx_blksize', 'type': '__u32'}, {'name': 'stx_attributes', 'type': '__u64'}, {'name': 'stx_nlink', 'type': '__u32'}, {'name': 'stx_uid', 'type': '__u32'}, {'name': 'stx_gid', 'type': '__u32'}, {'name': 'stx_mode', 'type': '__u16'}, {'name': '__spare0', 'type': '[__u16; 1usize]'}, {'name': 'stx_ino', 'type': '__u64'}, {'name': 'stx_size', 'type': '__u64'}, {'name': 'stx_blocks', 'type': '__u64'}, {'name': 'stx_attributes_mask', 'type': '__u64'}, {'name': 'stx_atime', 'type': 'statx_timestamp'}, {'name': 'stx_btime', 'type': 'statx_timestamp'}, {'name': 'stx_ctime', 'type': 'statx_timestamp'}, {'name': 'stx_mtime', 'type': 'statx_timestamp'}, {'name': 'stx_rdev_major', 'type': '__u32'}, {'name': 'stx_rdev_minor', 'type': '__u32'}, {'name': 'stx_dev_major', 'type': '__u32'}, {'name': 'stx_dev_minor', 'type': '__u32'}, {'name': 'stx_mnt_id', 'type': '__u64'}, {'name': 'stx_dio_mem_align', 'type': '__u32'}, {'name': 'stx_dio_offset_align', 'type': '__u32'}, {'name': 'stx_subvol', 'type': '__u64'}, {'name': 'stx_atomic_write_unit_min', 'type': '__u32'}, {'name': 'stx_atomic_write_unit_max', 'type': '__u32'}, {'name': 'stx_atomic_write_segments_max', 'type': '__u32'}, {'name': 'stx_dio_read_offset_align', 'type': '__u32'}, {'name': 'stx_atomic_write_unit_max_opt', 'type': '__u32'}, {'name': '__spare2', 'type': '[__u32; 1usize]'}, {'name': '__spare3', 'type': '[__u64; 8usize]'}]`

### Rust Evidence

- Graph edges: `34`

## W-000578 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: vm_area_struct
- Explanation: vm_area_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__bindgen_anon_1', 'type': 'vm_area_struct__bindgen_ty_1'}, {'name': 'vm_mm', 'type': '*mut mm_struct'}, {'name': 'vm_page_prot', 'type': 'pgprot_t'}, {'name': '__bindgen_anon_2', 'type': 'vm_area_struct__bindgen_ty_2'}, {'name': 'vm_lock_seq', 'type': 'ffi::c_uint'}, {'name': 'anon_vma_chain', 'type': 'list_head'}, {'name': 'anon_vma', 'type': '*mut anon_vma'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'vm_pgoff', 'type': 'ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_private_data', 'type': '*mut ffi::c_void'}, {'name': 'swap_readahead_info', 'type': 'atomic_long_t'}, {'name': 'vm_policy', 'type': '*mut mempolicy'}, {'name': '__bindgen_padding_0', 'type': '[u32; 2usize]'}, {'name': 'vm_refcnt', 'type': 'refcount_t'}, {'name': 'shared', 'type': 'vm_area_struct__bindgen_ty_3'}, {'name': 'vm_userfaultfd_ctx', 'type': 'vm_userfaultfd_ctx'}]`
- New: `[{'name': '__bindgen_anon_1', 'type': 'vm_area_struct__bindgen_ty_1'}, {'name': 'vm_mm', 'type': '*mut mm_struct'}, {'name': 'vm_page_prot', 'type': 'pgprot_t'}, {'name': '__bindgen_anon_2', 'type': 'vm_area_struct__bindgen_ty_2'}, {'name': 'vm_lock_seq', 'type': 'ffi::c_uint'}, {'name': 'anon_vma_chain', 'type': 'list_head'}, {'name': 'anon_vma', 'type': '*mut anon_vma'}, {'name': 'vm_ops', 'type': '*const vm_operations_struct'}, {'name': 'vm_pgoff', 'type': 'ffi::c_ulong'}, {'name': 'vm_file', 'type': '*mut file'}, {'name': 'vm_private_data', 'type': '*mut ffi::c_void'}, {'name': 'swap_readahead_info', 'type': 'atomic_long_t'}, {'name': 'vm_policy', 'type': '*mut mempolicy'}, {'name': '__bindgen_padding_0', 'type': '[u32; 2usize]'}, {'name': 'vm_refcnt', 'type': 'refcount_t'}, {'name': 'shared', 'type': 'vm_area_struct__bindgen_ty_3'}, {'name': 'vm_userfaultfd_ctx', 'type': 'vm_userfaultfd_ctx'}, {'name': 'pfnmap_track_ctx', 'type': '*mut pfnmap_track_ctx'}]`

### Rust Evidence

- Graph edges: `42`

## W-000579 FieldDrift

- Risk: High
- Score: 12.6
- Symbol: zone
- Explanation: zone changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_watermark', 'type': '[ffi::c_ulong; 4usize]'}, {'name': 'watermark_boost', 'type': 'ffi::c_ulong'}, {'name': 'nr_reserved_highatomic', 'type': 'ffi::c_ulong'}, {'name': 'nr_free_highatomic', 'type': 'ffi::c_ulong'}, {'name': 'lowmem_reserve', 'type': '[ffi::c_long; 4usize]'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'zone_pgdat', 'type': '*mut pglist_data'}, {'name': 'per_cpu_pageset', 'type': '*mut per_cpu_pages'}, {'name': 'per_cpu_zonestats', 'type': '*mut per_cpu_zonestat'}, {'name': 'pageset_high_min', 'type': 'ffi::c_int'}, {'name': 'pageset_high_max', 'type': 'ffi::c_int'}, {'name': 'pageset_batch', 'type': 'ffi::c_int'}, {'name': 'zone_start_pfn', 'type': 'ffi::c_ulong'}, {'name': 'managed_pages', 'type': 'atomic_long_t'}, {'name': 'spanned_pages', 'type': 'ffi::c_ulong'}, {'name': 'present_pages', 'type': 'ffi::c_ulong'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'initialized', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': 'free_area', 'type': '[free_area; 11usize]'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'trylock_free_pages', 'type': 'llist_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 2usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'percpu_drift_mark', 'type': 'ffi::c_ulong'}, {'name': 'compact_cached_free_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_cached_migrate_pfn', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'compact_init_migrate_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_init_free_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_considered', 'type': 'ffi::c_uint'}, {'name': 'compact_defer_shift', 'type': 'ffi::c_uint'}, {'name': 'compact_order_failed', 'type': 'ffi::c_int'}, {'name': 'compact_blockskip_flush', 'type': 'bool_'}, {'name': 'contiguous', 'type': 'bool_'}, {'name': '__bindgen_padding_2', 'type': '[u64; 0usize]'}, {'name': '_pad3_', 'type': 'cacheline_padding'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 11usize]'}, {'name': 'vm_numa_event', 'type': '[atomic_long_t; 6usize]'}]`
- New: `[{'name': '_watermark', 'type': '[ffi::c_ulong; 4usize]'}, {'name': 'watermark_boost', 'type': 'ffi::c_ulong'}, {'name': 'nr_reserved_highatomic', 'type': 'ffi::c_ulong'}, {'name': 'nr_free_highatomic', 'type': 'ffi::c_ulong'}, {'name': 'lowmem_reserve', 'type': '[ffi::c_long; 4usize]'}, {'name': 'node', 'type': 'ffi::c_int'}, {'name': 'zone_pgdat', 'type': '*mut pglist_data'}, {'name': 'per_cpu_pageset', 'type': '*mut per_cpu_pages'}, {'name': 'per_cpu_zonestats', 'type': '*mut per_cpu_zonestat'}, {'name': 'pageset_high_min', 'type': 'ffi::c_int'}, {'name': 'pageset_high_max', 'type': 'ffi::c_int'}, {'name': 'pageset_batch', 'type': 'ffi::c_int'}, {'name': 'zone_start_pfn', 'type': 'ffi::c_ulong'}, {'name': 'managed_pages', 'type': 'atomic_long_t'}, {'name': 'spanned_pages', 'type': 'ffi::c_ulong'}, {'name': 'present_pages', 'type': 'ffi::c_ulong'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'initialized', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u64'}, {'name': '_pad1_', 'type': 'cacheline_padding'}, {'name': 'free_area', 'type': '[free_area; 11usize]'}, {'name': 'flags', 'type': 'ffi::c_ulong'}, {'name': 'lock', 'type': 'spinlock_t'}, {'name': 'trylock_free_pages', 'type': 'llist_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 2usize]'}, {'name': '_pad2_', 'type': 'cacheline_padding'}, {'name': 'percpu_drift_mark', 'type': 'ffi::c_ulong'}, {'name': 'compact_cached_free_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_cached_migrate_pfn', 'type': '[ffi::c_ulong; 2usize]'}, {'name': 'compact_init_migrate_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_init_free_pfn', 'type': 'ffi::c_ulong'}, {'name': 'compact_considered', 'type': 'ffi::c_uint'}, {'name': 'compact_defer_shift', 'type': 'ffi::c_uint'}, {'name': 'compact_order_failed', 'type': 'ffi::c_int'}, {'name': 'compact_blockskip_flush', 'type': 'bool_'}, {'name': 'contiguous', 'type': 'bool_'}, {'name': '__bindgen_padding_2', 'type': '[u64; 0usize]'}, {'name': '_pad3_', 'type': 'cacheline_padding'}, {'name': 'vm_stat', 'type': '[atomic_long_t; 10usize]'}, {'name': 'vm_numa_event', 'type': '[atomic_long_t; 6usize]'}]`

### Rust Evidence

- Graph edges: `37`

## W-001105 NullabilityDrift

- Risk: High
- Score: 12.6
- Symbol: dev_pm_opp_find_bw_ceil
- Explanation: dev_pm_opp_find_bw_ceil has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/pm_opp.h:344 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:925 `Table::opp_from_bw` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:922 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`

## W-001107 NullabilityDrift

- Risk: High
- Score: 12.6
- Symbol: dev_pm_opp_find_freq_ceil_indexed
- Explanation: dev_pm_opp_find_freq_ceil_indexed has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/pm_opp.h:320 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:874 `Table::set_opp` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:871 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`

## W-001108 NullabilityDrift

- Risk: High
- Score: 12.6
- Symbol: dev_pm_opp_find_freq_exact_indexed
- Explanation: dev_pm_opp_find_freq_exact_indexed has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/pm_opp.h:296 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:862 `Table::set_opp` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:858 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and`

## W-001110 NullabilityDrift

- Risk: High
- Score: 12.6
- Symbol: dev_pm_opp_find_level_ceil
- Explanation: dev_pm_opp_find_level_ceil has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/pm_opp.h:332 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:900 `Table::opp_from_level` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:897 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`

## W-000006 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: __cpumask_set_cpu
- Explanation: __cpumask_set_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `9`

## W-000058 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: clk_enable
- Explanation: clk_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `9`

## W-000060 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: clk_get_optional
- Explanation: clk_get_optional changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `9`

## W-000255 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: drm_dev_put
- Explanation: drm_dev_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `9`

## W-000320 SignatureDrift

- Risk: High
- Score: 12.4
- Symbol: drm_ioctl_flags
- Explanation: drm_ioctl_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `9`

## W-000057 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: clk_disable_unprepare
- Explanation: clk_disable_unprepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000061 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: clk_get_rate
- Explanation: clk_get_rate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000063 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: clk_prepare_enable
- Explanation: clk_prepare_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000064 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: clk_put
- Explanation: clk_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000066 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: clk_unprepare
- Explanation: clk_unprepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000101 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: cpufreq_cpu_put
- Explanation: cpufreq_cpu_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000117 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: cpufreq_generic_frequency_table_verify
- Explanation: cpufreq_generic_frequency_table_verify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000256 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: drm_dev_register
- Explanation: drm_dev_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000526 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: vma_lookup
- Explanation: vma_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `8`

## W-000557 FieldDrift

- Risk: High
- Score: 12.2
- Symbol: gendisk
- Explanation: gendisk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'major', 'type': 'ffi::c_int'}, {'name': 'first_minor', 'type': 'ffi::c_int'}, {'name': 'minors', 'type': 'ffi::c_int'}, {'name': 'disk_name', 'type': '[ffi::c_char; 32usize]'}, {'name': 'events', 'type': 'ffi::c_ushort'}, {'name': 'event_flags', 'type': 'ffi::c_ushort'}, {'name': 'part_tbl', 'type': 'xarray'}, {'name': 'part0', 'type': '*mut block_device'}, {'name': 'fops', 'type': '*const block_device_operations'}, {'name': 'queue', 'type': '*mut request_queue'}, {'name': 'private_data', 'type': '*mut ffi::c_void'}, {'name': 'bio_split', 'type': 'bio_set'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'state', 'type': 'ffi::c_ulong'}, {'name': 'open_mutex', 'type': 'mutex'}, {'name': 'open_partitions', 'type': 'ffi::c_uint'}, {'name': 'bdi', 'type': '*mut backing_dev_info'}, {'name': 'queue_kobj', 'type': 'kobject'}, {'name': 'slave_dir', 'type': '*mut kobject'}, {'name': 'slave_bdevs', 'type': 'list_head'}, {'name': 'random', 'type': '*mut timer_rand_state'}, {'name': 'sync_io', 'type': 'atomic_t'}, {'name': 'ev', 'type': '*mut disk_events'}, {'name': 'cdi', 'type': '*mut cdrom_device_info'}, {'name': 'node_id', 'type': 'ffi::c_int'}, {'name': 'bb', 'type': '*mut badblocks'}, {'name': 'lockdep_map', 'type': 'lockdep_map'}, {'name': 'diskseq', 'type': 'u64_'}, {'name': 'open_mode', 'type': 'blk_mode_t'}, {'name': 'ia_ranges', 'type': '*mut blk_independent_access_ranges'}]`
- New: `[{'name': 'major', 'type': 'ffi::c_int'}, {'name': 'first_minor', 'type': 'ffi::c_int'}, {'name': 'minors', 'type': 'ffi::c_int'}, {'name': 'disk_name', 'type': '[ffi::c_char; 32usize]'}, {'name': 'events', 'type': 'ffi::c_ushort'}, {'name': 'event_flags', 'type': 'ffi::c_ushort'}, {'name': 'part_tbl', 'type': 'xarray'}, {'name': 'part0', 'type': '*mut block_device'}, {'name': 'fops', 'type': '*const block_device_operations'}, {'name': 'queue', 'type': '*mut request_queue'}, {'name': 'private_data', 'type': '*mut ffi::c_void'}, {'name': 'bio_split', 'type': 'bio_set'}, {'name': 'flags', 'type': 'ffi::c_int'}, {'name': 'state', 'type': 'ffi::c_ulong'}, {'name': 'open_mutex', 'type': 'mutex'}, {'name': 'open_partitions', 'type': 'ffi::c_uint'}, {'name': 'bdi', 'type': '*mut backing_dev_info'}, {'name': 'queue_kobj', 'type': 'kobject'}, {'name': 'slave_dir', 'type': '*mut kobject'}, {'name': 'slave_bdevs', 'type': 'list_head'}, {'name': 'random', 'type': '*mut timer_rand_state'}, {'name': 'ev', 'type': '*mut disk_events'}, {'name': 'cdi', 'type': '*mut cdrom_device_info'}, {'name': 'node_id', 'type': 'ffi::c_int'}, {'name': 'bb', 'type': '*mut badblocks'}, {'name': 'lockdep_map', 'type': 'lockdep_map'}, {'name': 'diskseq', 'type': 'u64_'}, {'name': 'open_mode', 'type': 'blk_mode_t'}, {'name': 'ia_ranges', 'type': '*mut blk_independent_access_ranges'}, {'name': 'rqos_state_mutex', 'type': 'mutex'}]`

### Rust Evidence

- Graph edges: `18`

## W-001035 SignatureDrift

- Risk: High
- Score: 12.2
- Symbol: PTR_ERR
- Explanation: PTR_ERR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['ptr'], 'return_type': 'return'}`
- New: `{'params': ['opp'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `8`

## W-000146 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: cpumask_empty
- Explanation: cpumask_empty changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000147 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: cpumask_full
- Explanation: cpumask_full changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000148 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: cpumask_test_cpu
- Explanation: cpumask_test_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000279 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: drm_gem_handle_create
- Explanation: drm_gem_handle_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000294 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: drm_gem_object_get
- Explanation: drm_gem_object_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000297 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: drm_gem_object_lookup
- Explanation: drm_gem_object_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000375 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: drm_vma_node_offset_addr
- Explanation: drm_vma_node_offset_addr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000430 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: mmap_read_trylock
- Explanation: mmap_read_trylock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000432 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: mmdrop
- Explanation: mmdrop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000460 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: raw_smp_processor_id
- Explanation: raw_smp_processor_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000542 SignatureDrift

- Risk: High
- Score: 12.0
- Symbol: xa_lock
- Explanation: xa_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `7`

## W-000550 FieldDrift

- Risk: High
- Score: 12.0
- Symbol: cgroup_subsys
- Explanation: cgroup_subsys changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'css_alloc', 'type': '::core::option::Option<'}, {'name': 'css_offline', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_released', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_free', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_reset', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_killed', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_rstat_flush', 'type': '::core::option::Option<'}, {'name': 'css_extra_stat_show', 'type': '::core::option::Option<'}, {'name': 'css_local_stat_show', 'type': '::core::option::Option<'}, {'name': 'cancel_attach', 'type': '::core::option::Option<unsafe extern "C" fn(tset: *mut cgroup_taskset)>'}, {'name': 'attach', 'type': '::core::option::Option<unsafe extern "C" fn(tset: *mut cgroup_taskset)>'}, {'name': 'post_attach', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'can_fork', 'type': '::core::option::Option<'}, {'name': 'fork', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'bind', 'type': '::core::option::Option<unsafe extern "C" fn(root_css: *mut cgroup_subsys_state)>'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'legacy_name', 'type': '*const ffi::c_char'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'css_idr', 'type': 'idr'}, {'name': 'cfts', 'type': 'list_head'}, {'name': 'dfl_cftypes', 'type': '*mut cftype'}, {'name': 'legacy_cftypes', 'type': '*mut cftype'}, {'name': 'depends_on', 'type': 'ffi::c_uint'}]`
- New: `[{'name': 'css_alloc', 'type': '::core::option::Option<'}, {'name': 'css_offline', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_released', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_free', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_reset', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_killed', 'type': '::core::option::Option<unsafe extern "C" fn(css: *mut cgroup_subsys_state)>'}, {'name': 'css_rstat_flush', 'type': '::core::option::Option<'}, {'name': 'css_extra_stat_show', 'type': '::core::option::Option<'}, {'name': 'css_local_stat_show', 'type': '::core::option::Option<'}, {'name': 'cancel_attach', 'type': '::core::option::Option<unsafe extern "C" fn(tset: *mut cgroup_taskset)>'}, {'name': 'attach', 'type': '::core::option::Option<unsafe extern "C" fn(tset: *mut cgroup_taskset)>'}, {'name': 'post_attach', 'type': '::core::option::Option<unsafe extern "C" fn()>'}, {'name': 'can_fork', 'type': '::core::option::Option<'}, {'name': 'fork', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'exit', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(task: *mut task_struct)>'}, {'name': 'bind', 'type': '::core::option::Option<unsafe extern "C" fn(root_css: *mut cgroup_subsys_state)>'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'legacy_name', 'type': '*const ffi::c_char'}, {'name': 'root', 'type': '*mut cgroup_root'}, {'name': 'css_idr', 'type': 'idr'}, {'name': 'cfts', 'type': 'list_head'}, {'name': 'dfl_cftypes', 'type': '*mut cftype'}, {'name': 'legacy_cftypes', 'type': '*mut cftype'}, {'name': 'depends_on', 'type': 'ffi::c_uint'}, {'name': 'rstat_ss_lock', 'type': 'spinlock_t'}, {'name': 'rstat_ss_cpu_lock', 'type': '*mut raw_spinlock_t'}]`

### Rust Evidence

- Graph edges: `17`

## W-000005 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: __cpumask_clear_cpu
- Explanation: __cpumask_clear_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000038 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: auxiliary_device_delete
- Explanation: auxiliary_device_delete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000065 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: clk_set_rate
- Explanation: clk_set_rate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000118 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: cpufreq_generic_get
- Explanation: cpufreq_generic_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000120 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: cpufreq_generic_suspend
- Explanation: cpufreq_generic_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000129 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: cpufreq_register_driver
- Explanation: cpufreq_register_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000130 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: cpufreq_register_em_with_opp
- Explanation: cpufreq_register_em_with_opp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000298 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: drm_gem_object_put
- Explanation: drm_gem_object_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000299 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: drm_gem_object_release
- Explanation: drm_gem_object_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000341 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: drm_modeset_lock
- Explanation: drm_modeset_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000350 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: drm_open_helper
- Explanation: drm_open_helper changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000429 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: mmap_read_lock
- Explanation: mmap_read_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000431 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: mmap_read_unlock
- Explanation: mmap_read_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000543 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: xa_trylock
- Explanation: xa_trylock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000544 SignatureDrift

- Risk: High
- Score: 11.8
- Symbol: xa_unlock
- Explanation: xa_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `6`

## W-000547 FieldDrift

- Risk: High
- Score: 11.8
- Symbol: blk_mq_tag_set
- Explanation: blk_mq_tag_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'ops', 'type': '*const blk_mq_ops'}, {'name': 'map', 'type': '[blk_mq_queue_map; 3usize]'}, {'name': 'nr_maps', 'type': 'ffi::c_uint'}, {'name': 'nr_hw_queues', 'type': 'ffi::c_uint'}, {'name': 'queue_depth', 'type': 'ffi::c_uint'}, {'name': 'reserved_tags', 'type': 'ffi::c_uint'}, {'name': 'cmd_size', 'type': 'ffi::c_uint'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'timeout', 'type': 'ffi::c_uint'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'tags', 'type': '*mut *mut blk_mq_tags'}, {'name': 'shared_tags', 'type': '*mut blk_mq_tags'}, {'name': 'tag_list_lock', 'type': 'mutex'}, {'name': 'tag_list', 'type': 'list_head'}, {'name': 'srcu', 'type': '*mut srcu_struct'}]`
- New: `[{'name': 'ops', 'type': '*const blk_mq_ops'}, {'name': 'map', 'type': '[blk_mq_queue_map; 3usize]'}, {'name': 'nr_maps', 'type': 'ffi::c_uint'}, {'name': 'nr_hw_queues', 'type': 'ffi::c_uint'}, {'name': 'queue_depth', 'type': 'ffi::c_uint'}, {'name': 'reserved_tags', 'type': 'ffi::c_uint'}, {'name': 'cmd_size', 'type': 'ffi::c_uint'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'timeout', 'type': 'ffi::c_uint'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'tags', 'type': '*mut *mut blk_mq_tags'}, {'name': 'shared_tags', 'type': '*mut blk_mq_tags'}, {'name': 'tag_list_lock', 'type': 'mutex'}, {'name': 'tag_list', 'type': 'list_head'}, {'name': 'srcu', 'type': '*mut srcu_struct'}, {'name': 'update_nr_hwq_lock', 'type': 'rw_semaphore'}]`

### Rust Evidence

- Graph edges: `16`

## W-000011 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: __drm_dev_alloc
- Explanation: __drm_dev_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000044 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: auxiliary_driver_unregister
- Explanation: auxiliary_driver_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000045 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: auxiliary_get_drvdata
- Explanation: auxiliary_get_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000141 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: cpufreq_unregister_driver
- Explanation: cpufreq_unregister_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000152 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: dev_is_pci
- Explanation: dev_is_pci changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000153 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: dev_is_platform
- Explanation: dev_is_platform changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000253 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: drm_dev_get
- Explanation: drm_dev_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000259 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: drm_dev_unregister
- Explanation: drm_dev_unregister changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000267 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: drm_gem_create_mmap_offset
- Explanation: drm_gem_create_mmap_offset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000420 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: init_completion
- Explanation: init_completion changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000435 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: mmgrab
- Explanation: mmgrab changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000438 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: mutex_destroy
- Explanation: mutex_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000525 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: vma_end_read
- Explanation: vma_end_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000540 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: xa_err
- Explanation: xa_err changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000541 SignatureDrift

- Risk: High
- Score: 11.6
- Symbol: xa_init_flags
- Explanation: xa_init_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `5`

## W-000576 FieldDrift

- Risk: High
- Score: 11.6
- Symbol: task_struct
- Explanation: task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'ffi::c_uint'}, {'name': 'saved_state', 'type': 'ffi::c_uint'}, {'name': 'stack', 'type': '*mut ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'ptrace', 'type': 'ffi::c_uint'}, {'name': 'on_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_cpu', 'type': 'ffi::c_int'}, {'name': 'on_rq', 'type': 'ffi::c_int'}, {'name': 'prio', 'type': 'ffi::c_int'}, {'name': 'static_prio', 'type': 'ffi::c_int'}, {'name': 'normal_prio', 'type': 'ffi::c_int'}, {'name': 'rt_priority', 'type': 'ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut ffi::c_void'}, {'name': 'migration_disabled', 'type': 'ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'trc_reader_nesting', 'type': 'ffi::c_int'}, {'name': 'trc_ipi_to_cpu', 'type': 'ffi::c_int'}, {'name': 'trc_reader_special', 'type': 'rcu_special'}, {'name': 'trc_holdout_list', 'type': 'list_head'}, {'name': 'trc_blkd_node', 'type': 'list_head'}, {'name': 'trc_blkd_cpu', 'type': 'ffi::c_int'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'ffi::c_int'}, {'name': 'exit_code', 'type': 'ffi::c_int'}, {'name': 'exit_signal', 'type': 'ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'ffi::c_int'}, {'name': 'jobctl', 'type': 'ffi::c_ulong'}, {'name': 'personality', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'worker_private', 'type': '*mut ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'perf_ctx_data', 'type': '*mut perf_ctx_data'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': '__bindgen_padding_1', 'type': '[u64; 3usize]'}, {'name': 'thread', 'type': 'thread_struct'}]`
- New: `[{'name': 'thread_info', 'type': 'thread_info'}, {'name': '__state', 'type': 'ffi::c_uint'}, {'name': 'saved_state', 'type': 'ffi::c_uint'}, {'name': 'stack', 'type': '*mut ffi::c_void'}, {'name': 'usage', 'type': 'refcount_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'ptrace', 'type': 'ffi::c_uint'}, {'name': 'on_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_entry', 'type': '__call_single_node'}, {'name': 'wakee_flips', 'type': 'ffi::c_uint'}, {'name': 'wakee_flip_decay_ts', 'type': 'ffi::c_ulong'}, {'name': 'last_wakee', 'type': '*mut task_struct'}, {'name': 'recent_used_cpu', 'type': 'ffi::c_int'}, {'name': 'wake_cpu', 'type': 'ffi::c_int'}, {'name': 'on_rq', 'type': 'ffi::c_int'}, {'name': 'prio', 'type': 'ffi::c_int'}, {'name': 'static_prio', 'type': 'ffi::c_int'}, {'name': 'normal_prio', 'type': 'ffi::c_int'}, {'name': 'rt_priority', 'type': 'ffi::c_uint'}, {'name': '__bindgen_padding_0', 'type': '[u64; 0usize]'}, {'name': 'se', 'type': 'sched_entity'}, {'name': 'rt', 'type': 'sched_rt_entity'}, {'name': 'dl', 'type': 'sched_dl_entity'}, {'name': 'dl_server', 'type': '*mut sched_dl_entity'}, {'name': 'sched_class', 'type': '*mut sched_class'}, {'name': 'sched_task_group', 'type': '*mut task_group'}, {'name': 'stats', 'type': 'sched_statistics'}, {'name': 'btrace_seq', 'type': 'ffi::c_uint'}, {'name': 'policy', 'type': 'ffi::c_uint'}, {'name': 'max_allowed_capacity', 'type': 'ffi::c_ulong'}, {'name': 'nr_cpus_allowed', 'type': 'ffi::c_int'}, {'name': 'cpus_ptr', 'type': '*const cpumask_t'}, {'name': 'user_cpus_ptr', 'type': '*mut cpumask_t'}, {'name': 'cpus_mask', 'type': 'cpumask_t'}, {'name': 'migration_pending', 'type': '*mut ffi::c_void'}, {'name': 'migration_disabled', 'type': 'ffi::c_ushort'}, {'name': 'migration_flags', 'type': 'ffi::c_ushort'}, {'name': 'rcu_read_lock_nesting', 'type': 'ffi::c_int'}, {'name': 'rcu_read_unlock_special', 'type': 'rcu_special'}, {'name': 'rcu_node_entry', 'type': 'list_head'}, {'name': 'rcu_blocked_node', 'type': '*mut rcu_node'}, {'name': 'rcu_tasks_nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'rcu_tasks_holdout', 'type': 'u8_'}, {'name': 'rcu_tasks_idx', 'type': 'u8_'}, {'name': 'rcu_tasks_idle_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_holdout_list', 'type': 'list_head'}, {'name': 'rcu_tasks_exit_cpu', 'type': 'ffi::c_int'}, {'name': 'rcu_tasks_exit_list', 'type': 'list_head'}, {'name': 'trc_reader_nesting', 'type': 'ffi::c_int'}, {'name': 'trc_ipi_to_cpu', 'type': 'ffi::c_int'}, {'name': 'trc_reader_special', 'type': 'rcu_special'}, {'name': 'trc_holdout_list', 'type': 'list_head'}, {'name': 'trc_blkd_node', 'type': 'list_head'}, {'name': 'trc_blkd_cpu', 'type': 'ffi::c_int'}, {'name': 'sched_info', 'type': 'sched_info'}, {'name': 'tasks', 'type': 'list_head'}, {'name': 'pushable_tasks', 'type': 'plist_node'}, {'name': 'pushable_dl_tasks', 'type': 'rb_node'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'active_mm', 'type': '*mut mm_struct'}, {'name': 'faults_disabled_mapping', 'type': '*mut address_space'}, {'name': 'exit_state', 'type': 'ffi::c_int'}, {'name': 'exit_code', 'type': 'ffi::c_int'}, {'name': 'exit_signal', 'type': 'ffi::c_int'}, {'name': 'pdeath_signal', 'type': 'ffi::c_int'}, {'name': 'jobctl', 'type': 'ffi::c_ulong'}, {'name': 'personality', 'type': 'ffi::c_uint'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'atomic_flags', 'type': 'ffi::c_ulong'}, {'name': 'restart_block', 'type': 'restart_block'}, {'name': 'pid', 'type': 'pid_t'}, {'name': 'tgid', 'type': 'pid_t'}, {'name': 'stack_canary', 'type': 'ffi::c_ulong'}, {'name': 'real_parent', 'type': '*mut task_struct'}, {'name': 'parent', 'type': '*mut task_struct'}, {'name': 'children', 'type': 'list_head'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'group_leader', 'type': '*mut task_struct'}, {'name': 'ptraced', 'type': 'list_head'}, {'name': 'ptrace_entry', 'type': 'list_head'}, {'name': 'thread_pid', 'type': '*mut pid'}, {'name': 'pid_links', 'type': '[hlist_node; 4usize]'}, {'name': 'thread_node', 'type': 'list_head'}, {'name': 'vfork_done', 'type': '*mut completion'}, {'name': 'set_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'clear_child_tid', 'type': '*mut ffi::c_int'}, {'name': 'worker_private', 'type': '*mut ffi::c_void'}, {'name': 'utime', 'type': 'u64_'}, {'name': 'stime', 'type': 'u64_'}, {'name': 'gtime', 'type': 'u64_'}, {'name': 'prev_cputime', 'type': 'prev_cputime'}, {'name': 'nvcsw', 'type': 'ffi::c_ulong'}, {'name': 'nivcsw', 'type': 'ffi::c_ulong'}, {'name': 'start_time', 'type': 'u64_'}, {'name': 'start_boottime', 'type': 'u64_'}, {'name': 'min_flt', 'type': 'ffi::c_ulong'}, {'name': 'maj_flt', 'type': 'ffi::c_ulong'}, {'name': 'posix_cputimers', 'type': 'posix_cputimers'}, {'name': 'posix_cputimers_work', 'type': 'posix_cputimers_work'}, {'name': 'ptracer_cred', 'type': '*const cred'}, {'name': 'real_cred', 'type': '*const cred'}, {'name': 'cred', 'type': '*const cred'}, {'name': 'cached_requested_key', 'type': '*mut key'}, {'name': 'comm', 'type': '[ffi::c_char; 16usize]'}, {'name': 'nameidata', 'type': '*mut nameidata'}, {'name': 'sysvsem', 'type': 'sysv_sem'}, {'name': 'sysvshm', 'type': 'sysv_shm'}, {'name': 'fs', 'type': '*mut fs_struct'}, {'name': 'files', 'type': '*mut files_struct'}, {'name': 'io_uring', 'type': '*mut io_uring_task'}, {'name': 'nsproxy', 'type': '*mut nsproxy'}, {'name': 'signal', 'type': '*mut signal_struct'}, {'name': 'sighand', 'type': '*mut sighand_struct'}, {'name': 'blocked', 'type': 'sigset_t'}, {'name': 'real_blocked', 'type': 'sigset_t'}, {'name': 'saved_sigmask', 'type': 'sigset_t'}, {'name': 'pending', 'type': 'sigpending'}, {'name': 'sas_ss_sp', 'type': 'ffi::c_ulong'}, {'name': 'sas_ss_size', 'type': 'usize'}, {'name': 'sas_ss_flags', 'type': 'ffi::c_uint'}, {'name': 'task_works', 'type': '*mut callback_head'}, {'name': 'audit_context', 'type': '*mut audit_context'}, {'name': 'loginuid', 'type': 'kuid_t'}, {'name': 'sessionid', 'type': 'ffi::c_uint'}, {'name': 'seccomp', 'type': 'seccomp'}, {'name': 'syscall_dispatch', 'type': 'syscall_user_dispatch'}, {'name': 'parent_exec_id', 'type': 'u64_'}, {'name': 'self_exec_id', 'type': 'u64_'}, {'name': 'alloc_lock', 'type': 'spinlock_t'}, {'name': 'pi_lock', 'type': 'raw_spinlock_t'}, {'name': 'wake_q', 'type': 'wake_q_node'}, {'name': 'pi_waiters', 'type': 'rb_root_cached'}, {'name': 'pi_top_task', 'type': '*mut task_struct'}, {'name': 'pi_blocked_on', 'type': '*mut rt_mutex_waiter'}, {'name': 'journal_info', 'type': '*mut ffi::c_void'}, {'name': 'bio_list', 'type': '*mut bio_list'}, {'name': 'plug', 'type': '*mut blk_plug'}, {'name': 'reclaim_state', 'type': '*mut reclaim_state'}, {'name': 'io_context', 'type': '*mut io_context'}, {'name': 'capture_control', 'type': '*mut capture_control'}, {'name': 'ptrace_message', 'type': 'ffi::c_ulong'}, {'name': 'last_siginfo', 'type': '*mut kernel_siginfo_t'}, {'name': 'ioac', 'type': 'task_io_accounting'}, {'name': 'acct_rss_mem1', 'type': 'u64_'}, {'name': 'acct_vm_mem1', 'type': 'u64_'}, {'name': 'acct_timexpd', 'type': 'u64_'}, {'name': 'mems_allowed', 'type': 'nodemask_t'}, {'name': 'mems_allowed_seq', 'type': 'seqcount_spinlock_t'}, {'name': 'cpuset_mem_spread_rotor', 'type': 'ffi::c_int'}, {'name': 'cgroups', 'type': '*mut css_set'}, {'name': 'cg_list', 'type': 'list_head'}, {'name': 'robust_list', 'type': '*mut robust_list_head'}, {'name': 'compat_robust_list', 'type': '*mut compat_robust_list_head'}, {'name': 'pi_state_list', 'type': 'list_head'}, {'name': 'pi_state_cache', 'type': '*mut futex_pi_state'}, {'name': 'futex_exit_mutex', 'type': 'mutex'}, {'name': 'futex_state', 'type': 'ffi::c_uint'}, {'name': 'perf_recursion', 'type': '[u8_; 4usize]'}, {'name': 'perf_event_ctxp', 'type': '*mut perf_event_context'}, {'name': 'perf_event_mutex', 'type': 'mutex'}, {'name': 'perf_event_list', 'type': 'list_head'}, {'name': 'perf_ctx_data', 'type': '*mut perf_ctx_data'}, {'name': 'mempolicy', 'type': '*mut mempolicy'}, {'name': 'il_prev', 'type': 'ffi::c_short'}, {'name': 'il_weight', 'type': 'u8_'}, {'name': 'pref_node_fork', 'type': 'ffi::c_short'}, {'name': 'rseq', 'type': '*mut rseq'}, {'name': 'rseq_len', 'type': 'u32_'}, {'name': 'rseq_sig', 'type': 'u32_'}, {'name': 'rseq_event_mask', 'type': 'ffi::c_ulong'}, {'name': 'mm_cid', 'type': 'ffi::c_int'}, {'name': 'last_mm_cid', 'type': 'ffi::c_int'}, {'name': 'migrate_from_cpu', 'type': 'ffi::c_int'}, {'name': 'mm_cid_active', 'type': 'ffi::c_int'}, {'name': 'cid_work', 'type': 'callback_head'}, {'name': 'tlb_ubc', 'type': 'tlbflush_unmap_batch'}, {'name': 'splice_pipe', 'type': '*mut pipe_inode_info'}, {'name': 'task_frag', 'type': 'page_frag'}, {'name': 'delays', 'type': '*mut task_delay_info'}, {'name': 'nr_dirtied', 'type': 'ffi::c_int'}, {'name': 'nr_dirtied_pause', 'type': 'ffi::c_int'}, {'name': 'dirty_paused_when', 'type': 'ffi::c_ulong'}, {'name': 'timer_slack_ns', 'type': 'u64_'}, {'name': 'default_timer_slack_ns', 'type': 'u64_'}, {'name': 'trace_recursion', 'type': 'ffi::c_ulong'}, {'name': 'throttle_disk', 'type': '*mut gendisk'}, {'name': 'utask', 'type': '*mut uprobe_task'}, {'name': 'kmap_ctrl', 'type': 'kmap_ctrl'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'rcu_users', 'type': 'refcount_t'}, {'name': 'pagefault_disabled', 'type': 'ffi::c_int'}, {'name': 'oom_reaper_list', 'type': '*mut task_struct'}, {'name': 'oom_reaper_timer', 'type': 'timer_list'}, {'name': 'stack_vm_area', 'type': '*mut vm_struct'}, {'name': 'stack_refcount', 'type': 'refcount_t'}, {'name': 'security', 'type': '*mut ffi::c_void'}, {'name': 'bpf_net_context', 'type': '*mut bpf_net_context'}, {'name': 'mce_vaddr', 'type': '*mut ffi::c_void'}, {'name': 'mce_kflags', 'type': '__u64'}, {'name': 'mce_addr', 'type': 'u64_'}, {'name': '_bitfield_align_2', 'type': '[u64; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 8usize]>'}, {'name': 'mce_kill_me', 'type': 'callback_head'}, {'name': 'mce_count', 'type': 'ffi::c_int'}, {'name': 'kretprobe_instances', 'type': 'llist_head'}, {'name': 'rethooks', 'type': 'llist_head'}, {'name': 'l1d_flush_kill', 'type': 'callback_head'}, {'name': 'thread', 'type': 'thread_struct'}]`

### Rust Evidence

- Graph edges: `15`

## W-000001 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: __auxiliary_device_add
- Explanation: __auxiliary_device_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000002 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: __auxiliary_driver_register
- Explanation: __auxiliary_driver_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000040 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: auxiliary_device_init
- Explanation: auxiliary_device_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000071 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: config_group_init
- Explanation: config_group_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000082 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: configfs_register_subsystem
- Explanation: configfs_register_subsystem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000121 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: cpufreq_get
- Explanation: cpufreq_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000177 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: dma_buf_attach
- Explanation: dma_buf_attach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000213 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: dma_fence_signal
- Explanation: dma_fence_signal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000291 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: drm_gem_mmap
- Explanation: drm_gem_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000365 SignatureDrift

- Risk: High
- Score: 11.4
- Symbol: drm_release
- Explanation: drm_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `4`

## W-000046 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: auxiliary_set_drvdata
- Explanation: auxiliary_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000087 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: configfs_unregister_subsystem
- Explanation: configfs_unregister_subsystem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000248 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: drm_compat_ioctl
- Explanation: drm_compat_ioctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000351 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: drm_poll
- Explanation: drm_poll changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000364 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: drm_read
- Explanation: drm_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000367 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: drm_send_event
- Explanation: drm_send_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000423 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: invalid
- Explanation: invalid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-000469 SignatureDrift

- Risk: High
- Score: 11.2
- Symbol: rt_mutex_lock
- Explanation: rt_mutex_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `3`

## W-001100 SleepabilityDrift

- Risk: High
- Score: 11.2
- Symbol: clk_prepare
- Explanation: clk_prepare has MAY_SLEEP C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['MAY_SLEEP']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/clk.h:330 `might_sleep();`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:188 `Clk::prepare` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:183 `/// [`clk_prepare`]: https://docs.kernel.org/core-api/kernel-api.html#c.clk_prepare`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:186 `// SAFETY: By the type invariants, self.as_raw() is a valid argument for`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:191 `/// Unprepare the clock.`

## W-001102 SleepabilityDrift

- Risk: High
- Score: 11.2
- Symbol: clk_unprepare
- Explanation: clk_unprepare has MAY_SLEEP C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['MAY_SLEEP']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/clk.h:362 `might_sleep();`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:200 `Clk::unprepare` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:195 `/// [`clk_unprepare`]: https://docs.kernel.org/core-api/kernel-api.html#c.clk_unprepare`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:198 `// SAFETY: By the type invariants, self.as_raw() is a valid argument for`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:203 `/// Prepare and enable the clock.`

## W-000024 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __round_jiffies
- Explanation: __round_jiffies changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `2`

## W-000027 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: __skb_checksum
- Explanation: __skb_checksum changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `2`

## W-000049 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: bio_add_vmalloc
- Explanation: bio_add_vmalloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000073 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: config_item_get
- Explanation: config_item_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000076 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: config_item_put
- Explanation: config_item_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000078 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: configfs_depend_item
- Explanation: configfs_depend_item changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000100 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: cpufreq_cpu_get_raw
- Explanation: cpufreq_cpu_get_raw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000126 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: cpufreq_quick_get
- Explanation: cpufreq_quick_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000182 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: dma_buf_export
- Explanation: dma_buf_export changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000187 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: dma_buf_map_attachment
- Explanation: dma_buf_map_attachment changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000193 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: dma_buf_unmap_attachment
- Explanation: dma_buf_unmap_attachment changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000196 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: dma_buf_vmap
- Explanation: dma_buf_vmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000198 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: dma_buf_vunmap
- Explanation: dma_buf_vunmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000215 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: dma_fence_signal_timestamp
- Explanation: dma_fence_signal_timestamp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000235 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: dma_resv_iter_first
- Explanation: dma_resv_iter_first changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000237 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: dma_resv_iter_next
- Explanation: dma_resv_iter_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000262 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_event_reserve_init
- Explanation: drm_event_reserve_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000281 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_gem_lock
- Explanation: drm_gem_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000284 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_gem_lru_move_tail
- Explanation: drm_gem_lru_move_tail changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000305 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_gem_prime_import
- Explanation: drm_gem_prime_import changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000311 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_gem_unlock
- Explanation: drm_gem_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000342 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_modeset_lock_all
- Explanation: drm_modeset_lock_all changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000346 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_modeset_unlock
- Explanation: drm_modeset_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000372 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: drm_vma_node_allow
- Explanation: drm_vma_node_allow changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000393 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: extra
- Explanation: extra changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000425 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: iterate_supers
- Explanation: iterate_supers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut super_block, arg2: *mut ffi::c_void), >'}, {'name': 'arg2', 'type': '*mut ffi::c_void'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'f', 'type': '::core::option::Option< unsafe extern "C" fn(arg1: *mut super_block, arg2: *mut ffi::c_void), >'}, {'name': 'arg', 'type': '*mut ffi::c_void'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `2`

## W-000439 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: offset
- Explanation: offset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000440 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: parse_int_array
- Explanation: parse_int_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000447 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: pfnmap_track
- Explanation: pfnmap_track changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000477 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: scm_recv
- Explanation: scm_recv changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000500 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: stack_depot_save
- Explanation: stack_depot_save changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000535 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: ww_mutex_lock
- Explanation: ww_mutex_lock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `2`

## W-000570 FieldDrift

- Risk: High
- Score: 11.0
- Symbol: queue_limits
- Explanation: queue_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`
- New: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

### Rust Evidence

- Graph edges: `12`

## W-001076 SignatureDrift

- Risk: High
- Score: 11.0
- Symbol: iterate_supers
- Explanation: iterate_supers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['void (*)(struct super_block *, void *)', 'void *'], 'return_type': 'extern void'}`
- New: `{'params': ['void (*f)(struct super_block *, void *)', 'void *arg'], 'return_type': 'extern void'}`

### Rust Evidence

- Graph edges: `2`

## W-001096 ErrorDrift

- Risk: High
- Score: 11.0
- Symbol: clk_get_optional
- Explanation: clk_get_optional has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN', 'NULL_RETURN', 'REFCOUNT_GET']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/clk.h:1209 `if (clk == ERR_PTR(-ENOENT))`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:318 `OptionalClk::get` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:313 `// SAFETY: It is safe to call [`clk_get_optional`] for a valid device pointer.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:317 `ERR_PTR_MAPPING`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/clk.rs:318 `LIFETIME_NAMING_PATTERN`

## W-001114 ErrorDrift

- Risk: High
- Score: 11.0
- Symbol: dev_pm_opp_get_sharing_cpus
- Explanation: dev_pm_opp_get_sharing_cpus has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/pm_opp.h:449 `return -EINVAL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:768 `Table::sharing_cpus` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:763 `/// Gets sharing CPUs.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:766 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:768 `TO_RESULT_MAPPING`

## W-001115 ErrorDrift

- Risk: High
- Score: 11.0
- Symbol: dev_pm_opp_init_cpufreq_table
- Explanation: dev_pm_opp_init_cpufreq_table has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE']`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/include/linux/pm_opp.h:473 `return -EINVAL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:45 `FreqTable::new` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:42 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:44 `TO_RESULT_MAPPING`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.16/rust/kernel/opp.rs:45 `LIFETIME_NAMING_PATTERN`

## W-000003 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __bpf_dynptr_write
- Explanation: __bpf_dynptr_write changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000004 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __cpufreq_driver_target
- Explanation: __cpufreq_driver_target changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000007 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __dev_pm_qos_flags
- Explanation: __dev_pm_qos_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000008 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __dev_pm_qos_resume_latency
- Explanation: __dev_pm_qos_resume_latency changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000009 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __devm_auxiliary_device_create
- Explanation: __devm_auxiliary_device_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000010 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __devm_drm_dev_alloc
- Explanation: __devm_drm_dev_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000012 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __drm_dev_dbg
- Explanation: __drm_dev_dbg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000013 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __drm_err
- Explanation: __drm_err changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000014 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __drm_mm_interval_first
- Explanation: __drm_mm_interval_first changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000015 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __drm_printfn_coredump
- Explanation: __drm_printfn_coredump changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000016 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __drm_printfn_dbg
- Explanation: __drm_printfn_dbg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000017 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __drm_printfn_err
- Explanation: __drm_printfn_err changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000018 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __drm_printfn_info
- Explanation: __drm_printfn_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000019 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __drm_printfn_line
- Explanation: __drm_printfn_line changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000020 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __drm_printfn_seq_file
- Explanation: __drm_printfn_seq_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000021 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __drm_puts_coredump
- Explanation: __drm_puts_coredump changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000022 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __drm_puts_seq_file
- Explanation: __drm_puts_seq_file changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000023 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __percpu_down_read
- Explanation: __percpu_down_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut percpu_rw_semaphore'}, {'name': 'arg2', 'type': 'bool_'}], 'return_type': 'bool_'}`
- New: `{'params': [{'name': 'arg1', 'type': '*mut percpu_rw_semaphore'}, {'name': 'arg2', 'type': 'bool_'}, {'name': 'arg3', 'type': 'bool_'}], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000025 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __round_jiffies_up
- Explanation: __round_jiffies_up changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000026 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __rt_mutex_init
- Explanation: __rt_mutex_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000028 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __skb_try_recv_from_queue
- Explanation: __skb_try_recv_from_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'sk', 'type': '*mut sock'}, {'name': 'queue', 'type': '*mut sk_buff_head'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'off', 'type': '*mut ffi::c_int'}, {'name': 'err', 'type': '*mut ffi::c_int'}, {'name': 'last', 'type': '*mut *mut sk_buff'}], 'return_type': '*mut sk_buff'}`
- New: `{'params': [{'name': 'queue', 'type': '*mut sk_buff_head'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'off', 'type': '*mut ffi::c_int'}, {'name': 'err', 'type': '*mut ffi::c_int'}, {'name': 'last', 'type': '*mut *mut sk_buff'}], 'return_type': '*mut sk_buff'}`

### Rust Evidence

- Graph edges: `1`

## W-000029 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __stack_depot_get_stack_record
- Explanation: __stack_depot_get_stack_record changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000030 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: __zerocopy_sg_from_iter
- Explanation: __zerocopy_sg_from_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'msg', 'type': '*mut msghdr'}, {'name': 'sk', 'type': '*mut sock'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'from', 'type': '*mut iov_iter'}, {'name': 'length', 'type': 'usize'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'msg', 'type': '*mut msghdr'}, {'name': 'sk', 'type': '*mut sock'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'from', 'type': '*mut iov_iter'}, {'name': 'length', 'type': 'usize'}, {'name': 'binding', 'type': '*mut net_devmem_dmabuf_binding'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000031 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: _find_first_andnot_bit
- Explanation: _find_first_andnot_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000032 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: alloc_pages_nolock_noprof
- Explanation: alloc_pages_nolock_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000033 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: anon_inode_make_secure_inode
- Explanation: anon_inode_make_secure_inode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000035 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_cpu_rescan_dead_smt_siblings
- Explanation: arch_cpu_rescan_dead_smt_siblings changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000036 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: arch_freq_get_on_cpu
- Explanation: arch_freq_get_on_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000037 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: auxiliary_device_create
- Explanation: auxiliary_device_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000039 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: auxiliary_device_destroy
- Explanation: auxiliary_device_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000041 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: auxiliary_device_sysfs_irq_add
- Explanation: auxiliary_device_sysfs_irq_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000042 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: auxiliary_device_sysfs_irq_remove
- Explanation: auxiliary_device_sysfs_irq_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000047 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bdev_rw_virt
- Explanation: bdev_rw_virt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000048 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_add_virt_nofail
- Explanation: bio_add_virt_nofail changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000050 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bio_add_vmalloc_chunk
- Explanation: bio_add_vmalloc_chunk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000051 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_rq_map_kern
- Explanation: blk_rq_map_kern changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'arg1', 'type': '*mut request_queue'}, {'name': 'arg2', 'type': '*mut request'}, {'name': 'arg3', 'type': '*mut ffi::c_void'}, {'name': 'arg4', 'type': 'ffi::c_uint'}, {'name': 'arg5', 'type': 'gfp_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'rq', 'type': '*mut request'}, {'name': 'kbuf', 'type': '*mut ffi::c_void'}, {'name': 'len', 'type': 'ffi::c_uint'}, {'name': 'gfp', 'type': 'gfp_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000052 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: bpf_dynptr_slice_rdwr
- Explanation: bpf_dynptr_slice_rdwr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000053 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: btf_ctx_arg_idx
- Explanation: btf_ctx_arg_idx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000068 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: collect_paths
- Explanation: collect_paths changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000069 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: compat_vma_mmap_prepare
- Explanation: compat_vma_mmap_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000070 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: config_group_find_item
- Explanation: config_group_find_item changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000074 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: config_item_get_unless_zero
- Explanation: config_item_get_unless_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000075 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: config_item_init_type_name
- Explanation: config_item_init_type_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000077 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: config_item_set_name
- Explanation: config_item_set_name changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000079 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: configfs_depend_item_unlocked
- Explanation: configfs_depend_item_unlocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000080 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: configfs_register_default_group
- Explanation: configfs_register_default_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000081 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: configfs_register_group
- Explanation: configfs_register_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000083 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: configfs_remove_default_groups
- Explanation: configfs_remove_default_groups changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000084 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: configfs_undepend_item
- Explanation: configfs_undepend_item changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000085 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: configfs_unregister_default_group
- Explanation: configfs_unregister_default_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000086 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: configfs_unregister_group
- Explanation: configfs_unregister_group changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000088 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: copy_folio_from_iter_atomic
- Explanation: copy_folio_from_iter_atomic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000090 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_latency_qos_add_request
- Explanation: cpu_latency_qos_add_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000091 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_latency_qos_limit
- Explanation: cpu_latency_qos_limit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000092 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_latency_qos_remove_request
- Explanation: cpu_latency_qos_remove_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000093 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_latency_qos_request_active
- Explanation: cpu_latency_qos_request_active changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000094 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_latency_qos_update_request
- Explanation: cpu_latency_qos_update_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000095 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_old_microcode
- Explanation: cpu_show_old_microcode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000096 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpu_show_tsa
- Explanation: cpu_show_tsa changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000097 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_boost_enabled
- Explanation: cpufreq_boost_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000098 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_boost_set_sw
- Explanation: cpufreq_boost_set_sw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000102 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_default_governor
- Explanation: cpufreq_default_governor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000103 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_disable_fast_switch
- Explanation: cpufreq_disable_fast_switch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000104 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_driver_adjust_perf
- Explanation: cpufreq_driver_adjust_perf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000105 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_driver_fast_switch
- Explanation: cpufreq_driver_fast_switch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000106 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_driver_has_adjust_perf
- Explanation: cpufreq_driver_has_adjust_perf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000107 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_driver_resolve_freq
- Explanation: cpufreq_driver_resolve_freq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000108 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_driver_target
- Explanation: cpufreq_driver_target changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000109 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_driver_test_flags
- Explanation: cpufreq_driver_test_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000110 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_enable_fast_switch
- Explanation: cpufreq_enable_fast_switch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000111 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_fallback_governor
- Explanation: cpufreq_fallback_governor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000112 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_freq_transition_begin
- Explanation: cpufreq_freq_transition_begin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000113 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_freq_transition_end
- Explanation: cpufreq_freq_transition_end changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000114 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_frequency_table_cpuinfo
- Explanation: cpufreq_frequency_table_cpuinfo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000115 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_frequency_table_get_index
- Explanation: cpufreq_frequency_table_get_index changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000116 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_frequency_table_verify
- Explanation: cpufreq_frequency_table_verify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000119 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_generic_init
- Explanation: cpufreq_generic_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000122 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_get_current_driver
- Explanation: cpufreq_get_current_driver changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000123 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_get_driver_data
- Explanation: cpufreq_get_driver_data changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000124 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_get_hw_max_freq
- Explanation: cpufreq_get_hw_max_freq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000125 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_policy_transition_delay_us
- Explanation: cpufreq_policy_transition_delay_us changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000127 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_quick_get_max
- Explanation: cpufreq_quick_get_max changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000128 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_ready_for_eas
- Explanation: cpufreq_ready_for_eas changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000131 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_register_governor
- Explanation: cpufreq_register_governor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000132 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_register_notifier
- Explanation: cpufreq_register_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000133 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_resume
- Explanation: cpufreq_resume changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000134 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_show_cpus
- Explanation: cpufreq_show_cpus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000135 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_start_governor
- Explanation: cpufreq_start_governor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000136 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_stop_governor
- Explanation: cpufreq_stop_governor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000137 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_supports_freq_invariance
- Explanation: cpufreq_supports_freq_invariance changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000138 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_suspend
- Explanation: cpufreq_suspend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000139 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_table_index_unsorted
- Explanation: cpufreq_table_index_unsorted changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000140 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_table_validate_and_sort
- Explanation: cpufreq_table_validate_and_sort changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000142 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_unregister_governor
- Explanation: cpufreq_unregister_governor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000143 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_unregister_notifier
- Explanation: cpufreq_unregister_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000144 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_update_limits
- Explanation: cpufreq_update_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000145 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: cpufreq_update_policy
- Explanation: cpufreq_update_policy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000149 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: css_rstat_flush
- Explanation: css_rstat_flush changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000150 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: css_rstat_updated
- Explanation: css_rstat_updated changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000154 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_add_ancestor_request
- Explanation: dev_pm_qos_add_ancestor_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000155 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_add_notifier
- Explanation: dev_pm_qos_add_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000156 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_add_request
- Explanation: dev_pm_qos_add_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000157 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_constraints_destroy
- Explanation: dev_pm_qos_constraints_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000158 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_constraints_init
- Explanation: dev_pm_qos_constraints_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000159 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_expose_flags
- Explanation: dev_pm_qos_expose_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000160 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_expose_latency_limit
- Explanation: dev_pm_qos_expose_latency_limit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000161 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_expose_latency_tolerance
- Explanation: dev_pm_qos_expose_latency_tolerance changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000162 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_flags
- Explanation: dev_pm_qos_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000163 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_get_user_latency_tolerance
- Explanation: dev_pm_qos_get_user_latency_tolerance changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000164 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_hide_flags
- Explanation: dev_pm_qos_hide_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000165 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_hide_latency_limit
- Explanation: dev_pm_qos_hide_latency_limit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000166 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_hide_latency_tolerance
- Explanation: dev_pm_qos_hide_latency_tolerance changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000167 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_read_value
- Explanation: dev_pm_qos_read_value changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000168 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_remove_notifier
- Explanation: dev_pm_qos_remove_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000169 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_remove_request
- Explanation: dev_pm_qos_remove_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000170 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_update_flags
- Explanation: dev_pm_qos_update_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000171 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_update_request
- Explanation: dev_pm_qos_update_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000172 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dev_pm_qos_update_user_latency_tolerance
- Explanation: dev_pm_qos_update_user_latency_tolerance changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000175 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: devm_is_action_added
- Explanation: devm_is_action_added changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000176 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: disable_cpufreq
- Explanation: disable_cpufreq changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000178 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_begin_cpu_access
- Explanation: dma_buf_begin_cpu_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000179 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_detach
- Explanation: dma_buf_detach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000180 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_dynamic_attach
- Explanation: dma_buf_dynamic_attach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000181 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_end_cpu_access
- Explanation: dma_buf_end_cpu_access changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000183 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_fd
- Explanation: dma_buf_fd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000184 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_get
- Explanation: dma_buf_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000185 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_iter_begin
- Explanation: dma_buf_iter_begin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000186 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_iter_next
- Explanation: dma_buf_iter_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000188 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_map_attachment_unlocked
- Explanation: dma_buf_map_attachment_unlocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000189 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_mmap
- Explanation: dma_buf_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000190 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_move_notify
- Explanation: dma_buf_move_notify changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000191 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_pin
- Explanation: dma_buf_pin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000192 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_put
- Explanation: dma_buf_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000194 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_unmap_attachment_unlocked
- Explanation: dma_buf_unmap_attachment_unlocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000195 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_unpin
- Explanation: dma_buf_unpin changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000197 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_vmap_unlocked
- Explanation: dma_buf_vmap_unlocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000199 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_buf_vunmap_unlocked
- Explanation: dma_buf_vunmap_unlocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000200 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_add_callback
- Explanation: dma_fence_add_callback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000201 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_allocate_private_stub
- Explanation: dma_fence_allocate_private_stub changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000202 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_context_alloc
- Explanation: dma_fence_context_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000203 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_default_wait
- Explanation: dma_fence_default_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000204 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_describe
- Explanation: dma_fence_describe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000205 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_enable_sw_signaling
- Explanation: dma_fence_enable_sw_signaling changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000206 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_free
- Explanation: dma_fence_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000207 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_get_status
- Explanation: dma_fence_get_status changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000208 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_get_stub
- Explanation: dma_fence_get_stub changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000209 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_init
- Explanation: dma_fence_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000210 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_release
- Explanation: dma_fence_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000211 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_remove_callback
- Explanation: dma_fence_remove_callback changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000212 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_set_deadline
- Explanation: dma_fence_set_deadline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000214 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_signal_locked
- Explanation: dma_fence_signal_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000216 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_signal_timestamp_locked
- Explanation: dma_fence_signal_timestamp_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000217 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_wait_any_timeout
- Explanation: dma_fence_wait_any_timeout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000218 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_fence_wait_timeout
- Explanation: dma_fence_wait_timeout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000219 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_iova_destroy
- Explanation: dma_iova_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000220 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_iova_free
- Explanation: dma_iova_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000221 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_iova_link
- Explanation: dma_iova_link changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000222 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_iova_sync
- Explanation: dma_iova_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000223 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_iova_try_alloc
- Explanation: dma_iova_try_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000224 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_iova_unlink
- Explanation: dma_iova_unlink changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000225 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_need_unmap
- Explanation: dma_need_unmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000226 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_pool_create
- Explanation: dma_pool_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `1`

## W-000227 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_pool_create_node
- Explanation: dma_pool_create_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000228 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_resv_add_fence
- Explanation: dma_resv_add_fence changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000229 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_resv_copy_fences
- Explanation: dma_resv_copy_fences changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000230 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_resv_describe
- Explanation: dma_resv_describe changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000231 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_resv_fini
- Explanation: dma_resv_fini changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000232 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_resv_get_fences
- Explanation: dma_resv_get_fences changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000233 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_resv_get_singleton
- Explanation: dma_resv_get_singleton changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000234 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_resv_init
- Explanation: dma_resv_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000236 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_resv_iter_first_unlocked
- Explanation: dma_resv_iter_first_unlocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000238 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_resv_iter_next_unlocked
- Explanation: dma_resv_iter_next_unlocked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000239 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_resv_replace_fences
- Explanation: dma_resv_replace_fences changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000240 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_resv_reserve_fences
- Explanation: dma_resv_reserve_fences changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000241 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_resv_set_deadline
- Explanation: dma_resv_set_deadline changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000242 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_resv_test_signaled
- Explanation: dma_resv_test_signaled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000243 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: dma_resv_wait_timeout
- Explanation: dma_resv_wait_timeout changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000244 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_set_pmd
- Explanation: do_set_pmd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'vmf', 'type': '*mut vm_fault'}, {'name': 'page', 'type': '*mut page'}], 'return_type': 'vm_fault_t'}`
- New: `{'params': [{'name': 'vmf', 'type': '*mut vm_fault'}, {'name': 'folio', 'type': '*mut folio'}, {'name': 'page', 'type': '*mut page'}], 'return_type': 'vm_fault_t'}`

### Rust Evidence

- Graph edges: `1`

## W-000245 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_trace_rdpmc
- Explanation: do_trace_rdpmc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'msr', 'type': 'ffi::c_uint'}, {'name': 'val', 'type': 'u64_'}, {'name': 'failed', 'type': 'ffi::c_int'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'msr', 'type': 'u32_'}, {'name': 'val', 'type': 'u64_'}, {'name': 'failed', 'type': 'ffi::c_int'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000246 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_trace_read_msr
- Explanation: do_trace_read_msr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'msr', 'type': 'ffi::c_uint'}, {'name': 'val', 'type': 'u64_'}, {'name': 'failed', 'type': 'ffi::c_int'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'msr', 'type': 'u32_'}, {'name': 'val', 'type': 'u64_'}, {'name': 'failed', 'type': 'ffi::c_int'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000247 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: do_trace_write_msr
- Explanation: do_trace_write_msr changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'msr', 'type': 'ffi::c_uint'}, {'name': 'val', 'type': 'u64_'}, {'name': 'failed', 'type': 'ffi::c_int'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'msr', 'type': 'u32_'}, {'name': 'val', 'type': 'u64_'}, {'name': 'failed', 'type': 'ffi::c_int'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000249 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_debugfs_dev_init
- Explanation: drm_debugfs_dev_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000250 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_dev_alloc
- Explanation: drm_dev_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000251 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_dev_enter
- Explanation: drm_dev_enter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000252 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_dev_exit
- Explanation: drm_dev_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000254 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_dev_printk
- Explanation: drm_dev_printk changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000257 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_dev_set_dma_dev
- Explanation: drm_dev_set_dma_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000258 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_dev_unplug
- Explanation: drm_dev_unplug changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000260 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_dev_wedged_event
- Explanation: drm_dev_wedged_event changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000261 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_event_cancel_free
- Explanation: drm_event_cancel_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000263 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_event_reserve_init_locked
- Explanation: drm_event_reserve_init_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000264 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_fdinfo_print_size
- Explanation: drm_fdinfo_print_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000265 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_file_err
- Explanation: drm_file_err changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000266 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_file_update_pid
- Explanation: drm_file_update_pid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000268 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_create_mmap_offset_size
- Explanation: drm_gem_create_mmap_offset_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000269 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_dma_resv_wait
- Explanation: drm_gem_dma_resv_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000270 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_dmabuf_export
- Explanation: drm_gem_dmabuf_export changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000271 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_dmabuf_mmap
- Explanation: drm_gem_dmabuf_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000272 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_dmabuf_release
- Explanation: drm_gem_dmabuf_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000273 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_dmabuf_vmap
- Explanation: drm_gem_dmabuf_vmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000274 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_dmabuf_vunmap
- Explanation: drm_gem_dmabuf_vunmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000275 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_dumb_map_offset
- Explanation: drm_gem_dumb_map_offset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000276 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_evict_locked
- Explanation: drm_gem_evict_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000277 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_free_mmap_offset
- Explanation: drm_gem_free_mmap_offset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000278 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_get_pages
- Explanation: drm_gem_get_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000280 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_handle_delete
- Explanation: drm_gem_handle_delete changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000282 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_lock_reservations
- Explanation: drm_gem_lock_reservations changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000283 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_lru_init
- Explanation: drm_gem_lru_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000285 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_lru_move_tail_locked
- Explanation: drm_gem_lru_move_tail_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000286 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_lru_remove
- Explanation: drm_gem_lru_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000287 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_lru_scan
- Explanation: drm_gem_lru_scan changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000288 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_map_attach
- Explanation: drm_gem_map_attach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000289 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_map_detach
- Explanation: drm_gem_map_detach changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000290 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_map_dma_buf
- Explanation: drm_gem_map_dma_buf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000292 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_mmap_obj
- Explanation: drm_gem_mmap_obj changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000293 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_object_free
- Explanation: drm_gem_object_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000296 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_object_init_with_mnt
- Explanation: drm_gem_object_init_with_mnt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000300 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_objects_lookup
- Explanation: drm_gem_objects_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000301 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_prime_export
- Explanation: drm_gem_prime_export changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000302 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_prime_fd_to_handle
- Explanation: drm_gem_prime_fd_to_handle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000303 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_prime_handle_to_dmabuf
- Explanation: drm_gem_prime_handle_to_dmabuf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000304 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_prime_handle_to_fd
- Explanation: drm_gem_prime_handle_to_fd changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000306 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_prime_import_dev
- Explanation: drm_gem_prime_import_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000307 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_prime_mmap
- Explanation: drm_gem_prime_mmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000308 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_private_object_fini
- Explanation: drm_gem_private_object_fini changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000309 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_private_object_init
- Explanation: drm_gem_private_object_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000310 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_put_pages
- Explanation: drm_gem_put_pages changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000312 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_unlock_reservations
- Explanation: drm_gem_unlock_reservations changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000313 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_unmap_dma_buf
- Explanation: drm_gem_unmap_dma_buf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000314 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_vm_close
- Explanation: drm_gem_vm_close changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000315 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_vm_open
- Explanation: drm_gem_vm_open changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000316 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_vmap
- Explanation: drm_gem_vmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000317 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_gem_vunmap
- Explanation: drm_gem_vunmap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000318 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_invalid_op
- Explanation: drm_invalid_op changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000321 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_ioctl_kernel
- Explanation: drm_ioctl_kernel changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000322 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_memory_stats_is_zero
- Explanation: drm_memory_stats_is_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000323 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_minor_acquire
- Explanation: drm_minor_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000324 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_minor_release
- Explanation: drm_minor_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000325 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_mm_init
- Explanation: drm_mm_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000326 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_mm_insert_node_in_range
- Explanation: drm_mm_insert_node_in_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000327 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_mm_print
- Explanation: drm_mm_print changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000328 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_mm_remove_node
- Explanation: drm_mm_remove_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000329 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_mm_reserve_node
- Explanation: drm_mm_reserve_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000330 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_mm_scan_add_block
- Explanation: drm_mm_scan_add_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000331 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_mm_scan_color_evict
- Explanation: drm_mm_scan_color_evict changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000332 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_mm_scan_init_with_range
- Explanation: drm_mm_scan_init_with_range changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000333 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_mm_scan_remove_block
- Explanation: drm_mm_scan_remove_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000334 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_mm_takedown
- Explanation: drm_mm_takedown changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000335 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_mode_config_cleanup
- Explanation: drm_mode_config_cleanup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000336 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_mode_config_reset
- Explanation: drm_mode_config_reset changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000337 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_modeset_acquire_fini
- Explanation: drm_modeset_acquire_fini changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000338 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_modeset_acquire_init
- Explanation: drm_modeset_acquire_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000339 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_modeset_backoff
- Explanation: drm_modeset_backoff changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000340 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_modeset_drop_locks
- Explanation: drm_modeset_drop_locks changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000343 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_modeset_lock_all_ctx
- Explanation: drm_modeset_lock_all_ctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000344 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_modeset_lock_init
- Explanation: drm_modeset_lock_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000345 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_modeset_lock_single_interruptible
- Explanation: drm_modeset_lock_single_interruptible changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000347 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_modeset_unlock_all
- Explanation: drm_modeset_unlock_all changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000348 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_noop
- Explanation: drm_noop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000352 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_prime_gem_destroy
- Explanation: drm_prime_gem_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000353 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_prime_get_contiguous_size
- Explanation: drm_prime_get_contiguous_size changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000354 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_prime_pages_to_sg
- Explanation: drm_prime_pages_to_sg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000355 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_prime_sg_to_dma_addr_array
- Explanation: drm_prime_sg_to_dma_addr_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000356 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_prime_sg_to_page_array
- Explanation: drm_prime_sg_to_page_array changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000357 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_print_bits
- Explanation: drm_print_bits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000358 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_print_hex_dump
- Explanation: drm_print_hex_dump changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000359 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_print_memory_stats
- Explanation: drm_print_memory_stats changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000360 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_print_regset32
- Explanation: drm_print_regset32 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000361 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_printf
- Explanation: drm_printf changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000362 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_put_dev
- Explanation: drm_put_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000363 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_puts
- Explanation: drm_puts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000366 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_release_noglobal
- Explanation: drm_release_noglobal changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000368 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_send_event_locked
- Explanation: drm_send_event_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000369 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_send_event_timestamp_locked
- Explanation: drm_send_event_timestamp_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000370 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_show_fdinfo
- Explanation: drm_show_fdinfo changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000371 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_show_memory_stats
- Explanation: drm_show_memory_stats changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000373 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_vma_node_allow_once
- Explanation: drm_vma_node_allow_once changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000374 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_vma_node_is_allowed
- Explanation: drm_vma_node_is_allowed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000376 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_vma_node_revoke
- Explanation: drm_vma_node_revoke changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000377 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_vma_offset_add
- Explanation: drm_vma_offset_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000378 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_vma_offset_lookup_locked
- Explanation: drm_vma_offset_lookup_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000379 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_vma_offset_manager_destroy
- Explanation: drm_vma_offset_manager_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000380 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_vma_offset_manager_init
- Explanation: drm_vma_offset_manager_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000381 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_vma_offset_remove
- Explanation: drm_vma_offset_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000382 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drm_warn_on_modeset_not_all_locked
- Explanation: drm_warn_on_modeset_not_all_locked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000383 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drmm_cgroup_register_region
- Explanation: drmm_cgroup_register_region changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000384 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drmm_mode_config_init
- Explanation: drmm_mode_config_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000386 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: drop_collected_paths
- Explanation: drop_collected_paths changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000387 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_mmsv_event_handle
- Explanation: ethtool_mmsv_event_handle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000388 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_mmsv_get_mm
- Explanation: ethtool_mmsv_get_mm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000389 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_mmsv_init
- Explanation: ethtool_mmsv_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000390 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_mmsv_link_state_handle
- Explanation: ethtool_mmsv_link_state_handle changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000391 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_mmsv_set_mm
- Explanation: ethtool_mmsv_set_mm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000392 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ethtool_mmsv_stop
- Explanation: ethtool_mmsv_stop changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000394 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filesystems_freeze
- Explanation: filesystems_freeze changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000395 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: filesystems_thaw
- Explanation: filesystems_thaw changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000396 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fpstate_clear_xstate_component
- Explanation: fpstate_clear_xstate_component changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'fps', 'type': '*mut fpstate'}, {'name': 'xfeature', 'type': 'ffi::c_uint'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'fpstate', 'type': '*mut fpstate'}, {'name': 'xfeature', 'type': 'ffi::c_uint'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000397 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freeze_super
- Explanation: freeze_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'super_', 'type': '*mut super_block'}, {'name': 'who', 'type': 'freeze_holder'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'super_', 'type': '*mut super_block'}, {'name': 'who', 'type': 'freeze_holder'}, {'name': 'freeze_owner', 'type': '*const ffi::c_void'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000398 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freq_constraints_init
- Explanation: freq_constraints_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000399 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freq_qos_add_notifier
- Explanation: freq_qos_add_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000400 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freq_qos_add_request
- Explanation: freq_qos_add_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000401 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freq_qos_apply
- Explanation: freq_qos_apply changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000402 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freq_qos_read_value
- Explanation: freq_qos_read_value changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000403 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freq_qos_remove_notifier
- Explanation: freq_qos_remove_notifier changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000404 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freq_qos_remove_request
- Explanation: freq_qos_remove_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000405 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freq_qos_update_request
- Explanation: freq_qos_update_request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000406 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_get_child_node_count
- Explanation: fwnode_get_child_node_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000407 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_get_named_child_node_count
- Explanation: fwnode_get_named_child_node_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000408 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_fill_statx_atomic_writes
- Explanation: generic_fill_statx_atomic_writes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'stat', 'type': '*mut kstat'}, {'name': 'unit_min', 'type': 'ffi::c_uint'}, {'name': 'unit_max', 'type': 'ffi::c_uint'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'stat', 'type': '*mut kstat'}, {'name': 'unit_min', 'type': 'ffi::c_uint'}, {'name': 'unit_max', 'type': 'ffi::c_uint'}, {'name': 'unit_max_opt', 'type': 'ffi::c_uint'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000409 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: genphy_match_phy_device
- Explanation: genphy_match_phy_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000410 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_cpu_idle_time
- Explanation: get_cpu_idle_time changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000411 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_governor_parent_kobj
- Explanation: get_governor_parent_kobj changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000412 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_netmem
- Explanation: get_netmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000413 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gov_attr_set_get
- Explanation: gov_attr_set_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000414 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gov_attr_set_init
- Explanation: gov_attr_set_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000415 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: gov_attr_set_put
- Explanation: gov_attr_set_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000416 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: has_target_index
- Explanation: has_target_index changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000417 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: have_governor_per_policy
- Explanation: have_governor_per_policy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000418 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: in_nf_duplicate
- Explanation: in_nf_duplicate changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000419 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: inet_proto_csum_replace_by_diff
- Explanation: inet_proto_csum_replace_by_diff changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'sum', 'type': '*mut __sum16'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'diff', 'type': '__wsum'}, {'name': 'pseudohdr', 'type': 'bool_'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'sum', 'type': '*mut __sum16'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'diff', 'type': '__wsum'}, {'name': 'pseudohdr', 'type': 'bool_'}, {'name': 'ipv6', 'type': 'bool_'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000436 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mock_drm_getfile
- Explanation: mock_drm_getfile changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000437 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: msg_zerocopy_realloc
- Explanation: msg_zerocopy_realloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'sk', 'type': '*mut sock'}, {'name': 'size', 'type': 'usize'}, {'name': 'uarg', 'type': '*mut ubuf_info'}], 'return_type': '*mut ubuf_info'}`
- New: `{'params': [{'name': 'sk', 'type': '*mut sock'}, {'name': 'size', 'type': 'usize'}, {'name': 'uarg', 'type': '*mut ubuf_info'}, {'name': 'devmem', 'type': 'bool_'}], 'return_type': '*mut ubuf_info'}`

### Rust Evidence

- Graph edges: `1`

## W-000442 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_hp_ignore_link_change
- Explanation: pci_hp_ignore_link_change changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000443 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_hp_unignore_link_change
- Explanation: pci_hp_unignore_link_change changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000444 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_msi_enabled
- Explanation: pci_msi_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'ffi::c_int'}`
- New: `{'params': [], 'return_type': 'bool_'}`

### Rust Evidence

- Graph edges: `1`

## W-000446 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pfnmap_setup_cachemode
- Explanation: pfnmap_setup_cachemode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000448 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pfnmap_untrack
- Explanation: pfnmap_untrack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000449 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_get_mac_termination
- Explanation: phy_get_mac_termination changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000450 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pidfd_prepare
- Explanation: pidfd_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'pid', 'type': '*mut pid'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'ret', 'type': '*mut *mut file'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'pid', 'type': '*mut pid'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'ret_file', 'type': '*mut *mut file'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000451 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: plist_add
- Explanation: plist_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000452 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: plist_del
- Explanation: plist_del changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000453 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: plist_requeue
- Explanation: plist_requeue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000454 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_qos_read_value
- Explanation: pm_qos_read_value changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000455 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_qos_update_flags
- Explanation: pm_qos_update_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000456 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pm_qos_update_target
- Explanation: pm_qos_update_target changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000458 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pool_index_plus_1
- Explanation: pool_index_plus_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000459 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: put_netmem
- Explanation: put_netmem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000463 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rdmsrq_on_cpu
- Explanation: rdmsrq_on_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000464 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rdmsrq_safe_on_cpu
- Explanation: rdmsrq_safe_on_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000465 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: refresh_frequency_limits
- Explanation: refresh_frequency_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000466 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_refined_jiffies
- Explanation: register_refined_jiffies changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'clock_tick_rate', 'type': 'ffi::c_long'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'clock_tick_rate', 'type': 'ffi::c_long'}], 'return_type': '()'}`

### Rust Evidence

- Graph edges: `1`

## W-000468 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rt_mutex_base_init
- Explanation: rt_mutex_base_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000470 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rt_mutex_lock_interruptible
- Explanation: rt_mutex_lock_interruptible changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000471 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rt_mutex_lock_killable
- Explanation: rt_mutex_lock_killable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000472 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rt_mutex_trylock
- Explanation: rt_mutex_trylock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000473 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: rt_mutex_unlock
- Explanation: rt_mutex_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000476 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sched_update_asym_prefer_cpu
- Explanation: sched_update_asym_prefer_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000478 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: scm_recv_unix
- Explanation: scm_recv_unix changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000479 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sem_last_holder
- Explanation: sem_last_holder changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000480 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_orig_insn
- Explanation: set_orig_insn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'aup', 'type': '*mut arch_uprobe'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'vaddr', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'aup', 'type': '*mut arch_uprobe'}, {'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'vaddr', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000481 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: set_swbp
- Explanation: set_swbp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'aup', 'type': '*mut arch_uprobe'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'vaddr', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'aup', 'type': '*mut arch_uprobe'}, {'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'vaddr', 'type': 'ffi::c_ulong'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000483 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_copy_and_crc32c_datagram_iter
- Explanation: skb_copy_and_crc32c_datagram_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000485 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_crc32c
- Explanation: skb_crc32c changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000486 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_send_sock_locked_with_flags
- Explanation: skb_send_sock_locked_with_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000487 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: skb_zerocopy_iter_stream
- Explanation: skb_zerocopy_iter_stream changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'sk', 'type': '*mut sock'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'msg', 'type': '*mut msghdr'}, {'name': 'len', 'type': 'ffi::c_int'}, {'name': 'uarg', 'type': '*mut ubuf_info'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'sk', 'type': '*mut sock'}, {'name': 'skb', 'type': '*mut sk_buff'}, {'name': 'msg', 'type': '*mut msghdr'}, {'name': 'len', 'type': 'ffi::c_int'}, {'name': 'uarg', 'type': '*mut ubuf_info'}, {'name': 'binding', 'type': '*mut net_devmem_dmabuf_binding'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000488 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: smp_text_poke_batch_add
- Explanation: smp_text_poke_batch_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000489 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: smp_text_poke_batch_finish
- Explanation: smp_text_poke_batch_finish changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000490 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: smp_text_poke_int3_handler
- Explanation: smp_text_poke_int3_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000491 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: smp_text_poke_single
- Explanation: smp_text_poke_single changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000492 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: smp_text_poke_sync_each_cpu
- Explanation: smp_text_poke_sync_each_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000493 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_early_init
- Explanation: stack_depot_early_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000494 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_fetch
- Explanation: stack_depot_fetch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000495 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_get_extra_bits
- Explanation: stack_depot_get_extra_bits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000496 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_init
- Explanation: stack_depot_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000497 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_print
- Explanation: stack_depot_print changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000498 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_put
- Explanation: stack_depot_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000499 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_request_early_init
- Explanation: stack_depot_request_early_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000501 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_save_flags
- Explanation: stack_depot_save_flags changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000502 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_set_extra_bits
- Explanation: stack_depot_set_extra_bits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000503 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: stack_depot_snprint
- Explanation: stack_depot_snprint changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000504 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: sugov_is_governor
- Explanation: sugov_is_governor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000505 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: text_poke_apply_relocation
- Explanation: text_poke_apply_relocation changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000510 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: thaw_super
- Explanation: thaw_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'super_', 'type': '*mut super_block'}, {'name': 'who', 'type': 'freeze_holder'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'super_', 'type': '*mut super_block'}, {'name': 'who', 'type': 'freeze_holder'}, {'name': 'freeze_owner', 'type': '*const ffi::c_void'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000511 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: timer_delete_sync_try
- Explanation: timer_delete_sync_try changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000512 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: timer_init_key
- Explanation: timer_init_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000513 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: timers_init
- Explanation: timers_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000522 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: uprobe_write_opcode
- Explanation: uprobe_write_opcode changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': 'auprobe', 'type': '*mut arch_uprobe'}, {'name': 'mm', 'type': '*mut mm_struct'}, {'name': 'vaddr', 'type': 'ffi::c_ulong'}, {'name': 'arg1', 'type': 'uprobe_opcode_t'}], 'return_type': 'ffi::c_int'}`
- New: `{'params': [{'name': 'auprobe', 'type': '*mut arch_uprobe'}, {'name': 'vma', 'type': '*mut vm_area_struct'}, {'name': 'vaddr', 'type': 'ffi::c_ulong'}, {'name': 'arg1', 'type': 'uprobe_opcode_t'}], 'return_type': 'ffi::c_int'}`

### Rust Evidence

- Graph edges: `1`

## W-000524 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: video_firmware_drivers_only
- Explanation: video_firmware_drivers_only changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000533 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wrmsrq_on_cpu
- Explanation: wrmsrq_on_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000534 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: wrmsrq_safe_on_cpu
- Explanation: wrmsrq_safe_on_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000536 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ww_mutex_lock_interruptible
- Explanation: ww_mutex_lock_interruptible changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000537 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ww_mutex_trylock
- Explanation: ww_mutex_trylock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000538 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: ww_mutex_unlock
- Explanation: ww_mutex_unlock changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-000539 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: x86_task_fpu
- Explanation: x86_task_fpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Rust Evidence

- Graph edges: `1`

## W-001042 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: blk_rq_map_kern
- Explanation: blk_rq_map_kern changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct request_queue *', 'struct request *', 'void *', 'unsigned int', 'gfp_t'], 'return_type': 'int'}`
- New: `{'params': ['struct request *rq', 'void *kbuf', 'unsigned int len', 'gfp_t gfp'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-001067 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: freeze_super
- Explanation: freeze_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *super', 'enum freeze_holder who'], 'return_type': 'int'}`
- New: `{'params': ['struct super_block *super', 'enum freeze_holder who', 'const void *freeze_owner'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-001068 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_get_phy_id
- Explanation: fwnode_get_phy_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct fwnode_handle *fwnode', 'u32 *phy_id'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct fwnode_handle *fwnode', 'u32 *phy_id'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-001069 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_get_phy_node
- Explanation: fwnode_get_phy_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct fwnode_handle *fwnode'], 'return_type': 'static inline struct fwnode_handle *'}`
- New: `{'params': ['const struct fwnode_handle *fwnode'], 'return_type': 'struct fwnode_handle *'}`

### Rust Evidence

- Graph edges: `1`

## W-001070 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_mdio_find_device
- Explanation: fwnode_mdio_find_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct fwnode_handle *fwnode'], 'return_type': 'static inline struct mdio_device *'}`
- New: `{'params': ['struct fwnode_handle *fwnode'], 'return_type': 'struct mdio_device *'}`

### Rust Evidence

- Graph edges: `1`

## W-001071 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: fwnode_phy_find_device
- Explanation: fwnode_phy_find_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct fwnode_handle *phy_fwnode'], 'return_type': 'static inline struct phy_device *'}`
- New: `{'params': ['struct fwnode_handle *phy_fwnode'], 'return_type': 'struct phy_device *'}`

### Rust Evidence

- Graph edges: `1`

## W-001072 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: generic_fill_statx_atomic_writes
- Explanation: generic_fill_statx_atomic_writes changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct kstat *stat', 'unsigned int unit_min', 'unsigned int unit_max'], 'return_type': 'void'}`
- New: `{'params': ['struct kstat *stat', 'unsigned int unit_min', 'unsigned int unit_max', 'unsigned int unit_max_opt'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001073 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: get_phy_device
- Explanation: get_phy_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct mii_bus *bus', 'int addr', 'bool is_c45'], 'return_type': 'static inline struct phy_device *'}`
- New: `{'params': ['struct mii_bus *bus', 'int addr', 'bool is_c45'], 'return_type': 'struct phy_device *'}`

### Rust Evidence

- Graph edges: `1`

## W-001077 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: mdiobus_register_board_info
- Explanation: mdiobus_register_board_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct mdio_board_info *i', 'unsigned int n'], 'return_type': 'static inline int'}`
- New: `{'params': ['const struct mdio_board_info *info', 'unsigned int n'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-001078 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: pci_msi_enabled
- Explanation: pci_msi_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [], 'return_type': 'static inline int'}`
- New: `{'params': [], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `1`

## W-001079 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_device_free
- Explanation: phy_device_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct phy_device *phydev'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct phy_device *phydev'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `1`

## W-001080 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: phy_device_register
- Explanation: phy_device_register changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct phy_device *phy'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct phy_device *phy'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-001084 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: register_refined_jiffies
- Explanation: register_refined_jiffies changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['long clock_tick_rate'], 'return_type': 'extern int'}`
- New: `{'params': ['long clock_tick_rate'], 'return_type': 'extern void'}`

### Rust Evidence

- Graph edges: `1`

## W-001089 SignatureDrift

- Risk: High
- Score: 10.8
- Symbol: thaw_super
- Explanation: thaw_super changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct super_block *super', 'enum freeze_holder who'], 'return_type': 'int'}`
- New: `{'params': ['struct super_block *super', 'enum freeze_holder who', 'const void *freeze_owner'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `1`

## W-001065 SignatureDrift

- Risk: High
- Score: 10.6
- Symbol: drmm_kms_helper_poll_init
- Explanation: drmm_kms_helper_poll_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_device *dev'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_device *dev'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-000560 FieldDrift

- Risk: High
- Score: 10.0
- Symbol: kstat
- Explanation: kstat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'result_mask', 'type': 'u32_'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'nlink', 'type': 'ffi::c_uint'}, {'name': 'blksize', 'type': 'u32'}, {'name': 'attributes', 'type': 'u64_'}, {'name': 'attributes_mask', 'type': 'u64_'}, {'name': 'ino', 'type': 'u64_'}, {'name': 'dev', 'type': 'dev_t'}, {'name': 'rdev', 'type': 'dev_t'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'gid', 'type': 'kgid_t'}, {'name': 'size', 'type': 'loff_t'}, {'name': 'atime', 'type': 'timespec64'}, {'name': 'mtime', 'type': 'timespec64'}, {'name': 'ctime', 'type': 'timespec64'}, {'name': 'btime', 'type': 'timespec64'}, {'name': 'blocks', 'type': 'u64_'}, {'name': 'mnt_id', 'type': 'u64_'}, {'name': 'change_cookie', 'type': 'u64_'}, {'name': 'subvol', 'type': 'u64_'}, {'name': 'dio_mem_align', 'type': 'u32_'}, {'name': 'dio_offset_align', 'type': 'u32_'}, {'name': 'dio_read_offset_align', 'type': 'u32_'}, {'name': 'atomic_write_unit_min', 'type': 'u32_'}, {'name': 'atomic_write_unit_max', 'type': 'u32_'}, {'name': 'atomic_write_segments_max', 'type': 'u32_'}]`
- New: `[{'name': 'result_mask', 'type': 'u32_'}, {'name': 'mode', 'type': 'umode_t'}, {'name': 'nlink', 'type': 'ffi::c_uint'}, {'name': 'blksize', 'type': 'u32'}, {'name': 'attributes', 'type': 'u64_'}, {'name': 'attributes_mask', 'type': 'u64_'}, {'name': 'ino', 'type': 'u64_'}, {'name': 'dev', 'type': 'dev_t'}, {'name': 'rdev', 'type': 'dev_t'}, {'name': 'uid', 'type': 'kuid_t'}, {'name': 'gid', 'type': 'kgid_t'}, {'name': 'size', 'type': 'loff_t'}, {'name': 'atime', 'type': 'timespec64'}, {'name': 'mtime', 'type': 'timespec64'}, {'name': 'ctime', 'type': 'timespec64'}, {'name': 'btime', 'type': 'timespec64'}, {'name': 'blocks', 'type': 'u64_'}, {'name': 'mnt_id', 'type': 'u64_'}, {'name': 'change_cookie', 'type': 'u64_'}, {'name': 'subvol', 'type': 'u64_'}, {'name': 'dio_mem_align', 'type': 'u32_'}, {'name': 'dio_offset_align', 'type': 'u32_'}, {'name': 'dio_read_offset_align', 'type': 'u32_'}, {'name': 'atomic_write_unit_min', 'type': 'u32_'}, {'name': 'atomic_write_unit_max', 'type': 'u32_'}, {'name': 'atomic_write_unit_max_opt', 'type': 'u32_'}, {'name': 'atomic_write_segments_max', 'type': 'u32_'}]`

### Rust Evidence

- Graph edges: `7`

## W-000564 FieldDrift

- Risk: Medium
- Score: 9.8
- Symbol: net_iov
- Explanation: net_iov changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '__unused_padding', 'type': 'ffi::c_ulong'}, {'name': 'pp_magic', 'type': 'ffi::c_ulong'}, {'name': 'pp', 'type': '*mut page_pool'}, {'name': 'owner', 'type': '*mut net_iov_area'}, {'name': 'dma_addr', 'type': 'ffi::c_ulong'}, {'name': 'pp_ref_count', 'type': 'atomic_long_t'}]`
- New: `[{'name': 'type_', 'type': 'net_iov_type'}, {'name': 'pp_magic', 'type': 'ffi::c_ulong'}, {'name': 'pp', 'type': '*mut page_pool'}, {'name': 'owner', 'type': '*mut net_iov_area'}, {'name': 'dma_addr', 'type': 'ffi::c_ulong'}, {'name': 'pp_ref_count', 'type': 'atomic_long_t'}]`

### Rust Evidence

- Graph edges: `6`

## W-000034 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: apply_relocation
- Explanation: apply_relocation changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000054 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: cgroup_rstat_flush
- Explanation: cgroup_rstat_flush changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000055 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: cgroup_rstat_updated
- Explanation: cgroup_rstat_updated changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000067 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: collect_mounts
- Explanation: collect_mounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000089 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: copy_page_from_iter_atomic
- Explanation: copy_page_from_iter_atomic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000151 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: d_hash_and_lookup
- Explanation: d_hash_and_lookup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000173 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: device_get_child_node_count
- Explanation: device_get_child_node_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000174 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: device_phy_find_device
- Explanation: device_phy_find_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000385 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drop_collected_mounts
- Explanation: drop_collected_mounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000421 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: init_timer_key
- Explanation: init_timer_key changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000422 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: init_timers
- Explanation: init_timers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000424 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: iterate_mounts
- Explanation: iterate_mounts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000426 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: llist_add_batch
- Explanation: llist_add_batch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000427 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mdio_bus_exit
- Explanation: mdio_bus_exit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000428 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: mdio_bus_init
- Explanation: mdio_bus_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000441 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pci_fixup_cardbus
- Explanation: pci_fixup_cardbus changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000445 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: pcim_iounmap_regions
- Explanation: pcim_iounmap_regions changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000457 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: poke_int3_handler
- Explanation: poke_int3_handler changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000461 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: rdmsrl_on_cpu
- Explanation: rdmsrl_on_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000462 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: rdmsrl_safe_on_cpu
- Explanation: rdmsrl_safe_on_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000467 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: relocate_vma_down
- Explanation: relocate_vma_down changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000474 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sched_dynamic_klp_disable
- Explanation: sched_dynamic_klp_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000475 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sched_dynamic_klp_enable
- Explanation: sched_dynamic_klp_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000482 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sg_next
- Explanation: sg_next changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000484 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: skb_copy_and_hash_datagram_iter
- Explanation: skb_copy_and_hash_datagram_iter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000506 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: text_poke_bp
- Explanation: text_poke_bp changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000507 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: text_poke_finish
- Explanation: text_poke_finish changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000508 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: text_poke_queue
- Explanation: text_poke_queue changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000509 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: text_poke_sync
- Explanation: text_poke_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000514 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: track_pfn_copy
- Explanation: track_pfn_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000515 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: track_pfn_insert
- Explanation: track_pfn_insert changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000516 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: track_pfn_remap
- Explanation: track_pfn_remap changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000517 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: try_alloc_pages_noprof
- Explanation: try_alloc_pages_noprof changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000518 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: try_to_del_timer_sync
- Explanation: try_to_del_timer_sync changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000519 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: untrack_pfn
- Explanation: untrack_pfn changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000520 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: untrack_pfn_clear
- Explanation: untrack_pfn_clear changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000521 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: untrack_pfn_copy
- Explanation: untrack_pfn_copy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000523 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: vfs_submount
- Explanation: vfs_submount changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000527 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: wakeup_source_add
- Explanation: wakeup_source_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000528 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: wakeup_source_create
- Explanation: wakeup_source_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000529 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: wakeup_source_destroy
- Explanation: wakeup_source_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000530 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: wakeup_source_remove
- Explanation: wakeup_source_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000531 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: wrmsrl_on_cpu
- Explanation: wrmsrl_on_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000532 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: wrmsrl_safe_on_cpu
- Explanation: wrmsrl_safe_on_cpu changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Rust Evidence

- Graph edges: `0`

## W-000559 FieldDrift

- Risk: Medium
- Score: 9.6
- Symbol: kiocb
- Explanation: kiocb changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'ki_filp', 'type': '*mut file'}, {'name': 'ki_pos', 'type': 'loff_t'}, {'name': 'private', 'type': '*mut ffi::c_void'}, {'name': 'ki_flags', 'type': 'ffi::c_int'}, {'name': 'ki_ioprio', 'type': 'u16_'}, {'name': '__bindgen_anon_1', 'type': 'kiocb__bindgen_ty_1'}]`
- New: `[{'name': 'ki_filp', 'type': '*mut file'}, {'name': 'ki_pos', 'type': 'loff_t'}, {'name': 'private', 'type': '*mut ffi::c_void'}, {'name': 'ki_flags', 'type': 'ffi::c_int'}, {'name': 'ki_ioprio', 'type': 'u16_'}, {'name': 'ki_write_stream', 'type': 'u8_'}, {'name': '__bindgen_anon_1', 'type': 'kiocb__bindgen_ty_1'}]`

### Rust Evidence

- Graph edges: `5`

## W-001034 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: IS_ENABLED
- Explanation: IS_ENABLED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['CONFIG_BLK_DEV_ZONED) && (q->limits.features & BLK_FEAT_ZONED'], 'return_type': 'return'}`
- New: `{'params': ['CONFIG_XARRAY_MULTI) && xa_is_internal(entry) && (entry < xa_mk_sibling(XA_CHUNK_SIZE - 1)'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001036 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __blake2b_init
- Explanation: __blake2b_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct blake2b_state *state', 'size_t outlen', 'const void *key', 'size_t keylen'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct blake2b_state *state', 'size_t outlen', 'size_t keylen'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001037 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __crypto_acomp_tfm
- Explanation: __crypto_acomp_tfm changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct crypto_tfm *tfm'], 'return_type': 'static inline struct crypto_acomp *'}`
- New: `{'params': ['crypto_acomp_tfm(tfm)->fb'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001038 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __crypto_ahash_cast
- Explanation: __crypto_ahash_cast changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct crypto_tfm *tfm'], 'return_type': 'static inline struct crypto_ahash *'}`
- New: `{'params': ['crypto_ahash_tfm(tfm)->fb'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001039 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: __ffs
- Explanation: __ffs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['b[0]'], 'return_type': 'return'}`
- New: `{'params': ['data'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001040 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: acomp_request_on_stack_init
- Explanation: acomp_request_on_stack_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['char *buf', 'struct crypto_acomp *tfm', 'gfp_t gfp', 'bool stackonly'], 'return_type': 'static inline struct acomp_req *'}`
- New: `{'params': ['char *buf', 'struct crypto_acomp *tfm'], 'return_type': 'static inline struct acomp_req *'}`

### Rust Evidence

- Graph edges: `0`

## W-001041 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: ahash_request_free
- Explanation: ahash_request_free changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct ahash_request *req'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct ahash_request *req'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001043 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: chacha20_block
- Explanation: chacha20_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u32 *state', 'u8 *stream'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct chacha_state *state', 'u8 out[CHACHA_BLOCK_SIZE]'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001044 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: chacha20_crypt
- Explanation: chacha20_crypt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u32 *state', 'u8 *dst', 'const u8 *src', 'unsigned int bytes'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct chacha_state *state', 'u8 *dst', 'const u8 *src', 'unsigned int bytes'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001045 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: chacha_block_generic
- Explanation: chacha_block_generic changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u32 *state', 'u8 *stream', 'int nrounds'], 'return_type': 'void'}`
- New: `{'params': ['struct chacha_state *state', 'u8 out[CHACHA_BLOCK_SIZE]', 'int nrounds'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001046 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: chacha_crypt
- Explanation: chacha_crypt changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u32 *state', 'u8 *dst', 'const u8 *src', 'unsigned int bytes', 'int nrounds'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct chacha_state *state', 'u8 *dst', 'const u8 *src', 'unsigned int bytes', 'int nrounds'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001047 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: chacha_crypt_arch
- Explanation: chacha_crypt_arch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u32 *state', 'u8 *dst', 'const u8 *src', 'unsigned int bytes', 'int nrounds'], 'return_type': 'void'}`
- New: `{'params': ['struct chacha_state *state', 'u8 *dst', 'const u8 *src', 'unsigned int bytes', 'int nrounds'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001048 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: chacha_init
- Explanation: chacha_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u32 *state', 'const u32 *key', 'const u8 *iv'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct chacha_state *state', 'const u32 key[CHACHA_KEY_WORDS]', 'const u8 iv[CHACHA_IV_SIZE]'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001049 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: chacha_init_consts
- Explanation: chacha_init_consts changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u32 *state'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct chacha_state *state'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001050 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: cpumask_any_and_but
- Explanation: cpumask_any_and_but changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct cpumask *mask1', 'const struct cpumask *mask2', 'unsigned int cpu'], 'return_type': 'static __always_inline unsigned int'}`
- New: `{'params': ['const struct cpumask *mask1', 'const struct cpumask *mask2', 'int cpu'], 'return_type': 'static __always_inline unsigned int'}`

### Rust Evidence

- Graph edges: `0`

## W-001051 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: cpumask_any_but
- Explanation: cpumask_any_but changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct cpumask *mask', 'unsigned int cpu'], 'return_type': 'static __always_inline unsigned int'}`
- New: `{'params': ['const struct cpumask *mask', 'int cpu'], 'return_type': 'static __always_inline unsigned int'}`

### Rust Evidence

- Graph edges: `0`

## W-001052 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_ahash_final
- Explanation: crypto_ahash_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct ahash_request *req'], 'return_type': 'int'}`
- New: `{'params': ['struct ahash_request *req'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-001053 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_ahash_finup
- Explanation: crypto_ahash_finup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct ahash_request *req'], 'return_type': 'int'}`
- New: `{'params': ['req'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001054 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_shash_final
- Explanation: crypto_shash_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct shash_desc *desc', 'u8 *out'], 'return_type': 'int'}`
- New: `{'params': ['struct shash_desc *desc', 'u8 *out'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-001055 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_shash_finup
- Explanation: crypto_shash_finup changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct shash_desc *desc', 'const u8 *data', 'unsigned int len', 'u8 *out'], 'return_type': 'int'}`
- New: `{'params': ['desc', 'NULL', '0', 'out'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001056 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_shash_init
- Explanation: crypto_shash_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct shash_desc *desc'], 'return_type': 'static inline int'}`
- New: `{'params': ['struct shash_desc *desc'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001057 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: crypto_shash_update
- Explanation: crypto_shash_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct shash_desc *desc', 'const u8 *data', 'unsigned int len'], 'return_type': 'int'}`
- New: `{'params': ['struct shash_desc *desc', 'const u8 *data', 'unsigned int len'], 'return_type': 'static inline int'}`

### Rust Evidence

- Graph edges: `0`

## W-001058 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: device_get_child_node_count
- Explanation: device_get_child_node_count changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const struct device *dev'], 'return_type': 'unsigned int'}`
- New: `{'params': ['const struct device *dev'], 'return_type': 'static inline unsigned int'}`

### Rust Evidence

- Graph edges: `0`

## W-001059 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_add_modes_noedid
- Explanation: drm_add_modes_noedid changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_connector *connector', 'int hdisplay', 'int vdisplay'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_connector *connector', 'unsigned int hdisplay', 'unsigned int vdisplay'], 'return_type': 'int'}`

### Rust Evidence

- Graph edges: `0`

## W-001060 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_panel_disable
- Explanation: drm_panel_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_panel *panel'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_panel *panel'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001061 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_panel_enable
- Explanation: drm_panel_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_panel *panel'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_panel *panel'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001062 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_panel_prepare
- Explanation: drm_panel_prepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_panel *panel'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_panel *panel'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001063 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_panel_unprepare
- Explanation: drm_panel_unprepare changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_panel *panel'], 'return_type': 'int'}`
- New: `{'params': ['struct drm_panel *panel'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001064 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: drm_priv_to_bridge_state
- Explanation: drm_priv_to_bridge_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct drm_private_state *priv'], 'return_type': 'static inline struct drm_bridge_state *'}`
- New: `{'params': ['bridge->base.state'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001066 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: find_next_bit
- Explanation: find_next_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['cpumask_bits(srcp)', 'small_cpumask_bits', 'n + 1'], 'return_type': 'return'}`
- New: `{'params': ['addr', 'XA_CHUNK_SIZE', 'offset'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001074 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hchacha_block
- Explanation: hchacha_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u32 *state', 'u32 *out', 'int nrounds'], 'return_type': 'static inline void'}`
- New: `{'params': ['const struct chacha_state *state', 'u32 out[HCHACHA_OUT_WORDS]', 'int nrounds'], 'return_type': 'static inline void'}`

### Rust Evidence

- Graph edges: `0`

## W-001075 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: hchacha_block_arch
- Explanation: hchacha_block_arch changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u32 *state', 'u32 *out', 'int nrounds'], 'return_type': 'void'}`
- New: `{'params': ['const struct chacha_state *state', 'u32 out[HCHACHA_OUT_WORDS]', 'int nrounds'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001081 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: poly1305_final
- Explanation: poly1305_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct poly1305_desc_ctx *desc', 'u8 *digest'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct poly1305_desc_ctx *desc', 'u8 *digest'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001082 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: poly1305_init
- Explanation: poly1305_init changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct poly1305_desc_ctx *desc', 'const u8 *key'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct poly1305_desc_ctx *desc', 'const u8 key[POLY1305_KEY_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001083 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: poly1305_update
- Explanation: poly1305_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct poly1305_desc_ctx *desc', 'const u8 *src', 'unsigned int nbytes'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct poly1305_desc_ctx *desc', 'const u8 *src', 'unsigned int nbytes'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001085 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sha224_final
- Explanation: sha224_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sha256_state *sctx', 'u8 *out'], 'return_type': 'void'}`
- New: `{'params': ['struct sha256_state *sctx', 'u8 out[SHA224_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001086 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sha256
- Explanation: sha256 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['const u8 *data', 'unsigned int len', 'u8 *out'], 'return_type': 'void'}`
- New: `{'params': ['const u8 *data', 'size_t len', 'u8 out[SHA256_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001087 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sha256_final
- Explanation: sha256_final changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sha256_state *sctx', 'u8 *out'], 'return_type': 'void'}`
- New: `{'params': ['struct sha256_state *sctx', 'u8 out[SHA256_DIGEST_SIZE]'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001088 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: sha256_update
- Explanation: sha256_update changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct sha256_state *sctx', 'const u8 *data', 'unsigned int len'], 'return_type': 'void'}`
- New: `{'params': ['struct sha256_state *sctx', 'const u8 *data', 'size_t len'], 'return_type': 'void'}`

### Rust Evidence

- Graph edges: `0`

## W-001090 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: unlikely
- Explanation: unlikely changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['tif_need_resched()'], 'return_type': 'return'}`
- New: `{'params': ['entry == XA_RETRY_ENTRY'], 'return_type': 'return'}`

### Rust Evidence

- Graph edges: `0`

## W-001091 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: void
- Explanation: void changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['*poll_queue_proc)(struct file *, wait_queue_head_t *, struct poll_table_struct *'], 'return_type': 'typedef'}`
- New: `{'params': ['*xa_update_node_t)(struct xa_node *node'], 'return_type': 'typedef'}`

### Rust Evidence

- Graph edges: `0`

## W-001092 SignatureDrift

- Risk: Medium
- Score: 9.6
- Symbol: xa_marked
- Explanation: xa_marked changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['&mapping->i_pages', 'tag'], 'return_type': 'return'}`
- New: `{'params': ['const struct xarray *xa', 'xa_mark_t mark'], 'return_type': 'static inline bool'}`

### Rust Evidence

- Graph edges: `0`

## W-000565 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: netlink_ext_ack
- Explanation: netlink_ext_ack changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_msg', 'type': '*const ffi::c_char'}, {'name': 'bad_attr', 'type': '*const nlattr'}, {'name': 'policy', 'type': '*mut nla_policy'}, {'name': 'miss_nest', 'type': '*const nlattr'}, {'name': 'miss_type', 'type': 'u16_'}, {'name': 'cookie', 'type': '[u8_; 20usize]'}, {'name': 'cookie_len', 'type': 'u8_'}, {'name': '_msg_buf', 'type': '[ffi::c_char; 80usize]'}]`
- New: `[{'name': '_msg', 'type': '*const ffi::c_char'}, {'name': 'bad_attr', 'type': '*const nlattr'}, {'name': 'policy', 'type': '*mut nla_policy'}, {'name': 'miss_nest', 'type': '*const nlattr'}, {'name': 'miss_type', 'type': 'u16_'}, {'name': 'cookie', 'type': '[u8_; 8usize]'}, {'name': 'cookie_len', 'type': 'u8_'}, {'name': '_msg_buf', 'type': '[ffi::c_char; 80usize]'}]`

### Rust Evidence

- Graph edges: `2`

## W-000545 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: address_space_operations
- Explanation: address_space_operations changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'writepage', 'type': '::core::option::Option<'}, {'name': 'read_folio', 'type': '::core::option::Option<'}, {'name': 'writepages', 'type': '::core::option::Option<'}, {'name': 'dirty_folio', 'type': '::core::option::Option<'}, {'name': 'readahead', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut readahead_control)>'}, {'name': 'write_begin', 'type': '::core::option::Option<'}, {'name': 'write_end', 'type': '::core::option::Option<'}, {'name': 'bmap', 'type': '::core::option::Option<'}, {'name': 'free_folio', 'type': '::core::option::Option<unsafe extern "C" fn(folio: *mut folio)>'}, {'name': 'direct_IO', 'type': '::core::option::Option<'}, {'name': 'migrate_folio', 'type': '::core::option::Option<'}, {'name': 'launder_folio', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut folio) -> ffi::c_int>'}, {'name': 'is_partially_uptodate', 'type': '::core::option::Option<'}, {'name': 'is_dirty_writeback', 'type': '::core::option::Option<'}, {'name': 'error_remove_folio', 'type': '::core::option::Option<'}, {'name': 'swap_activate', 'type': '::core::option::Option<'}, {'name': 'swap_deactivate', 'type': '::core::option::Option<unsafe extern "C" fn(file: *mut file)>'}, {'name': 'swap_rw', 'type': '::core::option::Option<'}]`
- New: `[{'name': 'read_folio', 'type': '::core::option::Option<'}, {'name': 'writepages', 'type': '::core::option::Option<'}, {'name': 'dirty_folio', 'type': '::core::option::Option<'}, {'name': 'readahead', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut readahead_control)>'}, {'name': 'write_begin', 'type': '::core::option::Option<'}, {'name': 'write_end', 'type': '::core::option::Option<'}, {'name': 'bmap', 'type': '::core::option::Option<'}, {'name': 'free_folio', 'type': '::core::option::Option<unsafe extern "C" fn(folio: *mut folio)>'}, {'name': 'direct_IO', 'type': '::core::option::Option<'}, {'name': 'migrate_folio', 'type': '::core::option::Option<'}, {'name': 'launder_folio', 'type': '::core::option::Option<unsafe extern "C" fn(arg1: *mut folio) -> ffi::c_int>'}, {'name': 'is_partially_uptodate', 'type': '::core::option::Option<'}, {'name': 'is_dirty_writeback', 'type': '::core::option::Option<'}, {'name': 'error_remove_folio', 'type': '::core::option::Option<'}, {'name': 'swap_activate', 'type': '::core::option::Option<'}, {'name': 'swap_deactivate', 'type': '::core::option::Option<unsafe extern "C" fn(file: *mut file)>'}, {'name': 'swap_rw', 'type': '::core::option::Option<'}]`

### Rust Evidence

- Graph edges: `1`

## W-000548 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: bpf_link_info__bindgen_ty_1__bindgen_ty_11__bindgen_ty_1__bindgen_ty_1
- Explanation: bpf_link_info__bindgen_ty_1__bindgen_ty_11__bindgen_ty_1__bindgen_ty_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'file_name', 'type': '__u64'}, {'name': 'name_len', 'type': '__u32'}, {'name': 'offset', 'type': '__u32'}, {'name': 'cookie', 'type': '__u64'}]`
- New: `[{'name': 'file_name', 'type': '__u64'}, {'name': 'name_len', 'type': '__u32'}, {'name': 'offset', 'type': '__u32'}, {'name': 'cookie', 'type': '__u64'}, {'name': 'ref_ctr_offset', 'type': '__u64'}]`

### Rust Evidence

- Graph edges: `1`

## W-000551 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: cgroup_subsys_state
- Explanation: cgroup_subsys_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cgroup', 'type': '*mut cgroup'}, {'name': 'ss', 'type': '*mut cgroup_subsys'}, {'name': 'refcnt', 'type': 'percpu_ref'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'children', 'type': 'list_head'}, {'name': 'rstat_css_node', 'type': 'list_head'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'serial_nr', 'type': 'u64_'}, {'name': 'online_cnt', 'type': 'atomic_t'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 'destroy_rwork', 'type': 'rcu_work'}, {'name': 'parent', 'type': '*mut cgroup_subsys_state'}, {'name': 'nr_descendants', 'type': 'ffi::c_int'}]`
- New: `[{'name': 'cgroup', 'type': '*mut cgroup'}, {'name': 'ss', 'type': '*mut cgroup_subsys'}, {'name': 'refcnt', 'type': 'percpu_ref'}, {'name': 'rstat_cpu', 'type': '*mut css_rstat_cpu'}, {'name': 'sibling', 'type': 'list_head'}, {'name': 'children', 'type': 'list_head'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'serial_nr', 'type': 'u64_'}, {'name': 'online_cnt', 'type': 'atomic_t'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 'destroy_rwork', 'type': 'rcu_work'}, {'name': 'parent', 'type': '*mut cgroup_subsys_state'}, {'name': 'nr_descendants', 'type': 'ffi::c_int'}, {'name': 'rstat_flush_next', 'type': '*mut cgroup_subsys_state'}]`

### Rust Evidence

- Graph edges: `1`

## W-000554 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: device_node
- Explanation: device_node changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'phandle', 'type': 'phandle'}, {'name': 'full_name', 'type': '*const ffi::c_char'}, {'name': 'fwnode', 'type': 'fwnode_handle'}, {'name': 'properties', 'type': '*mut property'}, {'name': 'deadprops', 'type': '*mut property'}, {'name': 'parent', 'type': '*mut device_node'}, {'name': 'child', 'type': '*mut device_node'}, {'name': 'sibling', 'type': '*mut device_node'}, {'name': '_flags', 'type': 'ffi::c_ulong'}, {'name': 'data', 'type': '*mut ffi::c_void'}]`

### Rust Evidence

- Graph edges: `1`

## W-000555 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: dir_context
- Explanation: dir_context changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'actor', 'type': 'filldir_t'}, {'name': 'pos', 'type': 'loff_t'}]`
- New: `[{'name': 'actor', 'type': 'filldir_t'}, {'name': 'pos', 'type': 'loff_t'}, {'name': 'count', 'type': 'ffi::c_int'}]`

### Rust Evidence

- Graph edges: `1`

## W-000556 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: fpu_guest
- Explanation: fpu_guest changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'xfeatures', 'type': 'u64_'}, {'name': 'perm', 'type': 'u64_'}, {'name': 'xfd_err', 'type': 'u64_'}, {'name': 'uabi_size', 'type': 'ffi::c_uint'}, {'name': 'fpstate', 'type': '*mut fpstate'}]`
- New: `[{'name': 'xfeatures', 'type': 'u64_'}, {'name': 'xfd_err', 'type': 'u64_'}, {'name': 'uabi_size', 'type': 'ffi::c_uint'}, {'name': 'fpstate', 'type': '*mut fpstate'}]`

### Rust Evidence

- Graph edges: `1`

## W-000558 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: kernel_ethtool_ts_info
- Explanation: kernel_ethtool_ts_info changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'cmd', 'type': 'u32_'}, {'name': 'so_timestamping', 'type': 'u32_'}, {'name': 'phc_index', 'type': 'ffi::c_int'}, {'name': 'phc_qualifier', 'type': 'hwtstamp_provider_qualifier'}, {'name': 'tx_types', 'type': 'hwtstamp_tx_types'}, {'name': 'rx_filters', 'type': 'hwtstamp_rx_filters'}]`
- New: `[{'name': 'cmd', 'type': 'u32_'}, {'name': 'so_timestamping', 'type': 'u32_'}, {'name': 'phc_index', 'type': 'ffi::c_int'}, {'name': 'phc_qualifier', 'type': 'hwtstamp_provider_qualifier'}, {'name': 'phc_source', 'type': 'hwtstamp_source'}, {'name': 'phc_phyindex', 'type': 'ffi::c_int'}, {'name': 'tx_types', 'type': 'hwtstamp_tx_types'}, {'name': 'rx_filters', 'type': 'hwtstamp_rx_filters'}]`

### Rust Evidence

- Graph edges: `1`

## W-000561 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ma_wr_state
- Explanation: ma_wr_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'mas', 'type': '*mut ma_state'}, {'name': 'node', 'type': '*mut maple_node'}, {'name': 'r_min', 'type': 'ffi::c_ulong'}, {'name': 'r_max', 'type': 'ffi::c_ulong'}, {'name': 'type_', 'type': 'maple_type'}, {'name': 'offset_end', 'type': 'ffi::c_uchar'}, {'name': 'pivots', 'type': '*mut ffi::c_ulong'}, {'name': 'end_piv', 'type': 'ffi::c_ulong'}, {'name': 'slots', 'type': '*mut *mut ffi::c_void'}, {'name': 'entry', 'type': '*mut ffi::c_void'}, {'name': 'content', 'type': '*mut ffi::c_void'}]`
- New: `[{'name': 'mas', 'type': '*mut ma_state'}, {'name': 'node', 'type': '*mut maple_node'}, {'name': 'r_min', 'type': 'ffi::c_ulong'}, {'name': 'r_max', 'type': 'ffi::c_ulong'}, {'name': 'type_', 'type': 'maple_type'}, {'name': 'offset_end', 'type': 'ffi::c_uchar'}, {'name': 'pivots', 'type': '*mut ffi::c_ulong'}, {'name': 'end_piv', 'type': 'ffi::c_ulong'}, {'name': 'slots', 'type': '*mut *mut ffi::c_void'}, {'name': 'entry', 'type': '*mut ffi::c_void'}, {'name': 'content', 'type': '*mut ffi::c_void'}, {'name': 'vacant_height', 'type': 'ffi::c_uchar'}, {'name': 'sufficient_height', 'type': 'ffi::c_uchar'}]`

### Rust Evidence

- Graph edges: `1`

## W-000562 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: mod_arch_specific
- Explanation: mod_arch_specific changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'num_orcs', 'type': 'ffi::c_uint'}, {'name': 'orc_unwind_ip', 'type': '*mut ffi::c_int'}, {'name': 'orc_unwind', 'type': '*mut orc_entry'}]`
- New: `[{'name': 'num_orcs', 'type': 'ffi::c_uint'}, {'name': 'orc_unwind_ip', 'type': '*mut ffi::c_int'}, {'name': 'orc_unwind', 'type': '*mut orc_entry'}, {'name': 'its_pages', 'type': 'its_array'}]`

### Rust Evidence

- Graph edges: `1`

## W-000567 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: per_cpu_zonestat
- Explanation: per_cpu_zonestat changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'vm_stat_diff', 'type': '[s8; 11usize]'}, {'name': 'stat_threshold', 'type': 's8'}, {'name': 'vm_numa_event', 'type': '[ffi::c_ulong; 6usize]'}]`
- New: `[{'name': 'vm_stat_diff', 'type': '[s8; 10usize]'}, {'name': 'stat_threshold', 'type': 's8'}, {'name': 'vm_numa_event', 'type': '[ffi::c_ulong; 6usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000569 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: platform_device_id
- Explanation: platform_device_id changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '[ffi::c_char; 20usize]'}, {'name': 'driver_data', 'type': 'kernel_ulong_t'}]`
- New: `[{'name': 'name', 'type': '[ffi::c_char; 24usize]'}, {'name': 'driver_data', 'type': 'kernel_ulong_t'}]`

### Rust Evidence

- Graph edges: `1`

## W-000571 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: ratelimit_state
- Explanation: ratelimit_state changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'interval', 'type': 'ffi::c_int'}, {'name': 'burst', 'type': 'ffi::c_int'}, {'name': 'printed', 'type': 'ffi::c_int'}, {'name': 'missed', 'type': 'ffi::c_int'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'begin', 'type': 'ffi::c_ulong'}]`
- New: `[{'name': 'lock', 'type': 'raw_spinlock_t'}, {'name': 'interval', 'type': 'ffi::c_int'}, {'name': 'burst', 'type': 'ffi::c_int'}, {'name': 'rs_n_left', 'type': 'atomic_t'}, {'name': 'missed', 'type': 'atomic_t'}, {'name': 'flags', 'type': 'ffi::c_uint'}, {'name': 'begin', 'type': 'ffi::c_ulong'}]`

### Rust Evidence

- Graph edges: `1`

## W-000572 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: rt_mutex_waiter
- Explanation: rt_mutex_waiter changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': '_address', 'type': 'u8'}]`
- New: `[]`

### Rust Evidence

- Graph edges: `1`

## W-000573 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: sb_writers
- Explanation: sb_writers changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'frozen', 'type': 'ffi::c_ushort'}, {'name': 'freeze_kcount', 'type': 'ffi::c_int'}, {'name': 'freeze_ucount', 'type': 'ffi::c_int'}, {'name': 'rw_sem', 'type': '[percpu_rw_semaphore; 3usize]'}]`
- New: `[{'name': 'frozen', 'type': 'ffi::c_ushort'}, {'name': 'freeze_kcount', 'type': 'ffi::c_int'}, {'name': 'freeze_ucount', 'type': 'ffi::c_int'}, {'name': 'freeze_owner', 'type': '*const ffi::c_void'}, {'name': 'rw_sem', 'type': '[percpu_rw_semaphore; 3usize]'}]`

### Rust Evidence

- Graph edges: `1`

## W-000575 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: super_block
- Explanation: super_block changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'ffi::c_ulong'}, {'name': 's_iflags', 'type': 'ffi::c_ulong'}, {'name': 's_magic', 'type': 'ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut ffi::c_void'}, {'name': 's_xattr', 'type': '*const *mut xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': 'list_head'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': 'u32_'}, {'name': 's_fsnotify_info', 'type': '*mut fsnotify_sb_info'}, {'name': 's_id', 'type': '[ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const ffi::c_char'}, {'name': 's_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': 'u32'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}]`
- New: `[{'name': 's_list', 'type': 'list_head'}, {'name': 's_dev', 'type': 'dev_t'}, {'name': 's_blocksize_bits', 'type': 'ffi::c_uchar'}, {'name': 's_blocksize', 'type': 'ffi::c_ulong'}, {'name': 's_maxbytes', 'type': 'loff_t'}, {'name': 's_type', 'type': '*mut file_system_type'}, {'name': 's_op', 'type': '*const super_operations'}, {'name': 'dq_op', 'type': '*const dquot_operations'}, {'name': 's_qcop', 'type': '*const quotactl_ops'}, {'name': 's_export_op', 'type': '*const export_operations'}, {'name': 's_flags', 'type': 'ffi::c_ulong'}, {'name': 's_iflags', 'type': 'ffi::c_ulong'}, {'name': 's_magic', 'type': 'ffi::c_ulong'}, {'name': 's_root', 'type': '*mut dentry'}, {'name': 's_umount', 'type': 'rw_semaphore'}, {'name': 's_count', 'type': 'ffi::c_int'}, {'name': 's_active', 'type': 'atomic_t'}, {'name': 's_security', 'type': '*mut ffi::c_void'}, {'name': 's_xattr', 'type': '*const *mut xattr_handler'}, {'name': 's_roots', 'type': 'hlist_bl_head'}, {'name': 's_mounts', 'type': 'list_head'}, {'name': 's_bdev', 'type': '*mut block_device'}, {'name': 's_bdev_file', 'type': '*mut file'}, {'name': 's_bdi', 'type': '*mut backing_dev_info'}, {'name': 's_mtd', 'type': '*mut mtd_info'}, {'name': 's_instances', 'type': 'hlist_node'}, {'name': 's_quota_types', 'type': 'ffi::c_uint'}, {'name': 's_dquot', 'type': 'quota_info'}, {'name': 's_writers', 'type': 'sb_writers'}, {'name': 's_fs_info', 'type': '*mut ffi::c_void'}, {'name': 's_time_gran', 'type': 'u32_'}, {'name': 's_time_min', 'type': 'time64_t'}, {'name': 's_time_max', 'type': 'time64_t'}, {'name': 's_fsnotify_mask', 'type': 'u32_'}, {'name': 's_fsnotify_info', 'type': '*mut fsnotify_sb_info'}, {'name': 's_id', 'type': '[ffi::c_char; 32usize]'}, {'name': 's_uuid', 'type': 'uuid_t'}, {'name': 's_uuid_len', 'type': 'u8_'}, {'name': 's_sysfs_name', 'type': '[ffi::c_char; 37usize]'}, {'name': 's_max_links', 'type': 'ffi::c_uint'}, {'name': 's_vfs_rename_mutex', 'type': 'mutex'}, {'name': 's_subtype', 'type': '*const ffi::c_char'}, {'name': 's_d_op', 'type': '*const dentry_operations'}, {'name': 's_shrink', 'type': '*mut shrinker'}, {'name': 's_remove_count', 'type': 'atomic_long_t'}, {'name': 's_readonly_remount', 'type': 'ffi::c_int'}, {'name': 's_wb_err', 'type': 'errseq_t'}, {'name': 's_dio_done_wq', 'type': '*mut workqueue_struct'}, {'name': 's_pins', 'type': 'hlist_head'}, {'name': 's_user_ns', 'type': '*mut user_namespace'}, {'name': 's_dentry_lru', 'type': 'list_lru'}, {'name': 's_inode_lru', 'type': 'list_lru'}, {'name': 'rcu', 'type': 'callback_head'}, {'name': 'destroy_work', 'type': 'work_struct'}, {'name': 's_sync_lock', 'type': 'mutex'}, {'name': 's_stack_depth', 'type': 'ffi::c_int'}, {'name': '__bindgen_padding_0', 'type': '[u32; 15usize]'}, {'name': 's_inode_list_lock', 'type': 'spinlock_t'}, {'name': 's_inodes', 'type': 'list_head'}, {'name': 's_inode_wblist_lock', 'type': 'spinlock_t'}, {'name': 's_inodes_wb', 'type': 'list_head'}]`

### Rust Evidence

- Graph edges: `1`

## W-000577 FieldDrift

- Risk: Medium
- Score: 8.8
- Symbol: thread_struct
- Explanation: thread_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'tls_array', 'type': '[desc_struct; 3usize]'}, {'name': 'sp', 'type': 'ffi::c_ulong'}, {'name': 'es', 'type': 'ffi::c_ushort'}, {'name': 'ds', 'type': 'ffi::c_ushort'}, {'name': 'fsindex', 'type': 'ffi::c_ushort'}, {'name': 'gsindex', 'type': 'ffi::c_ushort'}, {'name': 'fsbase', 'type': 'ffi::c_ulong'}, {'name': 'gsbase', 'type': 'ffi::c_ulong'}, {'name': 'ptrace_bps', 'type': '[*mut perf_event; 4usize]'}, {'name': 'virtual_dr6', 'type': 'ffi::c_ulong'}, {'name': 'ptrace_dr7', 'type': 'ffi::c_ulong'}, {'name': 'cr2', 'type': 'ffi::c_ulong'}, {'name': 'trap_nr', 'type': 'ffi::c_ulong'}, {'name': 'error_code', 'type': 'ffi::c_ulong'}, {'name': 'io_bitmap', 'type': '*mut io_bitmap'}, {'name': 'iopl_emul', 'type': 'ffi::c_ulong'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pkru', 'type': 'u32_'}, {'name': '__bindgen_padding_0', 'type': '[u64; 5usize]'}, {'name': 'fpu', 'type': 'fpu'}]`
- New: `[{'name': 'tls_array', 'type': '[desc_struct; 3usize]'}, {'name': 'sp', 'type': 'ffi::c_ulong'}, {'name': 'es', 'type': 'ffi::c_ushort'}, {'name': 'ds', 'type': 'ffi::c_ushort'}, {'name': 'fsindex', 'type': 'ffi::c_ushort'}, {'name': 'gsindex', 'type': 'ffi::c_ushort'}, {'name': 'fsbase', 'type': 'ffi::c_ulong'}, {'name': 'gsbase', 'type': 'ffi::c_ulong'}, {'name': 'ptrace_bps', 'type': '[*mut perf_event; 4usize]'}, {'name': 'virtual_dr6', 'type': 'ffi::c_ulong'}, {'name': 'ptrace_dr7', 'type': 'ffi::c_ulong'}, {'name': 'cr2', 'type': 'ffi::c_ulong'}, {'name': 'trap_nr', 'type': 'ffi::c_ulong'}, {'name': 'error_code', 'type': 'ffi::c_ulong'}, {'name': 'io_bitmap', 'type': '*mut io_bitmap'}, {'name': 'iopl_emul', 'type': 'ffi::c_ulong'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'pkru', 'type': 'u32_'}]`

### Rust Evidence

- Graph edges: `1`

## W-000649 MacroConstDrift

- Risk: Medium
- Score: 8.4
- Symbol: cpuhp_state_CPUHP_AP_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `145`
- New: `144`

### Rust Evidence

- Graph edges: `4`

## W-000582 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: BIO_CHAIN
- Explanation: BIO_CHAIN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `3`

### Rust Evidence

- Graph edges: `3`

## W-000776 MacroConstDrift

- Risk: Medium
- Score: 8.2
- Symbol: l1tf_mitigations_L1TF_MITIGATION_FLUSH
- Explanation: l1tf_mitigations_L1TF_MITIGATION_FLUSH changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2`
- New: `3`

### Rust Evidence

- Graph edges: `3`

## W-000650 MacroConstDrift

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

## W-000720 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: cpuhp_state_CPUHP_BP_PREPARE_DYN
- Explanation: cpuhp_state_CPUHP_BP_PREPARE_DYN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `64`
- New: `63`

### Rust Evidence

- Graph edges: `2`

## W-000779 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: l1tf_mitigations_L1TF_MITIGATION_FULL
- Explanation: l1tf_mitigations_L1TF_MITIGATION_FULL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `5`

### Rust Evidence

- Graph edges: `2`

## W-000580 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: BIO_BPS_THROTTLED
- Explanation: BIO_BPS_THROTTLED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `5`

### Rust Evidence

- Graph edges: `1`

## W-000581 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: BIO_CGROUP_ACCT
- Explanation: BIO_CGROUP_ACCT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `7`

### Rust Evidence

- Graph edges: `1`

## W-000583 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: BIO_EMULATES_ZONE_APPEND
- Explanation: BIO_EMULATES_ZONE_APPEND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `12`

### Rust Evidence

- Graph edges: `1`

## W-000584 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: BIO_FLAG_LAST
- Explanation: BIO_FLAG_LAST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `13`

### Rust Evidence

- Graph edges: `1`

## W-000585 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: BIO_QOS_MERGED
- Explanation: BIO_QOS_MERGED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `9`

### Rust Evidence

- Graph edges: `1`

## W-000586 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: BIO_QOS_THROTTLED
- Explanation: BIO_QOS_THROTTLED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `8`

### Rust Evidence

- Graph edges: `1`

## W-000587 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: BIO_QUIET
- Explanation: BIO_QUIET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `2`

### Rust Evidence

- Graph edges: `1`

## W-000588 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: BIO_REFFED
- Explanation: BIO_REFFED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `4`

### Rust Evidence

- Graph edges: `1`

## W-000589 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: BIO_REMAPPED
- Explanation: BIO_REMAPPED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `10`

### Rust Evidence

- Graph edges: `1`

## W-000590 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: BIO_TRACE_COMPLETION
- Explanation: BIO_TRACE_COMPLETION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000591 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: BIO_ZONE_WRITE_PLUGGING
- Explanation: BIO_ZONE_WRITE_PLUGGING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000592 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: INPUT_DEVICE_ID_SW_MAX
- Explanation: INPUT_DEVICE_ID_SW_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `17`

### Rust Evidence

- Graph edges: `1`

## W-000593 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: NETLINK_MAX_COOKIE_LEN
- Explanation: NETLINK_MAX_COOKIE_LEN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `8`

### Rust Evidence

- Graph edges: `1`

## W-000594 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: PCI_EXT_CAP_ID_MAX
- Explanation: PCI_EXT_CAP_ID_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-000595 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: PLATFORM_NAME_SIZE
- Explanation: PLATFORM_NAME_SIZE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `24`

### Rust Evidence

- Graph edges: `1`

## W-000596 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: QUEUE_FLAG_MAX
- Explanation: QUEUE_FLAG_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `15`

### Rust Evidence

- Graph edges: `1`

## W-000597 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: X86_FEATURE_INDIRECT_THUNK_ITS
- Explanation: X86_FEATURE_INDIRECT_THUNK_ITS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `681`
- New: `682`

### Rust Evidence

- Graph edges: `1`

## W-000598 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ACPI_CPUDRV_DEAD
- Explanation: cpuhp_state_CPUHP_ACPI_CPUDRV_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `23`
- New: `22`

### Rust Evidence

- Graph edges: `1`

## W-000599 MacroConstDrift

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

## W-000600 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARC_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARC_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `127`
- New: `126`

### Rust Evidence

- Graph edges: `1`

## W-000601 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM64_DEBUG_MONITORS_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM64_DEBUG_MONITORS_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `111`
- New: `110`

### Rust Evidence

- Graph edges: `1`

## W-000602 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM64_ISNDEP_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM64_ISNDEP_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `139`
- New: `138`

### Rust Evidence

- Graph edges: `1`

## W-000603 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARMADA_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARMADA_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `125`
- New: `124`

### Rust Evidence

- Graph edges: `1`

## W-000604 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_EVTSTRM_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_EVTSTRM_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `119`
- New: `118`

### Rust Evidence

- Graph edges: `1`

## W-000605 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_ARCH_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `118`
- New: `117`

### Rust Evidence

- Graph edges: `1`

## W-000606 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CACHE_B15_RAC_DEAD
- Explanation: cpuhp_state_CPUHP_AP_ARM_CACHE_B15_RAC_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `35`
- New: `34`

### Rust Evidence

- Graph edges: `1`

## W-000607 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CACHE_B15_RAC_DYING
- Explanation: cpuhp_state_CPUHP_AP_ARM_CACHE_B15_RAC_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `144`
- New: `143`

### Rust Evidence

- Graph edges: `1`

## W-000608 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_CTI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_CTI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `138`
- New: `137`

### Rust Evidence

- Graph edges: `1`

## W-000609 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_CORESIGHT_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `137`
- New: `136`

### Rust Evidence

- Graph edges: `1`

## W-000610 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_GLOBAL_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_GLOBAL_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `120`
- New: `119`

### Rust Evidence

- Graph edges: `1`

## W-000611 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_L2X0_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_L2X0_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `116`
- New: `115`

### Rust Evidence

- Graph edges: `1`

## W-000612 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_MVEBU_COHERENCY
- Explanation: cpuhp_state_CPUHP_AP_ARM_MVEBU_COHERENCY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `105`
- New: `104`

### Rust Evidence

- Graph edges: `1`

## W-000613 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_MVEBU_SYNC_CLOCKS
- Explanation: cpuhp_state_CPUHP_AP_ARM_MVEBU_SYNC_CLOCKS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `154`
- New: `153`

### Rust Evidence

- Graph edges: `1`

## W-000614 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_TWD_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_TWD_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `122`
- New: `121`

### Rust Evidence

- Graph edges: `1`

## W-000615 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_VFP_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_VFP_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `110`
- New: `109`

### Rust Evidence

- Graph edges: `1`

## W-000616 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_XEN_RUNSTATE_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_XEN_RUNSTATE_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `136`
- New: `135`

### Rust Evidence

- Graph edges: `1`

## W-000617 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ARM_XEN_STARTING
- Explanation: cpuhp_state_CPUHP_AP_ARM_XEN_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `135`
- New: `134`

### Rust Evidence

- Graph edges: `1`

## W-000618 MacroConstDrift

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

## W-000619 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_BLK_MQ_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_BLK_MQ_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `153`
- New: `152`

### Rust Evidence

- Graph edges: `1`

## W-000620 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CACHECTRL_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CACHECTRL_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `89`
- New: `88`

### Rust Evidence

- Graph edges: `1`

## W-000621 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CLINT_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CLINT_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `130`
- New: `129`

### Rust Evidence

- Graph edges: `1`

## W-000622 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CPU_PM_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CPU_PM_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `92`
- New: `91`

### Rust Evidence

- Graph edges: `1`

## W-000623 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_CSKY_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_CSKY_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `131`
- New: `130`

### Rust Evidence

- Graph edges: `1`

## W-000624 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_DTPM_CPU_DEAD
- Explanation: cpuhp_state_CPUHP_AP_DTPM_CPU_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `37`
- New: `36`

### Rust Evidence

- Graph edges: `1`

## W-000625 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_DUMMY_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_DUMMY_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `134`
- New: `133`

### Rust Evidence

- Graph edges: `1`

## W-000626 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_EXYNOS4_MCT_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_EXYNOS4_MCT_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `117`
- New: `116`

### Rust Evidence

- Graph edges: `1`

## W-000627 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_HRTIMERS_DYING
- Explanation: cpuhp_state_CPUHP_AP_HRTIMERS_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `141`
- New: `140`

### Rust Evidence

- Graph edges: `1`

## W-000628 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_HYPERV_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_HYPERV_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `148`
- New: `147`

### Rust Evidence

- Graph edges: `1`

## W-000629 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_HYPERV_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_HYPERV_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `133`
- New: `132`

### Rust Evidence

- Graph edges: `1`

## W-000630 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IDLE_DEAD
- Explanation: cpuhp_state_CPUHP_AP_IDLE_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `87`
- New: `86`

### Rust Evidence

- Graph edges: `1`

## W-000631 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_AFFINITY_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_IRQ_AFFINITY_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `152`
- New: `151`

### Rust Evidence

- Graph edges: `1`

## W-000632 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_APPLE_AIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_APPLE_AIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `95`
- New: `94`

### Rust Evidence

- Graph edges: `1`

## W-000633 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_ARMADA_XP_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_ARMADA_XP_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `96`
- New: `95`

### Rust Evidence

- Graph edges: `1`

## W-000634 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_AVECINTC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_AVECINTC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `100`
- New: `99`

### Rust Evidence

- Graph edges: `1`

## W-000635 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_BCM2836_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_BCM2836_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `97`
- New: `96`

### Rust Evidence

- Graph edges: `1`

## W-000636 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_EIOINTC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_EIOINTC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `99`
- New: `98`

### Rust Evidence

- Graph edges: `1`

## W-000637 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_GIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_GIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `93`
- New: `92`

### Rust Evidence

- Graph edges: `1`

## W-000638 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_HIP04_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_HIP04_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `94`
- New: `93`

### Rust Evidence

- Graph edges: `1`

## W-000639 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_MIPS_GIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_MIPS_GIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `98`
- New: `97`

### Rust Evidence

- Graph edges: `1`

## W-000640 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_RISCV_IMSIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_RISCV_IMSIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `103`
- New: `102`

### Rust Evidence

- Graph edges: `1`

## W-000641 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_RISCV_SBI_IPI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_RISCV_SBI_IPI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `104`
- New: `103`

### Rust Evidence

- Graph edges: `1`

## W-000642 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_SIFIVE_PLIC_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_SIFIVE_PLIC_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `101`
- New: `100`

### Rust Evidence

- Graph edges: `1`

## W-000643 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_IRQ_THEAD_ACLINT_SSWI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_IRQ_THEAD_ACLINT_SSWI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `102`
- New: `101`

### Rust Evidence

- Graph edges: `1`

## W-000644 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_JCORE_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_JCORE_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `121`
- New: `120`

### Rust Evidence

- Graph edges: `1`

## W-000645 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_KTHREADS_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_KTHREADS_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `192`
- New: `191`

### Rust Evidence

- Graph edges: `1`

## W-000646 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_KVM_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_KVM_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `149`
- New: `148`

### Rust Evidence

- Graph edges: `1`

## W-000647 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_MIPS_GIC_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_MIPS_GIC_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `126`
- New: `125`

### Rust Evidence

- Graph edges: `1`

## W-000648 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_OFFLINE
- Explanation: cpuhp_state_CPUHP_AP_OFFLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `88`
- New: `87`

### Rust Evidence

- Graph edges: `1`

## W-000651 MacroConstDrift

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

## W-000652 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_ONLINE_IDLE
- Explanation: cpuhp_state_CPUHP_AP_ONLINE_IDLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `147`
- New: `146`

### Rust Evidence

- Graph edges: `1`

## W-000653 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_ACPI_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_ACPI_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `113`
- New: `112`

### Rust Evidence

- Graph edges: `1`

## W-000654 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_APM_XGENE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_APM_XGENE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `176`
- New: `175`

### Rust Evidence

- Graph edges: `1`

## W-000655 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CAVIUM_TX2_UNCORE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CAVIUM_TX2_UNCORE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `177`
- New: `176`

### Rust Evidence

- Graph edges: `1`

## W-000656 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CCI_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CCI_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `163`
- New: `162`

### Rust Evidence

- Graph edges: `1`

## W-000657 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_CCN_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_CCN_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `164`
- New: `163`

### Rust Evidence

- Graph edges: `1`

## W-000658 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_CPA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_CPA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `165`
- New: `164`

### Rust Evidence

- Graph edges: `1`

## W-000659 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_DDRC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_DDRC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `166`
- New: `165`

### Rust Evidence

- Graph edges: `1`

## W-000660 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_HHA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_HHA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `167`
- New: `166`

### Rust Evidence

- Graph edges: `1`

## W-000661 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_L3_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_L3_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `168`
- New: `167`

### Rust Evidence

- Graph edges: `1`

## W-000662 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PA_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PA_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `169`
- New: `168`

### Rust Evidence

- Graph edges: `1`

## W-000663 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PCIE_PMU_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_PCIE_PMU_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `171`
- New: `170`

### Rust Evidence

- Graph edges: `1`

## W-000664 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_SLLC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HISI_SLLC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `170`
- New: `169`

### Rust Evidence

- Graph edges: `1`

## W-000665 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HNS3_PMU_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HNS3_PMU_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `172`
- New: `171`

### Rust Evidence

- Graph edges: `1`

## W-000666 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_HW_BREAKPOINT_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_HW_BREAKPOINT_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `112`
- New: `111`

### Rust Evidence

- Graph edges: `1`

## W-000667 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_L2X0_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_L2X0_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `173`
- New: `172`

### Rust Evidence

- Graph edges: `1`

## W-000668 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_MARVELL_CN10K_DDR_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_MARVELL_CN10K_DDR_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `178`
- New: `177`

### Rust Evidence

- Graph edges: `1`

## W-000669 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_MRVL_PEM_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_MRVL_PEM_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `179`
- New: `178`

### Rust Evidence

- Graph edges: `1`

## W-000670 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L2_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L2_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `174`
- New: `173`

### Rust Evidence

- Graph edges: `1`

## W-000671 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L3_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_QCOM_L3_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `175`
- New: `174`

### Rust Evidence

- Graph edges: `1`

## W-000672 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ARM_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_ARM_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `114`
- New: `113`

### Rust Evidence

- Graph edges: `1`

## W-000673 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_CSKY_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_CSKY_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `186`
- New: `185`

### Rust Evidence

- Graph edges: `1`

## W-000674 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `156`
- New: `155`

### Rust Evidence

- Graph edges: `1`

## W-000675 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_CORE_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_CORE_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `181`
- New: `180`

### Rust Evidence

- Graph edges: `1`

## W-000676 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_24x7_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_24x7_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `184`
- New: `183`

### Rust Evidence

- Graph edges: `1`

## W-000677 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_GPCI_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_HV_GPCI_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `185`
- New: `184`

### Rust Evidence

- Graph edges: `1`

## W-000678 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_NEST_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_NEST_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `180`
- New: `179`

### Rust Evidence

- Graph edges: `1`

## W-000679 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_THREAD_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_THREAD_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `182`
- New: `181`

### Rust Evidence

- Graph edges: `1`

## W-000680 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_POWERPC_TRACE_IMC_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_POWERPC_TRACE_IMC_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `183`
- New: `182`

### Rust Evidence

- Graph edges: `1`

## W-000681 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_RISCV_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_RISCV_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `115`
- New: `114`

### Rust Evidence

- Graph edges: `1`

## W-000682 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_S390_CF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_S390_CF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `161`
- New: `160`

### Rust Evidence

- Graph edges: `1`

## W-000683 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_S390_SF_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_S390_SF_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `162`
- New: `161`

### Rust Evidence

- Graph edges: `1`

## W-000684 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_IBS_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_IBS_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `108`
- New: `107`

### Rust Evidence

- Graph edges: `1`

## W-000685 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_POWER_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_POWER_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `160`
- New: `159`

### Rust Evidence

- Graph edges: `1`

## W-000686 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `159`
- New: `158`

### Rust Evidence

- Graph edges: `1`

## W-000687 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_AMD_UNCORE_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `106`
- New: `105`

### Rust Evidence

- Graph edges: `1`

## W-000688 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `157`
- New: `156`

### Rust Evidence

- Graph edges: `1`

## W-000689 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `107`
- New: `106`

### Rust Evidence

- Graph edges: `1`

## W-000690 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_X86_UNCORE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_PERF_X86_UNCORE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `158`
- New: `157`

### Rust Evidence

- Graph edges: `1`

## W-000691 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_PERF_XTENSA_STARTING
- Explanation: cpuhp_state_CPUHP_AP_PERF_XTENSA_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `109`
- New: `108`

### Rust Evidence

- Graph edges: `1`

## W-000692 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_QCOM_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_QCOM_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `123`
- New: `122`

### Rust Evidence

- Graph edges: `1`

## W-000693 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RANDOM_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_RANDOM_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `190`
- New: `189`

### Rust Evidence

- Graph edges: `1`

## W-000694 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RCUTREE_DYING
- Explanation: cpuhp_state_CPUHP_AP_RCUTREE_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `91`
- New: `90`

### Rust Evidence

- Graph edges: `1`

## W-000695 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RCUTREE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_RCUTREE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `191`
- New: `190`

### Rust Evidence

- Graph edges: `1`

## W-000696 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_REALTEK_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_REALTEK_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `128`
- New: `127`

### Rust Evidence

- Graph edges: `1`

## W-000697 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_RISCV_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_RISCV_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `129`
- New: `128`

### Rust Evidence

- Graph edges: `1`

## W-000698 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SCHED_STARTING
- Explanation: cpuhp_state_CPUHP_AP_SCHED_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `90`
- New: `89`

### Rust Evidence

- Graph edges: `1`

## W-000699 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SCHED_WAIT_EMPTY
- Explanation: cpuhp_state_CPUHP_AP_SCHED_WAIT_EMPTY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `150`
- New: `149`

### Rust Evidence

- Graph edges: `1`

## W-000700 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SMPBOOT_THREADS
- Explanation: cpuhp_state_CPUHP_AP_SMPBOOT_THREADS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `151`
- New: `150`

### Rust Evidence

- Graph edges: `1`

## W-000701 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_SMPCFD_DYING
- Explanation: cpuhp_state_CPUHP_AP_SMPCFD_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `140`
- New: `139`

### Rust Evidence

- Graph edges: `1`

## W-000702 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TEGRA_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_TEGRA_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `124`
- New: `123`

### Rust Evidence

- Graph edges: `1`

## W-000703 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TICK_DYING
- Explanation: cpuhp_state_CPUHP_AP_TICK_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `142`
- New: `141`

### Rust Evidence

- Graph edges: `1`

## W-000704 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TI_GP_TIMER_STARTING
- Explanation: cpuhp_state_CPUHP_AP_TI_GP_TIMER_STARTING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `132`
- New: `131`

### Rust Evidence

- Graph edges: `1`

## W-000705 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_TMIGR_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_TMIGR_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `187`
- New: `186`

### Rust Evidence

- Graph edges: `1`

## W-000706 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_WATCHDOG_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_WATCHDOG_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `188`
- New: `187`

### Rust Evidence

- Graph edges: `1`

## W-000707 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_WORKQUEUE_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_WORKQUEUE_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `189`
- New: `188`

### Rust Evidence

- Graph edges: `1`

## W-000708 MacroConstDrift

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

## W-000709 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_INTEL_EPB_ONLINE
- Explanation: cpuhp_state_CPUHP_AP_X86_INTEL_EPB_ONLINE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `155`
- New: `154`

### Rust Evidence

- Graph edges: `1`

## W-000710 MacroConstDrift

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

## W-000711 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_AP_X86_TBOOT_DYING
- Explanation: cpuhp_state_CPUHP_AP_X86_TBOOT_DYING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `143`
- New: `142`

### Rust Evidence

- Graph edges: `1`

## W-000712 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ARM64_FPSIMD_DEAD
- Explanation: cpuhp_state_CPUHP_ARM64_FPSIMD_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `17`

### Rust Evidence

- Graph edges: `1`

## W-000713 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ARM_BL_PREPARE
- Explanation: cpuhp_state_CPUHP_ARM_BL_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `56`
- New: `55`

### Rust Evidence

- Graph edges: `1`

## W-000714 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ARM_OMAP_WAKE_DEAD
- Explanation: cpuhp_state_CPUHP_ARM_OMAP_WAKE_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `18`

### Rust Evidence

- Graph edges: `1`

## W-000715 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ARM_SHMOBILE_SCU_PREPARE
- Explanation: cpuhp_state_CPUHP_ARM_SHMOBILE_SCU_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-000716 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_BIO_DEAD
- Explanation: cpuhp_state_CPUHP_BIO_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `22`
- New: `21`

### Rust Evidence

- Graph edges: `1`

## W-000717 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_BLK_MQ_DEAD
- Explanation: cpuhp_state_CPUHP_BLK_MQ_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `25`
- New: `24`

### Rust Evidence

- Graph edges: `1`

## W-000718 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_BLOCK_SOFTIRQ_DEAD
- Explanation: cpuhp_state_CPUHP_BLOCK_SOFTIRQ_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `20`

### Rust Evidence

- Graph edges: `1`

## W-000719 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_BP_KICK_AP
- Explanation: cpuhp_state_CPUHP_BP_KICK_AP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `85`
- New: `84`

### Rust Evidence

- Graph edges: `1`

## W-000721 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_BP_PREPARE_DYN_END
- Explanation: cpuhp_state_CPUHP_BP_PREPARE_DYN_END changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `84`
- New: `83`

### Rust Evidence

- Graph edges: `1`

## W-000722 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_BRINGUP_CPU
- Explanation: cpuhp_state_CPUHP_BRINGUP_CPU changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `86`
- New: `85`

### Rust Evidence

- Graph edges: `1`

## W-000723 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_CPUIDLE_COUPLED_PREPARE
- Explanation: cpuhp_state_CPUHP_CPUIDLE_COUPLED_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `46`

### Rust Evidence

- Graph edges: `1`

## W-000724 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_CPUIDLE_DEAD
- Explanation: cpuhp_state_CPUHP_CPUIDLE_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `16`

### Rust Evidence

- Graph edges: `1`

## W-000725 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_DEBUG_OBJ_DEAD
- Explanation: cpuhp_state_CPUHP_DEBUG_OBJ_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `11`

### Rust Evidence

- Graph edges: `1`

## W-000726 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_FS_BUFF_DEAD
- Explanation: cpuhp_state_CPUHP_FS_BUFF_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `26`
- New: `25`

### Rust Evidence

- Graph edges: `1`

## W-000727 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_HRTIMERS_PREPARE
- Explanation: cpuhp_state_CPUHP_HRTIMERS_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `41`
- New: `40`

### Rust Evidence

- Graph edges: `1`

## W-000728 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_IBMVNIC_DEAD
- Explanation: cpuhp_state_CPUHP_IBMVNIC_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `9`

### Rust Evidence

- Graph edges: `1`

## W-000729 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_IOMMU_IOVA_DEAD
- Explanation: cpuhp_state_CPUHP_IOMMU_IOVA_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `34`
- New: `33`

### Rust Evidence

- Graph edges: `1`

## W-000730 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_IRQ_POLL_DEAD
- Explanation: cpuhp_state_CPUHP_IRQ_POLL_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `19`

### Rust Evidence

- Graph edges: `1`

## W-000731 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_KVM_PPC_BOOK3S_PREPARE
- Explanation: cpuhp_state_CPUHP_KVM_PPC_BOOK3S_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `59`
- New: `58`

### Rust Evidence

- Graph edges: `1`

## W-000732 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MD_RAID5_PREPARE
- Explanation: cpuhp_state_CPUHP_MD_RAID5_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `44`

### Rust Evidence

- Graph edges: `1`

## W-000733 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MIPS_SOC_PREPARE
- Explanation: cpuhp_state_CPUHP_MIPS_SOC_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `63`
- New: `62`

### Rust Evidence

- Graph edges: `1`

## W-000734 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MM_MEMCQ_DEAD
- Explanation: cpuhp_state_CPUHP_MM_MEMCQ_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `28`
- New: `27`

### Rust Evidence

- Graph edges: `1`

## W-000735 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MM_VMSTAT_DEAD
- Explanation: cpuhp_state_CPUHP_MM_VMSTAT_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `13`

### Rust Evidence

- Graph edges: `1`

## W-000736 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MM_WRITEBACK_DEAD
- Explanation: cpuhp_state_CPUHP_MM_WRITEBACK_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `12`

### Rust Evidence

- Graph edges: `1`

## W-000737 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_MM_ZSWP_POOL_PREPARE
- Explanation: cpuhp_state_CPUHP_MM_ZSWP_POOL_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `57`

### Rust Evidence

- Graph edges: `1`

## W-000738 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_NET_DEV_DEAD
- Explanation: cpuhp_state_CPUHP_NET_DEV_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `32`
- New: `31`

### Rust Evidence

- Graph edges: `1`

## W-000739 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_NET_IUCV_PREPARE
- Explanation: cpuhp_state_CPUHP_NET_IUCV_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `55`
- New: `54`

### Rust Evidence

- Graph edges: `1`

## W-000740 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_NET_MVNETA_DEAD
- Explanation: cpuhp_state_CPUHP_NET_MVNETA_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `15`

### Rust Evidence

- Graph edges: `1`

## W-000741 MacroConstDrift

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

## W-000742 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_PADATA_DEAD
- Explanation: cpuhp_state_CPUHP_PADATA_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `36`
- New: `35`

### Rust Evidence

- Graph edges: `1`

## W-000743 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_PAGE_ALLOC
- Explanation: cpuhp_state_CPUHP_PAGE_ALLOC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `31`
- New: `30`

### Rust Evidence

- Graph edges: `1`

## W-000744 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_PCI_XGENE_DEAD
- Explanation: cpuhp_state_CPUHP_PCI_XGENE_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `33`
- New: `32`

### Rust Evidence

- Graph edges: `1`

## W-000745 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_PERCPU_CNT_DEAD
- Explanation: cpuhp_state_CPUHP_PERCPU_CNT_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `29`
- New: `28`

### Rust Evidence

- Graph edges: `1`

## W-000746 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_PERF_POWER
- Explanation: cpuhp_state_CPUHP_PERF_POWER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `4`

### Rust Evidence

- Graph edges: `1`

## W-000747 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_PERF_SUPERH
- Explanation: cpuhp_state_CPUHP_PERF_SUPERH changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `5`

### Rust Evidence

- Graph edges: `1`

## W-000748 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_PERF_X86_AMD_UNCORE_PREP
- Explanation: cpuhp_state_CPUHP_PERF_X86_AMD_UNCORE_PREP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `3`

### Rust Evidence

- Graph edges: `1`

## W-000749 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_PERF_X86_PREPARE
- Explanation: cpuhp_state_CPUHP_PERF_X86_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `2`

### Rust Evidence

- Graph edges: `1`

## W-000750 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_POWERPC_MMU_CTX_PREPARE
- Explanation: cpuhp_state_CPUHP_POWERPC_MMU_CTX_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-000751 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_POWERPC_PMAC_PREPARE
- Explanation: cpuhp_state_CPUHP_POWERPC_PMAC_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `47`

### Rust Evidence

- Graph edges: `1`

## W-000752 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_POWER_NUMA_PREPARE
- Explanation: cpuhp_state_CPUHP_POWER_NUMA_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `40`
- New: `39`

### Rust Evidence

- Graph edges: `1`

## W-000753 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_PRINTK_DEAD
- Explanation: cpuhp_state_CPUHP_PRINTK_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `27`
- New: `26`

### Rust Evidence

- Graph edges: `1`

## W-000754 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_RADIX_DEAD
- Explanation: cpuhp_state_CPUHP_RADIX_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `30`
- New: `29`

### Rust Evidence

- Graph edges: `1`

## W-000755 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_RANDOM_PREPARE
- Explanation: cpuhp_state_CPUHP_RANDOM_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `38`
- New: `37`

### Rust Evidence

- Graph edges: `1`

## W-000756 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_RCUTREE_PREP
- Explanation: cpuhp_state_CPUHP_RCUTREE_PREP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `45`

### Rust Evidence

- Graph edges: `1`

## W-000757 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_RELAY_PREPARE
- Explanation: cpuhp_state_CPUHP_RELAY_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `43`

### Rust Evidence

- Graph edges: `1`

## W-000758 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_S390_PFAULT_DEAD
- Explanation: cpuhp_state_CPUHP_S390_PFAULT_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `24`
- New: `23`

### Rust Evidence

- Graph edges: `1`

## W-000759 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_SH_SH3X_PREPARE
- Explanation: cpuhp_state_CPUHP_SH_SH3X_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-000760 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_SLUB_DEAD
- Explanation: cpuhp_state_CPUHP_SLUB_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `10`

### Rust Evidence

- Graph edges: `1`

## W-000761 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_SMPCFD_PREPARE
- Explanation: cpuhp_state_CPUHP_SMPCFD_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `42`

### Rust Evidence

- Graph edges: `1`

## W-000762 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_SOFTIRQ_DEAD
- Explanation: cpuhp_state_CPUHP_SOFTIRQ_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `14`

### Rust Evidence

- Graph edges: `1`

## W-000763 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TEARDOWN_CPU
- Explanation: cpuhp_state_CPUHP_TEARDOWN_CPU changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `146`
- New: `145`

### Rust Evidence

- Graph edges: `1`

## W-000764 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TIMERS_PREPARE
- Explanation: cpuhp_state_CPUHP_TIMERS_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `61`
- New: `60`

### Rust Evidence

- Graph edges: `1`

## W-000765 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TMIGR_PREPARE
- Explanation: cpuhp_state_CPUHP_TMIGR_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `62`
- New: `61`

### Rust Evidence

- Graph edges: `1`

## W-000766 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TOPOLOGY_PREPARE
- Explanation: cpuhp_state_CPUHP_TOPOLOGY_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `54`
- New: `53`

### Rust Evidence

- Graph edges: `1`

## W-000767 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_TRACE_RB_PREPARE
- Explanation: cpuhp_state_CPUHP_TRACE_RB_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `57`
- New: `56`

### Rust Evidence

- Graph edges: `1`

## W-000768 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_VIRT_NET_DEAD
- Explanation: cpuhp_state_CPUHP_VIRT_NET_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `8`

### Rust Evidence

- Graph edges: `1`

## W-000769 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_WORKQUEUE_PREP
- Explanation: cpuhp_state_CPUHP_WORKQUEUE_PREP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `39`
- New: `38`

### Rust Evidence

- Graph edges: `1`

## W-000770 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_X2APIC_PREPARE
- Explanation: cpuhp_state_CPUHP_X2APIC_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `42`
- New: `41`

### Rust Evidence

- Graph edges: `1`

## W-000771 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_X86_HPET_DEAD
- Explanation: cpuhp_state_CPUHP_X86_HPET_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000772 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_X86_MCE_DEAD
- Explanation: cpuhp_state_CPUHP_X86_MCE_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `7`

### Rust Evidence

- Graph edges: `1`

## W-000773 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_XEN_EVTCHN_PREPARE
- Explanation: cpuhp_state_CPUHP_XEN_EVTCHN_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-000774 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_XEN_PREPARE
- Explanation: cpuhp_state_CPUHP_XEN_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-000775 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: cpuhp_state_CPUHP_ZCOMP_PREPARE
- Explanation: cpuhp_state_CPUHP_ZCOMP_PREPARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `60`
- New: `59`

### Rust Evidence

- Graph edges: `1`

## W-000777 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: l1tf_mitigations_L1TF_MITIGATION_FLUSH_NOSMT
- Explanation: l1tf_mitigations_L1TF_MITIGATION_FLUSH_NOSMT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `4`

### Rust Evidence

- Graph edges: `1`

## W-000778 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: l1tf_mitigations_L1TF_MITIGATION_FLUSH_NOWARN
- Explanation: l1tf_mitigations_L1TF_MITIGATION_FLUSH_NOWARN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `1`
- New: `2`

### Rust Evidence

- Graph edges: `1`

## W-000780 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: l1tf_mitigations_L1TF_MITIGATION_FULL_FORCE
- Explanation: l1tf_mitigations_L1TF_MITIGATION_FULL_FORCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `6`

### Rust Evidence

- Graph edges: `1`

## W-000781 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_ARP_PVLAN_DISABLE
- Explanation: skb_drop_reason_SKB_DROP_REASON_ARP_PVLAN_DISABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `114`
- New: `116`

### Rust Evidence

- Graph edges: `1`

## W-000782 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_BPF_CGROUP_EGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_BPF_CGROUP_EGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `54`

### Rust Evidence

- Graph edges: `1`

## W-000783 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_BRIDGE_INGRESS_STP_STATE
- Explanation: skb_drop_reason_SKB_DROP_REASON_BRIDGE_INGRESS_STP_STATE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `116`
- New: `118`

### Rust Evidence

- Graph edges: `1`

## W-000784 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CAKE_FLOOD
- Explanation: skb_drop_reason_SKB_DROP_REASON_CAKE_FLOOD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `64`
- New: `66`

### Rust Evidence

- Graph edges: `1`

## W-000785 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_CPU_BACKLOG
- Explanation: skb_drop_reason_SKB_DROP_REASON_CPU_BACKLOG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `68`
- New: `70`

### Rust Evidence

- Graph edges: `1`

## W-000786 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DEV_HDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_DEV_HDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `75`
- New: `77`

### Rust Evidence

- Graph edges: `1`

## W-000787 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DEV_READY
- Explanation: skb_drop_reason_SKB_DROP_REASON_DEV_READY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `76`
- New: `78`

### Rust Evidence

- Graph edges: `1`

## W-000788 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_DUP_FRAG
- Explanation: skb_drop_reason_SKB_DROP_REASON_DUP_FRAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `91`
- New: `93`

### Rust Evidence

- Graph edges: `1`

## W-000789 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FQ_BAND_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FQ_BAND_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65`
- New: `67`

### Rust Evidence

- Graph edges: `1`

## W-000790 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FQ_FLOW_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FQ_FLOW_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `67`
- New: `69`

### Rust Evidence

- Graph edges: `1`

## W-000791 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FQ_HORIZON_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FQ_HORIZON_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `66`
- New: `68`

### Rust Evidence

- Graph edges: `1`

## W-000792 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FRAG_REASM_TIMEOUT
- Explanation: skb_drop_reason_SKB_DROP_REASON_FRAG_REASM_TIMEOUT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `92`
- New: `94`

### Rust Evidence

- Graph edges: `1`

## W-000793 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FRAG_TOO_FAR
- Explanation: skb_drop_reason_SKB_DROP_REASON_FRAG_TOO_FAR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `93`
- New: `95`

### Rust Evidence

- Graph edges: `1`

## W-000794 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_FULL_RING
- Explanation: skb_drop_reason_SKB_DROP_REASON_FULL_RING changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `77`
- New: `79`

### Rust Evidence

- Graph edges: `1`

## W-000795 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_HDR_TRUNC
- Explanation: skb_drop_reason_SKB_DROP_REASON_HDR_TRUNC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `79`
- New: `81`

### Rust Evidence

- Graph edges: `1`

## W-000796 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_ICMP_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_ICMP_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `82`
- New: `84`

### Rust Evidence

- Graph edges: `1`

## W-000797 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_INVALID_PROTO
- Explanation: skb_drop_reason_SKB_DROP_REASON_INVALID_PROTO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `83`
- New: `85`

### Rust Evidence

- Graph edges: `1`

## W-000798 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6DISABLED
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6DISABLED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `54`
- New: `55`

### Rust Evidence

- Graph edges: `1`

## W-000799 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_BAD_EXTHDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_BAD_EXTHDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `95`
- New: `97`

### Rust Evidence

- Graph edges: `1`

## W-000800 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_CODE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_CODE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `98`
- New: `100`

### Rust Evidence

- Graph edges: `1`

## W-000801 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_OPTIONS
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_BAD_OPTIONS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `99`
- New: `101`

### Rust Evidence

- Graph edges: `1`

## W-000802 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_FRAG
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_FRAG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `96`
- New: `98`

### Rust Evidence

- Graph edges: `1`

## W-000803 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_HOP_LIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_HOP_LIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `97`
- New: `99`

### Rust Evidence

- Graph edges: `1`

## W-000804 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_NS_OTHERHOST
- Explanation: skb_drop_reason_SKB_DROP_REASON_IPV6_NDISC_NS_OTHERHOST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `100`
- New: `102`

### Rust Evidence

- Graph edges: `1`

## W-000805 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INADDRERRORS
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INADDRERRORS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `84`
- New: `86`

### Rust Evidence

- Graph edges: `1`

## W-000806 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INNOROUTES
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INNOROUTES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `85`
- New: `87`

### Rust Evidence

- Graph edges: `1`

## W-000807 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_DEST
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_DEST changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `89`
- New: `91`

### Rust Evidence

- Graph edges: `1`

## W-000808 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_INVALID_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `87`
- New: `89`

### Rust Evidence

- Graph edges: `1`

## W-000809 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_LOCALNET
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_LOCALNET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `88`
- New: `90`

### Rust Evidence

- Graph edges: `1`

## W-000810 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_LOCAL_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_LOCAL_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `86`
- New: `88`

### Rust Evidence

- Graph edges: `1`

## W-000811 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_OUTNOROUTES
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_OUTNOROUTES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `53`

### Rust Evidence

- Graph edges: `1`

## W-000812 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_IP_TUNNEL_ECN
- Explanation: skb_drop_reason_SKB_DROP_REASON_IP_TUNNEL_ECN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `111`
- New: `113`

### Rust Evidence

- Graph edges: `1`

## W-000813 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_LOCAL_MAC
- Explanation: skb_drop_reason_SKB_DROP_REASON_LOCAL_MAC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `113`
- New: `115`

### Rust Evidence

- Graph edges: `1`

## W-000814 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAC_IEEE_MAC_CONTROL
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAC_IEEE_MAC_CONTROL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `115`
- New: `117`

### Rust Evidence

- Graph edges: `1`

## W-000815 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAC_INVALID_SOURCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAC_INVALID_SOURCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `108`
- New: `110`

### Rust Evidence

- Graph edges: `1`

## W-000816 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_MAX
- Explanation: skb_drop_reason_SKB_DROP_REASON_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `117`
- New: `119`

### Rust Evidence

- Graph edges: `1`

## W-000817 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_CREATEFAIL
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_CREATEFAIL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `55`
- New: `56`

### Rust Evidence

- Graph edges: `1`

## W-000818 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_DEAD
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_DEAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `59`

### Rust Evidence

- Graph edges: `1`

## W-000819 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_FAILED
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_FAILED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `56`
- New: `57`

### Rust Evidence

- Graph edges: `1`

## W-000820 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NEIGH_QUEUEFULL
- Explanation: skb_drop_reason_SKB_DROP_REASON_NEIGH_QUEUEFULL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `57`
- New: `58`

### Rust Evidence

- Graph edges: `1`

## W-000821 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NOMEM
- Explanation: skb_drop_reason_SKB_DROP_REASON_NOMEM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `78`
- New: `80`

### Rust Evidence

- Graph edges: `1`

## W-000822 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_NO_TX_TARGET
- Explanation: skb_drop_reason_SKB_DROP_REASON_NO_TX_TARGET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `110`
- New: `112`

### Rust Evidence

- Graph edges: `1`

## W-000823 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PACKET_SOCK_ERROR
- Explanation: skb_drop_reason_SKB_DROP_REASON_PACKET_SOCK_ERROR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `103`
- New: `105`

### Rust Evidence

- Graph edges: `1`

## W-000824 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_PKT_TOO_BIG
- Explanation: skb_drop_reason_SKB_DROP_REASON_PKT_TOO_BIG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `90`
- New: `92`

### Rust Evidence

- Graph edges: `1`

## W-000825 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QDISC_CONGESTED
- Explanation: skb_drop_reason_SKB_DROP_REASON_QDISC_CONGESTED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `63`
- New: `65`

### Rust Evidence

- Graph edges: `1`

## W-000826 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QDISC_DROP
- Explanation: skb_drop_reason_SKB_DROP_REASON_QDISC_DROP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `61`
- New: `63`

### Rust Evidence

- Graph edges: `1`

## W-000827 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QDISC_OVERLIMIT
- Explanation: skb_drop_reason_SKB_DROP_REASON_QDISC_OVERLIMIT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `62`
- New: `64`

### Rust Evidence

- Graph edges: `1`

## W-000828 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_QUEUE_PURGE
- Explanation: skb_drop_reason_SKB_DROP_REASON_QUEUE_PURGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `101`
- New: `103`

### Rust Evidence

- Graph edges: `1`

## W-000829 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SECURITY_HOOK
- Explanation: skb_drop_reason_SKB_DROP_REASON_SECURITY_HOOK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `60`
- New: `62`

### Rust Evidence

- Graph edges: `1`

## W-000830 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_CSUM
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_CSUM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `72`
- New: `74`

### Rust Evidence

- Graph edges: `1`

## W-000831 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_GSO_SEG
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_GSO_SEG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `73`
- New: `75`

### Rust Evidence

- Graph edges: `1`

## W-000832 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_SKB_UCOPY_FAULT
- Explanation: skb_drop_reason_SKB_DROP_REASON_SKB_UCOPY_FAULT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `74`
- New: `76`

### Rust Evidence

- Graph edges: `1`

## W-000833 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TAP_FILTER
- Explanation: skb_drop_reason_SKB_DROP_REASON_TAP_FILTER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `80`
- New: `82`

### Rust Evidence

- Graph edges: `1`

## W-000834 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TAP_TXFILTER
- Explanation: skb_drop_reason_SKB_DROP_REASON_TAP_TXFILTER changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `81`
- New: `83`

### Rust Evidence

- Graph edges: `1`

## W-000835 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_ACK_UNSENT_DATA
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_ACK_UNSENT_DATA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `50`

### Rust Evidence

- Graph edges: `1`

## W-000836 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_CLOSE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_CLOSE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `46`

### Rust Evidence

- Graph edges: `1`

## W-000837 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_FASTOPEN
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_FASTOPEN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `46`
- New: `47`

### Rust Evidence

- Graph edges: `1`

## W-000838 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_ACK_SEQUENCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_ACK_SEQUENCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `42`
- New: `43`

### Rust Evidence

- Graph edges: `1`

## W-000839 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SEQUENCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SEQUENCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `41`
- New: `42`

### Rust Evidence

- Graph edges: `1`

## W-000840 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SYN
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_INVALID_SYN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `44`
- New: `45`

### Rust Evidence

- Graph edges: `1`

## W-000841 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_LISTEN_OVERFLOW
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_LISTEN_OVERFLOW changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `39`
- New: `40`

### Rust Evidence

- Graph edges: `1`

## W-000842 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_MINTTL
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_MINTTL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `94`
- New: `96`

### Rust Evidence

- Graph edges: `1`

## W-000843 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_DROP
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_DROP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `52`

### Rust Evidence

- Graph edges: `1`

## W-000844 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_QUEUE_PRUNE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OFO_QUEUE_PRUNE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `51`

### Rust Evidence

- Graph edges: `1`

## W-000845 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_ACK
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_ACK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `47`
- New: `48`

### Rust Evidence

- Graph edges: `1`

## W-000846 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_SEQUENCE
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_OLD_SEQUENCE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `40`
- New: `41`

### Rust Evidence

- Graph edges: `1`

## W-000847 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_RESET
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_RESET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `43`
- New: `44`

### Rust Evidence

- Graph edges: `1`

## W-000848 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_RFC7323_TSECR
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_RFC7323_TSECR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `38`
- New: `39`

### Rust Evidence

- Graph edges: `1`

## W-000849 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TCP_TOO_OLD_ACK
- Explanation: skb_drop_reason_SKB_DROP_REASON_TCP_TOO_OLD_ACK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `49`

### Rust Evidence

- Graph edges: `1`

## W-000850 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_CHAIN_NOTFOUND
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_CHAIN_NOTFOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `104`
- New: `106`

### Rust Evidence

- Graph edges: `1`

## W-000851 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_COOKIE_ERROR
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_COOKIE_ERROR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `102`
- New: `104`

### Rust Evidence

- Graph edges: `1`

## W-000852 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_EGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_EGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `59`
- New: `61`

### Rust Evidence

- Graph edges: `1`

## W-000853 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_INGRESS
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_INGRESS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `70`
- New: `72`

### Rust Evidence

- Graph edges: `1`

## W-000854 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TC_RECLASSIFY_LOOP
- Explanation: skb_drop_reason_SKB_DROP_REASON_TC_RECLASSIFY_LOOP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `105`
- New: `107`

### Rust Evidence

- Graph edges: `1`

## W-000855 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_TUNNEL_TXINFO
- Explanation: skb_drop_reason_SKB_DROP_REASON_TUNNEL_TXINFO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `112`
- New: `114`

### Rust Evidence

- Graph edges: `1`

## W-000856 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_UNHANDLED_PROTO
- Explanation: skb_drop_reason_SKB_DROP_REASON_UNHANDLED_PROTO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `71`
- New: `73`

### Rust Evidence

- Graph edges: `1`

## W-000857 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_ENTRY_EXISTS
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_ENTRY_EXISTS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `109`
- New: `111`

### Rust Evidence

- Graph edges: `1`

## W-000858 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_INVALID_HDR
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_INVALID_HDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `106`
- New: `108`

### Rust Evidence

- Graph edges: `1`

## W-000859 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_VXLAN_VNI_NOT_FOUND
- Explanation: skb_drop_reason_SKB_DROP_REASON_VXLAN_VNI_NOT_FOUND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `107`
- New: `109`

### Rust Evidence

- Graph edges: `1`

## W-000860 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: skb_drop_reason_SKB_DROP_REASON_XDP
- Explanation: skb_drop_reason_SKB_DROP_REASON_XDP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `69`
- New: `71`

### Rust Evidence

- Graph edges: `1`

## W-000861 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: xfeature_XFEATURE_MAX
- Explanation: xfeature_XFEATURE_MAX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `20`

### Rust Evidence

- Graph edges: `1`

## W-000862 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: zone_stat_item_NR_FREE_CMA_PAGES
- Explanation: zone_stat_item_NR_FREE_CMA_PAGES changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `9`

### Rust Evidence

- Graph edges: `1`

## W-000863 MacroConstDrift

- Risk: Medium
- Score: 7.8
- Symbol: zone_stat_item_NR_VM_ZONE_STAT_ITEMS
- Explanation: zone_stat_item_NR_VM_ZONE_STAT_ITEMS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `10`

### Rust Evidence

- Graph edges: `1`

## W-000864 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: ACPI_CA_VERSION
- Explanation: ACPI_CA_VERSION changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x20240827`
- New: `0x20250404`

### Rust Evidence

- Graph edges: `0`

## W-000865 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: ACPI_COPY_NAMESEG
- Explanation: ACPI_COPY_NAMESEG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(strncpy (ACPI_CAST_PTR (char, (dest)), ACPI_CAST_PTR (char, (src)), ACPI_NAMESEG_SIZE))`
- New: `(memcpy (ACPI_CAST_PTR (char, (dest)), ACPI_CAST_PTR (char, (src)), ACPI_NAMESEG_SIZE))`

### Rust Evidence

- Graph edges: `0`

## W-000866 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: ACPI_VALIDATE_RSDP_SIG
- Explanation: ACPI_VALIDATE_RSDP_SIG changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(!strncmp (ACPI_CAST_PTR (char, (a)), ACPI_SIG_RSDP, 8))`
- New: `(!strncmp (ACPI_CAST_PTR (char, (a)), ACPI_SIG_RSDP, (sizeof(a) < 8) ? ACPI_NAMESEG_SIZE : 8))`

### Rust Evidence

- Graph edges: `0`

## W-000867 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: BLK_MAX_BLOCK_SIZE
- Explanation: BLK_MAX_BLOCK_SIZE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `SZ_64K`
- New: `PAGE_SIZE`

### Rust Evidence

- Graph edges: `0`

## W-000868 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CHACHA_STATE_WORDS
- Explanation: CHACHA_STATE_WORDS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(CHACHA_BLOCK_SIZE / sizeof(u32))`
- New: `16`

### Rust Evidence

- Graph edges: `0`

## W-000869 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_ACODEC
- Explanation: CLKID_ACODEC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `206`
- New: `180`

### Rust Evidence

- Graph edges: `0`

## W-000870 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_ADC
- Explanation: CLKID_ADC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `45`
- New: `41`

### Rust Evidence

- Graph edges: `0`

## W-000871 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AHB_ARB0
- Explanation: CLKID_AHB_ARB0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `57`
- New: `49`

### Rust Evidence

- Graph edges: `0`

## W-000872 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AHB_CTRL_BUS
- Explanation: CLKID_AHB_CTRL_BUS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `61`
- New: `51`

### Rust Evidence

- Graph edges: `0`

## W-000873 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AHB_DATA_BUS
- Explanation: CLKID_AHB_DATA_BUS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `60`
- New: `50`

### Rust Evidence

- Graph edges: `0`

## W-000874 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_AHB_BUS
- Explanation: CLKID_AO_AHB_BUS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `91`
- New: `56`

### Rust Evidence

- Graph edges: `0`

## W-000875 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_AHB_SRAM
- Explanation: CLKID_AO_AHB_SRAM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `90`
- New: `11`

### Rust Evidence

- Graph edges: `0`

## W-000876 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_I2C
- Explanation: CLKID_AO_I2C changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `93`
- New: `58`

### Rust Evidence

- Graph edges: `0`

## W-000877 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_IFACE
- Explanation: CLKID_AO_IFACE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `92`
- New: `57`

### Rust Evidence

- Graph edges: `0`

## W-000878 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_AO_MEDIA_CPU
- Explanation: CLKID_AO_MEDIA_CPU changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `89`
- New: `54`

### Rust Evidence

- Graph edges: `0`

## W-000879 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_ASSIST_MISC
- Explanation: CLKID_ASSIST_MISC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `33`
- New: `32`

### Rust Evidence

- Graph edges: `0`

## W-000880 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_BOOT_ROM
- Explanation: CLKID_BOOT_ROM changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `59`
- New: `45`

### Rust Evidence

- Graph edges: `0`

## W-000881 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CLK81
- Explanation: CLKID_CLK81 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `12`
- New: `10`

### Rust Evidence

- Graph edges: `0`

## W-000882 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CTS_ENCI
- Explanation: CLKID_CTS_ENCI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `199`
- New: `162`

### Rust Evidence

- Graph edges: `0`

## W-000883 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CTS_ENCI_SEL
- Explanation: CLKID_CTS_ENCI_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `195`
- New: `158`

### Rust Evidence

- Graph edges: `0`

## W-000884 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CTS_ENCP
- Explanation: CLKID_CTS_ENCP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `200`
- New: `163`

### Rust Evidence

- Graph edges: `0`

## W-000885 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CTS_ENCP_SEL
- Explanation: CLKID_CTS_ENCP_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `196`
- New: `159`

### Rust Evidence

- Graph edges: `0`

## W-000886 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CTS_VDAC
- Explanation: CLKID_CTS_VDAC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `201`
- New: `164`

### Rust Evidence

- Graph edges: `0`

## W-000887 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_CTS_VDAC_SEL
- Explanation: CLKID_CTS_VDAC_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `197`
- New: `160`

### Rust Evidence

- Graph edges: `0`

## W-000888 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_DAC_CLK
- Explanation: CLKID_DAC_CLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `79`
- New: `89`

### Rust Evidence

- Graph edges: `0`

## W-000889 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_DDR
- Explanation: CLKID_DDR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `16`
- New: `15`

### Rust Evidence

- Graph edges: `0`

## W-000890 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_DEMUX
- Explanation: CLKID_DEMUX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `37`
- New: `39`

### Rust Evidence

- Graph edges: `0`

## W-000891 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_DOS
- Explanation: CLKID_DOS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `17`
- New: `16`

### Rust Evidence

- Graph edges: `0`

## W-000892 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_EFUSE
- Explanation: CLKID_EFUSE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `58`
- New: `106`

### Rust Evidence

- Graph edges: `0`

## W-000893 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_ENC480P
- Explanation: CLKID_ENC480P changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `82`
- New: `92`

### Rust Evidence

- Graph edges: `0`

## W-000894 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_ETH
- Explanation: CLKID_ETH changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `36`
- New: `38`

### Rust Evidence

- Graph edges: `0`

## W-000895 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV2
- Explanation: CLKID_FCLK_DIV2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `4`
- New: `2`

### Rust Evidence

- Graph edges: `0`

## W-000896 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV2_DIV
- Explanation: CLKID_FCLK_DIV2_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `146`
- New: `75`

### Rust Evidence

- Graph edges: `0`

## W-000897 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV3
- Explanation: CLKID_FCLK_DIV3 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `5`
- New: `3`

### Rust Evidence

- Graph edges: `0`

## W-000898 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV3_DIV
- Explanation: CLKID_FCLK_DIV3_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `147`
- New: `76`

### Rust Evidence

- Graph edges: `0`

## W-000899 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV4
- Explanation: CLKID_FCLK_DIV4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `6`
- New: `4`

### Rust Evidence

- Graph edges: `0`

## W-000900 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV4_DIV
- Explanation: CLKID_FCLK_DIV4_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `148`
- New: `77`

### Rust Evidence

- Graph edges: `0`

## W-000901 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV5
- Explanation: CLKID_FCLK_DIV5 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `7`
- New: `5`

### Rust Evidence

- Graph edges: `0`

## W-000902 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV5_DIV
- Explanation: CLKID_FCLK_DIV5_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `149`
- New: `78`

### Rust Evidence

- Graph edges: `0`

## W-000903 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV7
- Explanation: CLKID_FCLK_DIV7 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `8`
- New: `6`

### Rust Evidence

- Graph edges: `0`

## W-000904 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FCLK_DIV7_DIV
- Explanation: CLKID_FCLK_DIV7_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `150`
- New: `79`

### Rust Evidence

- Graph edges: `0`

## W-000905 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FIXED_PLL
- Explanation: CLKID_FIXED_PLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `3`
- New: `1`

### Rust Evidence

- Graph edges: `0`

## W-000906 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_FIXED_PLL_DCO
- Explanation: CLKID_FIXED_PLL_DCO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `160`
- New: `101`

### Rust Evidence

- Graph edges: `0`

## W-000907 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_G2D
- Explanation: CLKID_G2D changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `49`
- New: `43`

### Rust Evidence

- Graph edges: `0`

## W-000908 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_GEN_CLK
- Explanation: CLKID_GEN_CLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `159`
- New: `84`

### Rust Evidence

- Graph edges: `0`

## W-000909 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_GEN_CLK_DIV
- Explanation: CLKID_GEN_CLK_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `158`
- New: `83`

### Rust Evidence

- Graph edges: `0`

## W-000910 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_GEN_CLK_SEL
- Explanation: CLKID_GEN_CLK_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `157`
- New: `82`

### Rust Evidence

- Graph edges: `0`

## W-000911 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_GP0_PLL
- Explanation: CLKID_GP0_PLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `9`
- New: `7`

### Rust Evidence

- Graph edges: `0`

## W-000912 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_GP0_PLL_DCO
- Explanation: CLKID_GP0_PLL_DCO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `165`
- New: `103`

### Rust Evidence

- Graph edges: `0`

## W-000913 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI
- Explanation: CLKID_HDMI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `205`
- New: `168`

### Rust Evidence

- Graph edges: `0`

## W-000914 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_DIV
- Explanation: CLKID_HDMI_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `204`
- New: `167`

### Rust Evidence

- Graph edges: `0`

## W-000915 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_PLL
- Explanation: CLKID_HDMI_PLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `2`
- New: `128`

### Rust Evidence

- Graph edges: `0`

## W-000916 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_PLL_DCO
- Explanation: CLKID_HDMI_PLL_DCO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `161`
- New: `125`

### Rust Evidence

- Graph edges: `0`

## W-000917 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_PLL_OD
- Explanation: CLKID_HDMI_PLL_OD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `162`
- New: `126`

### Rust Evidence

- Graph edges: `0`

## W-000918 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_PLL_OD2
- Explanation: CLKID_HDMI_PLL_OD2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `163`
- New: `127`

### Rust Evidence

- Graph edges: `0`

## W-000919 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_SEL
- Explanation: CLKID_HDMI_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `203`
- New: `166`

### Rust Evidence

- Graph edges: `0`

## W-000920 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_TX
- Explanation: CLKID_HDMI_TX changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `202`
- New: `165`

### Rust Evidence

- Graph edges: `0`

## W-000921 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HDMI_TX_SEL
- Explanation: CLKID_HDMI_TX_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `198`
- New: `161`

### Rust Evidence

- Graph edges: `0`

## W-000922 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_HIU_IFACE
- Explanation: CLKID_HIU_IFACE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `32`
- New: `30`

### Rust Evidence

- Graph edges: `0`

## W-000923 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_I2C
- Explanation: CLKID_I2C changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `22`
- New: `24`

### Rust Evidence

- Graph edges: `0`

## W-000924 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_IEC958
- Explanation: CLKID_IEC958 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `39`
- New: `91`

### Rust Evidence

- Graph edges: `0`

## W-000925 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_ISA
- Explanation: CLKID_ISA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `18`
- New: `20`

### Rust Evidence

- Graph edges: `0`

## W-000926 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI
- Explanation: CLKID_MALI changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `106`
- New: `175`

### Rust Evidence

- Graph edges: `0`

## W-000927 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_0
- Explanation: CLKID_MALI_0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `102`
- New: `171`

### Rust Evidence

- Graph edges: `0`

## W-000928 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_0_DIV
- Explanation: CLKID_MALI_0_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `101`
- New: `170`

### Rust Evidence

- Graph edges: `0`

## W-000929 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_0_SEL
- Explanation: CLKID_MALI_0_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `100`
- New: `169`

### Rust Evidence

- Graph edges: `0`

## W-000930 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_1
- Explanation: CLKID_MALI_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `105`
- New: `174`

### Rust Evidence

- Graph edges: `0`

## W-000931 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_1_DIV
- Explanation: CLKID_MALI_1_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `104`
- New: `173`

### Rust Evidence

- Graph edges: `0`

## W-000932 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MALI_1_SEL
- Explanation: CLKID_MALI_1_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `103`
- New: `172`

### Rust Evidence

- Graph edges: `0`

## W-000933 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MMC_PCLK
- Explanation: CLKID_MMC_PCLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `66`
- New: `56`

### Rust Evidence

- Graph edges: `0`

## W-000934 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MPEG_DIV
- Explanation: CLKID_MPEG_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `11`
- New: `9`

### Rust Evidence

- Graph edges: `0`

## W-000935 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MPEG_SEL
- Explanation: CLKID_MPEG_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `10`
- New: `8`

### Rust Evidence

- Graph edges: `0`

## W-000936 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MPLL0
- Explanation: CLKID_MPLL0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `13`
- New: `11`

### Rust Evidence

- Graph edges: `0`

## W-000937 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MPLL0_DIV
- Explanation: CLKID_MPLL0_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `142`
- New: `69`

### Rust Evidence

- Graph edges: `0`

## W-000938 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MPLL1
- Explanation: CLKID_MPLL1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `14`
- New: `12`

### Rust Evidence

- Graph edges: `0`

## W-000939 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MPLL1_DIV
- Explanation: CLKID_MPLL1_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `143`
- New: `70`

### Rust Evidence

- Graph edges: `0`

## W-000940 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MPLL2
- Explanation: CLKID_MPLL2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `15`
- New: `13`

### Rust Evidence

- Graph edges: `0`

## W-000941 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MPLL2_DIV
- Explanation: CLKID_MPLL2_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `144`
- New: `71`

### Rust Evidence

- Graph edges: `0`

## W-000942 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_MPLL_PREDIV
- Explanation: CLKID_MPLL_PREDIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `145`
- New: `73`

### Rust Evidence

- Graph edges: `0`

## W-000943 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_NAND
- Explanation: CLKID_NAND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `53`
- New: `178`

### Rust Evidence

- Graph edges: `0`

## W-000944 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PERIPHS
- Explanation: CLKID_PERIPHS changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `20`
- New: `22`

### Rust Evidence

- Graph edges: `0`

## W-000945 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_PL301
- Explanation: CLKID_PL301 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `19`
- New: `21`

### Rust Evidence

- Graph edges: `0`

## W-000946 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_RESET
- Explanation: CLKID_RESET changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `52`
- New: `44`

### Rust Evidence

- Graph edges: `0`

## W-000947 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_RNG0
- Explanation: CLKID_RNG0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `25`
- New: `27`

### Rust Evidence

- Graph edges: `0`

## W-000948 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_RNG1
- Explanation: CLKID_RNG1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `83`
- New: `93`

### Rust Evidence

- Graph edges: `0`

## W-000949 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SANA
- Explanation: CLKID_SANA changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `69`
- New: `25`

### Rust Evidence

- Graph edges: `0`

## W-000950 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SAR_ADC
- Explanation: CLKID_SAR_ADC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `23`
- New: `212`

### Rust Evidence

- Graph edges: `0`

## W-000951 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SDIO
- Explanation: CLKID_SDIO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `30`
- New: `22`

### Rust Evidence

- Graph edges: `0`

## W-000952 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_A
- Explanation: CLKID_SD_EMMC_A changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `94`
- New: `33`

### Rust Evidence

- Graph edges: `0`

## W-000953 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_A_CLK0
- Explanation: CLKID_SD_EMMC_A_CLK0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `119`
- New: `60`

### Rust Evidence

- Graph edges: `0`

## W-000954 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_A_CLK0_DIV
- Explanation: CLKID_SD_EMMC_A_CLK0_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `118`
- New: `64`

### Rust Evidence

- Graph edges: `0`

## W-000955 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_A_CLK0_SEL
- Explanation: CLKID_SD_EMMC_A_CLK0_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `117`
- New: `63`

### Rust Evidence

- Graph edges: `0`

## W-000956 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_B
- Explanation: CLKID_SD_EMMC_B changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `95`
- New: `34`

### Rust Evidence

- Graph edges: `0`

## W-000957 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_B_CLK0
- Explanation: CLKID_SD_EMMC_B_CLK0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `122`
- New: `61`

### Rust Evidence

- Graph edges: `0`

## W-000958 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_B_CLK0_DIV
- Explanation: CLKID_SD_EMMC_B_CLK0_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `121`
- New: `66`

### Rust Evidence

- Graph edges: `0`

## W-000959 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_B_CLK0_SEL
- Explanation: CLKID_SD_EMMC_B_CLK0_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `120`
- New: `65`

### Rust Evidence

- Graph edges: `0`

## W-000960 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_C
- Explanation: CLKID_SD_EMMC_C changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `96`
- New: `35`

### Rust Evidence

- Graph edges: `0`

## W-000961 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_C_CLK0
- Explanation: CLKID_SD_EMMC_C_CLK0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `125`
- New: `62`

### Rust Evidence

- Graph edges: `0`

## W-000962 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_C_CLK0_DIV
- Explanation: CLKID_SD_EMMC_C_CLK0_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `124`
- New: `68`

### Rust Evidence

- Graph edges: `0`

## W-000963 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SD_EMMC_C_CLK0_SEL
- Explanation: CLKID_SD_EMMC_C_CLK0_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `123`
- New: `67`

### Rust Evidence

- Graph edges: `0`

## W-000964 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SEC_AHB_AHB3_BRIDGE
- Explanation: CLKID_SEC_AHB_AHB3_BRIDGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `71`
- New: `52`

### Rust Evidence

- Graph edges: `0`

## W-000965 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SPICC
- Explanation: CLKID_SPICC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `21`
- New: `82`

### Rust Evidence

- Graph edges: `0`

## W-000966 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_SYS_PLL_DCO
- Explanation: CLKID_SYS_PLL_DCO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `164`
- New: `102`

### Rust Evidence

- Graph edges: `0`

## W-000967 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_UART0
- Explanation: CLKID_UART0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `26`
- New: `28`

### Rust Evidence

- Graph edges: `0`

## W-000968 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_UART1
- Explanation: CLKID_UART1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `48`
- New: `42`

### Rust Evidence

- Graph edges: `0`

## W-000969 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_UART2
- Explanation: CLKID_UART2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `68`
- New: `57`

### Rust Evidence

- Graph edges: `0`

## W-000970 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_USB
- Explanation: CLKID_USB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `55`
- New: `47`

### Rust Evidence

- Graph edges: `0`

## W-000971 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_USB0
- Explanation: CLKID_USB0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `50`
- New: `17`

### Rust Evidence

- Graph edges: `0`

## W-000972 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_USB0_DDR_BRIDGE
- Explanation: CLKID_USB0_DDR_BRIDGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `65`
- New: `49`

### Rust Evidence

- Graph edges: `0`

## W-000973 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_USB1
- Explanation: CLKID_USB1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `51`
- New: `18`

### Rust Evidence

- Graph edges: `0`

## W-000974 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_USB1_DDR_BRIDGE
- Explanation: CLKID_USB1_DDR_BRIDGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `64`
- New: `55`

### Rust Evidence

- Graph edges: `0`

## W-000975 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VAPB
- Explanation: CLKID_VAPB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `140`
- New: `124`

### Rust Evidence

- Graph edges: `0`

## W-000976 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VAPB_0
- Explanation: CLKID_VAPB_0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `135`
- New: `119`

### Rust Evidence

- Graph edges: `0`

## W-000977 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VAPB_0_DIV
- Explanation: CLKID_VAPB_0_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `134`
- New: `118`

### Rust Evidence

- Graph edges: `0`

## W-000978 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VAPB_0_SEL
- Explanation: CLKID_VAPB_0_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `133`
- New: `117`

### Rust Evidence

- Graph edges: `0`

## W-000979 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VAPB_1
- Explanation: CLKID_VAPB_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `138`
- New: `122`

### Rust Evidence

- Graph edges: `0`

## W-000980 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VAPB_1_DIV
- Explanation: CLKID_VAPB_1_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `137`
- New: `121`

### Rust Evidence

- Graph edges: `0`

## W-000981 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VAPB_1_SEL
- Explanation: CLKID_VAPB_1_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `136`
- New: `120`

### Rust Evidence

- Graph edges: `0`

## W-000982 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VAPB_SEL
- Explanation: CLKID_VAPB_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `139`
- New: `123`

### Rust Evidence

- Graph edges: `0`

## W-000983 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK
- Explanation: CLKID_VCLK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `175`
- New: `138`

### Rust Evidence

- Graph edges: `0`

## W-000984 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2
- Explanation: CLKID_VCLK2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `176`
- New: `139`

### Rust Evidence

- Graph edges: `0`

## W-000985 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV
- Explanation: CLKID_VCLK2_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `174`
- New: `137`

### Rust Evidence

- Graph edges: `0`

## W-000986 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV1
- Explanation: CLKID_VCLK2_DIV1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `190`
- New: `153`

### Rust Evidence

- Graph edges: `0`

## W-000987 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV12
- Explanation: CLKID_VCLK2_DIV12 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `194`
- New: `157`

### Rust Evidence

- Graph edges: `0`

## W-000988 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV12_EN
- Explanation: CLKID_VCLK2_DIV12_EN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `184`
- New: `147`

### Rust Evidence

- Graph edges: `0`

## W-000989 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV2
- Explanation: CLKID_VCLK2_DIV2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `191`
- New: `154`

### Rust Evidence

- Graph edges: `0`

## W-000990 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV2_EN
- Explanation: CLKID_VCLK2_DIV2_EN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `181`
- New: `144`

### Rust Evidence

- Graph edges: `0`

## W-000991 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV4
- Explanation: CLKID_VCLK2_DIV4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `192`
- New: `155`

### Rust Evidence

- Graph edges: `0`

## W-000992 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV4_EN
- Explanation: CLKID_VCLK2_DIV4_EN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `182`
- New: `145`

### Rust Evidence

- Graph edges: `0`

## W-000993 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV6
- Explanation: CLKID_VCLK2_DIV6 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `193`
- New: `156`

### Rust Evidence

- Graph edges: `0`

## W-000994 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_DIV6_EN
- Explanation: CLKID_VCLK2_DIV6_EN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `183`
- New: `146`

### Rust Evidence

- Graph edges: `0`

## W-000995 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_INPUT
- Explanation: CLKID_VCLK2_INPUT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `172`
- New: `135`

### Rust Evidence

- Graph edges: `0`

## W-000996 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_SEL
- Explanation: CLKID_VCLK2_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `170`
- New: `133`

### Rust Evidence

- Graph edges: `0`

## W-000997 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_VENCI0
- Explanation: CLKID_VCLK2_VENCI0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `73`
- New: `80`

### Rust Evidence

- Graph edges: `0`

## W-000998 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_VENCI1
- Explanation: CLKID_VCLK2_VENCI1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `74`
- New: `81`

### Rust Evidence

- Graph edges: `0`

## W-000999 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_VENCL
- Explanation: CLKID_VCLK2_VENCL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `86`
- New: `97`

### Rust Evidence

- Graph edges: `0`

## W-001000 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_VENCP0
- Explanation: CLKID_VCLK2_VENCP0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `75`
- New: `82`

### Rust Evidence

- Graph edges: `0`

## W-001001 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK2_VENCP1
- Explanation: CLKID_VCLK2_VENCP1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `76`
- New: `83`

### Rust Evidence

- Graph edges: `0`

## W-001002 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV
- Explanation: CLKID_VCLK_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `173`
- New: `136`

### Rust Evidence

- Graph edges: `0`

## W-001003 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV1
- Explanation: CLKID_VCLK_DIV1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `185`
- New: `148`

### Rust Evidence

- Graph edges: `0`

## W-001004 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV12
- Explanation: CLKID_VCLK_DIV12 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `189`
- New: `152`

### Rust Evidence

- Graph edges: `0`

## W-001005 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV12_EN
- Explanation: CLKID_VCLK_DIV12_EN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `180`
- New: `143`

### Rust Evidence

- Graph edges: `0`

## W-001006 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV2
- Explanation: CLKID_VCLK_DIV2 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `186`
- New: `149`

### Rust Evidence

- Graph edges: `0`

## W-001007 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV2_EN
- Explanation: CLKID_VCLK_DIV2_EN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `177`
- New: `140`

### Rust Evidence

- Graph edges: `0`

## W-001008 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV4
- Explanation: CLKID_VCLK_DIV4 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `187`
- New: `150`

### Rust Evidence

- Graph edges: `0`

## W-001009 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV4_EN
- Explanation: CLKID_VCLK_DIV4_EN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `178`
- New: `141`

### Rust Evidence

- Graph edges: `0`

## W-001010 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV6
- Explanation: CLKID_VCLK_DIV6 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `188`
- New: `151`

### Rust Evidence

- Graph edges: `0`

## W-001011 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_DIV6_EN
- Explanation: CLKID_VCLK_DIV6_EN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `179`
- New: `142`

### Rust Evidence

- Graph edges: `0`

## W-001012 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_INPUT
- Explanation: CLKID_VCLK_INPUT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `171`
- New: `134`

### Rust Evidence

- Graph edges: `0`

## W-001013 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VCLK_SEL
- Explanation: CLKID_VCLK_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `169`
- New: `132`

### Rust Evidence

- Graph edges: `0`

## W-001014 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VDEC_1
- Explanation: CLKID_VDEC_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `153`
- New: `204`

### Rust Evidence

- Graph edges: `0`

## W-001015 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VDEC_1_DIV
- Explanation: CLKID_VDEC_1_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `152`
- New: `203`

### Rust Evidence

- Graph edges: `0`

## W-001016 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VDEC_1_SEL
- Explanation: CLKID_VDEC_1_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `151`
- New: `202`

### Rust Evidence

- Graph edges: `0`

## W-001017 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VDEC_HEVC
- Explanation: CLKID_VDEC_HEVC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `156`
- New: `207`

### Rust Evidence

- Graph edges: `0`

## W-001018 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VDEC_HEVC_DIV
- Explanation: CLKID_VDEC_HEVC_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `155`
- New: `206`

### Rust Evidence

- Graph edges: `0`

## W-001019 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VDEC_HEVC_SEL
- Explanation: CLKID_VDEC_HEVC_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `154`
- New: `205`

### Rust Evidence

- Graph edges: `0`

## W-001020 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VID_PLL
- Explanation: CLKID_VID_PLL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `166`
- New: `129`

### Rust Evidence

- Graph edges: `0`

## W-001021 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VID_PLL_DIV
- Explanation: CLKID_VID_PLL_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `168`
- New: `131`

### Rust Evidence

- Graph edges: `0`

## W-001022 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VID_PLL_SEL
- Explanation: CLKID_VID_PLL_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `167`
- New: `130`

### Rust Evidence

- Graph edges: `0`

## W-001023 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VPU
- Explanation: CLKID_VPU changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `132`
- New: `116`

### Rust Evidence

- Graph edges: `0`

## W-001024 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VPU_0
- Explanation: CLKID_VPU_0 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `128`
- New: `112`

### Rust Evidence

- Graph edges: `0`

## W-001025 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VPU_0_DIV
- Explanation: CLKID_VPU_0_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `127`
- New: `111`

### Rust Evidence

- Graph edges: `0`

## W-001026 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VPU_0_SEL
- Explanation: CLKID_VPU_0_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `126`
- New: `110`

### Rust Evidence

- Graph edges: `0`

## W-001027 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VPU_1
- Explanation: CLKID_VPU_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `131`
- New: `115`

### Rust Evidence

- Graph edges: `0`

## W-001028 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VPU_1_DIV
- Explanation: CLKID_VPU_1_DIV changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `130`
- New: `114`

### Rust Evidence

- Graph edges: `0`

## W-001029 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VPU_1_SEL
- Explanation: CLKID_VPU_1_SEL changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `129`
- New: `113`

### Rust Evidence

- Graph edges: `0`

## W-001030 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: CLKID_VPU_INTR
- Explanation: CLKID_VPU_INTR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `70`
- New: `58`

### Rust Evidence

- Graph edges: `0`

## W-001031 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: DATA_MAIN
- Explanation: DATA_MAIN changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `.data`
- New: `.data .data.rel .data.rel.local`

### Rust Evidence

- Graph edges: `0`

## W-001032 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: FOP_DONTCACHE
- Explanation: FOP_DONTCACHE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0 /* ((__force fop_flags_t)(1 << 7)) */`
- New: `((__force fop_flags_t)(1 << 7))`

### Rust Evidence

- Graph edges: `0`

## W-001033 MacroConstDrift

- Risk: Medium
- Score: 6.6
- Symbol: TRACE_EVENT_FN_COND
- Explanation: TRACE_EVENT_FN_COND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `(name, proto, args, cond, struct,		\`
- New: `(name, proto, args, cond, struct,	\`

### Rust Evidence

- Graph edges: `0`
