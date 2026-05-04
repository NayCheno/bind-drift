# BindDrift Ranked Warnings

## W-000053 NullabilityDrift

- Risk: High
- Score: 15.7
- Symbol: rb_first
- Explanation: rb_first has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/rbtree.h:61 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:206 `RBTree<K::iter` unsafe=0
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:209 `RBTree<K::iter` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:221 `RBTree<K::iter_mut` unsafe=0
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:224 `RBTree<K::iter_mut` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:249 `RBTree<K::cursor_front_mut` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:208 `// SAFETY: by the invariants, all pointers are valid.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:223 `// SAFETY: by the invariants, all pointers are valid.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:245 `/// Returns a cursor over the tree nodes, starting with the smallest key.`

## W-000031 NullabilityDrift

- Risk: High
- Score: 14.0
- Symbol: dma_alloc_attrs
- Explanation: dma_alloc_attrs has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/dma-mapping.h:266 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/dma.rs:722 `None` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/dma.rs:839 `Coherent<T>::zeroed` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/dma.rs:1063 `None` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/dma.rs:720 `// SAFETY: Device pointer is guaranteed as valid by the type invariant on `Device`.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/dma.rs:837 `// SAFETY: Device pointer is guaranteed as valid by the type invariant on `Device`.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/dma.rs:1061 `// SAFETY: `dev.as_raw()` is valid by the type invariant on `device::Device`.`

## W-000003 AllocationFreePairingDrift

- Risk: High
- Score: 13.7
- Symbol: auxiliary_device_uninit
- Explanation: auxiliary_device_uninit has FREE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['FREE', 'REFCOUNT_PUT']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/auxiliary_bus.h:241 `mutex_destroy(&auxdev->sysfs.lock);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:377 `None` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:404 `drop` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:375 `// SAFETY: `adev` is guaranteed to be a valid pointer to a`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:402 `// SAFETY: By the type invariant of `Self`, `self.0.as_ptr()` is a valid registered`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:408 `// SAFETY: A `Registration` of a `struct auxiliary_device` can be released from any thread.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:402 `AS_PTR`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:404 `AS_PTR`

## W-000004 OwnershipRefcountDrift

- Risk: High
- Score: 13.7
- Symbol: auxiliary_device_uninit
- Explanation: auxiliary_device_uninit has REFCOUNT_PUT C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['FREE', 'REFCOUNT_PUT']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/auxiliary_bus.h:242 `put_device(&auxdev->dev);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:377 `None` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:404 `drop` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:375 `// SAFETY: `adev` is guaranteed to be a valid pointer to a`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:402 `// SAFETY: By the type invariant of `Self`, `self.0.as_ptr()` is a valid registered`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:408 `// SAFETY: A `Registration` of a `struct auxiliary_device` can be released from any thread.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:402 `AS_PTR`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/auxiliary.rs:404 `AS_PTR`

## W-000039 NullabilityDrift

- Risk: High
- Score: 13.7
- Symbol: kunit_get_current_test
- Explanation: kunit_get_current_test has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/kunit/test-bug.h:44 `return NULL;`
- /home/nya/workspace/bind-drift/vendor/linux/include/kunit/test-bug.h:65 `static inline struct kunit *kunit_get_current_test(void) { return NULL; }`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/kunit.rs:73 `info` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/kunit.rs:329 `TestResult::in_kunit_test` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/kunit.rs:72 `// SAFETY: FFI call without safety requirements.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/kunit.rs:324 `/// assert_eq!(mock_res, 100);`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/kunit.rs:325 `/// ````

## W-000040 NullabilityDrift

- Risk: High
- Score: 13.7
- Symbol: lock_vma_under_rcu
- Explanation: lock_vma_under_rcu has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/mmap_lock.h:517 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/mm.rs:179 `MmWithUser::lock_vma_under_rcu` unsafe=0
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/mm.rs:181 `MmWithUser::lock_vma_under_rcu` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/mm.rs:174 `/// When per-vma locks are disabled, this always returns `None`.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/mm.rs:179 `// SAFETY: Calling `bindings::lock_vma_under_rcu` is always okay given an mm where`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/mm.rs:184 `// SAFETY: If `lock_vma_under_rcu` returns a non-null ptr, then it points at a`

## W-000051 NullabilityDrift

- Risk: High
- Score: 13.7
- Symbol: pwmchip_alloc
- Explanation: pwmchip_alloc has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pwm.h:567 `return ERR_PTR(-EINVAL);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:581 `bound_parent_device` unsafe=0
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:594 `bound_parent_device` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:576 `// SAFETY: Per the function's safety contract, the parent device is bound.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:581 `/// Allocates and wraps a PWM chip using `bindings::pwmchip_alloc`.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:582 `///`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:583 `AREF`

## W-000054 NullabilityDrift

- Risk: High
- Score: 13.7
- Symbol: rb_last
- Explanation: rb_last has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/rbtree.h:76 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:279 `RBTree<K::cursor_back_mut` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:294 `RBTree<K::cursor_back` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:275 `/// Returns a cursor over the tree nodes, starting with the largest key.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:278 `// SAFETY: `self.root` is always a valid root node.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/rbtree.rs:290 `/// Returns a cursor over the tree nodes, starting with the largest key.`

## W-000016 NullabilityDrift

- Risk: High
- Score: 13.3
- Symbol: debugfs_create_dir
- Explanation: debugfs_create_dir has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/debugfs.h:301 `return ERR_PTR(-ENODEV);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/debugfs/entry.rs:46 `Entry<::dynamic_dir` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/debugfs/entry.rs:100 `Entry<::dir` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/debugfs/entry.rs:42 `// SAFETY: The invariants of this function's arguments ensure the safety of this call.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/debugfs/entry.rs:95 `// SAFETY: The invariants of this function's arguments ensure the safety of this call.`

## W-000011 OwnershipRefcountDrift

- Risk: High
- Score: 13.2
- Symbol: clk_put
- Explanation: clk_put has REFCOUNT_PUT C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['REFCOUNT_PUT']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/clk.h:1081 `static inline void clk_put(struct clk *clk) {}`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:257 `drop` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:256 `// SAFETY: By the type invariants, self.as_raw() is a valid argument for [`clk_put`].`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:261 `/// A reference-counted optional clock.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:262 `///`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:254 `IMPL_DROP`

## W-000013 NullabilityDrift

- Risk: High
- Score: 13.2
- Symbol: cpufreq_cpu_get
- Explanation: cpufreq_cpu_get has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/cpufreq.h:221 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/cpufreq.rs:685 `from_cpu` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/cpufreq.rs:684 `// SAFETY: It is safe to call `cpufreq_cpu_get` for any valid CPU.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/cpufreq.rs:688 `// SAFETY: The `ptr` is guaranteed to be valid and remains valid for the lifetime of`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/cpufreq.rs:683 `RESULT_RETURN`

## W-000014 OwnershipRefcountDrift

- Risk: High
- Score: 13.2
- Symbol: cpufreq_cpu_put
- Explanation: cpufreq_cpu_put has REFCOUNT_PUT C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['REFCOUNT_PUT']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/cpufreq.h:223 `static inline void cpufreq_cpu_put(struct cpufreq_policy *policy) { }`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/cpufreq.rs:712 `drop` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/cpufreq.rs:711 `// SAFETY: The underlying pointer is guaranteed to be valid for the lifetime of `self`.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/cpufreq.rs:716 `/// CPU frequency driver.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/cpufreq.rs:717 `///`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/cpufreq.rs:709 `IMPL_DROP`

## W-000030 NullabilityDrift

- Risk: High
- Score: 13.2
- Symbol: devm_platform_ioremap_resource
- Explanation: devm_platform_ioremap_resource has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/platform_device.h:86 `return IOMEM_ERR_PTR(-EINVAL);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/error.rs:470 `From<core::convert::Infallible>::to_result` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/error.rs:465 `///     pdev: &mut PlatformDevice,`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/error.rs:466 `///     index: u32,`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/error.rs:467 `/// ) -> Result<*mut kernel::ffi::c_void> {`

## W-000056 OwnershipRefcountDrift

- Risk: High
- Score: 13.2
- Symbol: refcount_dec
- Explanation: refcount_dec has REFCOUNT_PUT C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['REFCOUNT_PUT']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/refcount.h:476 `__refcount_dec(r, NULL);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:82 `Refcount::dec` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:77 `/// Provides release memory ordering, such that prior loads and stores are done`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:78 `/// before.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:81 `// SAFETY: `self.as_ptr()` is valid.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:81 `AS_PTR`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:82 `AS_PTR`

## W-000057 OwnershipRefcountDrift

- Risk: High
- Score: 13.2
- Symbol: refcount_dec_and_test
- Explanation: refcount_dec_and_test has REFCOUNT_PUT C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['REFCOUNT_PUT']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/refcount.h:450 `return __refcount_dec_and_test(r, NULL);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:106 `Refcount::dec_and_test` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:101 `/// <https://github.com/rust-lang/rust/issues/55005>.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:105 `// SAFETY: `self.as_ptr()` is valid.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:110 `// SAFETY: `refcount_t` is thread-safe.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:105 `AS_PTR`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:106 `AS_PTR`

## W-000058 OwnershipRefcountDrift

- Risk: High
- Score: 13.2
- Symbol: refcount_inc
- Explanation: refcount_inc has REFCOUNT_GET C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['REFCOUNT_GET']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/refcount.h:383 `__refcount_inc(r, NULL);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:70 `Refcount::inc` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:65 `/// Provides no memory ordering, it is assumed that caller already has a reference on the`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:66 `/// object.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:69 `// SAFETY: self is valid.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/refcount.rs:70 `AS_PTR`

## W-000059 NullabilityDrift

- Risk: High
- Score: 13.2
- Symbol: regulator_get
- Explanation: regulator_get has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/regulator/consumer.h:305 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/regulator.rs:276 `get_internal` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/regulator.rs:274 `// SAFETY: It is safe to call `regulator_get()`, on a device pointer`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/regulator.rs:272 `RESULT_RETURN`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/regulator.rs:276 `ERR_PTR_MAPPING`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/regulator.rs:276 `LIFETIME_NAMING_PATTERN`

## W-000002 NullabilityDrift

- Risk: High
- Score: 13.0
- Symbol: acpi_match_device
- Explanation: acpi_match_device has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/acpi.h:990 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/driver.rs:311 `acpi_id_info` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/driver.rs:308 `// SAFETY:`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/driver.rs:316 `// SAFETY: `DeviceId` is a `#[repr(transparent)]` wrapper of `struct acpi_device_id``
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/driver.rs:311 `AS_PTR`

## W-000005 NullabilityDrift

- Risk: High
- Score: 13.0
- Symbol: clk_get
- Explanation: clk_get has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/clk.h:980 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:151 `Clk::get` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:147 `// SAFETY: It is safe to call [`clk_get`] for a valid device pointer.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:150 `ERR_PTR_MAPPING`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:151 `LIFETIME_NAMING_PATTERN`

## W-000007 NullabilityDrift

- Risk: High
- Score: 13.0
- Symbol: clk_get_optional
- Explanation: clk_get_optional has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN', 'NULL_RETURN', 'REFCOUNT_GET']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/clk.h:1232 `if (clk == ERR_PTR(-ENOENT))`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:319 `OptionalClk::get` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:314 `// SAFETY: It is safe to call [`clk_get_optional`] for a valid device pointer.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:318 `ERR_PTR_MAPPING`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:319 `LIFETIME_NAMING_PATTERN`

## W-000008 NullabilityDrift

- Risk: High
- Score: 13.0
- Symbol: clk_get_optional
- Explanation: clk_get_optional has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN', 'NULL_RETURN', 'REFCOUNT_GET']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/clk.h:1233 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:319 `OptionalClk::get` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:314 `// SAFETY: It is safe to call [`clk_get_optional`] for a valid device pointer.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:318 `ERR_PTR_MAPPING`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:319 `LIFETIME_NAMING_PATTERN`

## W-000009 OwnershipRefcountDrift

- Risk: High
- Score: 13.0
- Symbol: clk_get_optional
- Explanation: clk_get_optional has REFCOUNT_GET C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN', 'NULL_RETURN', 'REFCOUNT_GET']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/clk.h:1230 `struct clk *clk = clk_get(dev, id);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:319 `OptionalClk::get` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:314 `// SAFETY: It is safe to call [`clk_get_optional`] for a valid device pointer.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:318 `ERR_PTR_MAPPING`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:319 `LIFETIME_NAMING_PATTERN`

## W-000028 OwnershipRefcountDrift

- Risk: High
- Score: 13.0
- Symbol: dev_pm_opp_put
- Explanation: dev_pm_opp_put has REFCOUNT_PUT C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['REFCOUNT_PUT']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pm_opp.h:388 `static inline void dev_pm_opp_put(struct dev_pm_opp *opp) {}`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:1052 `dec_ref` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:1051 `// SAFETY: The safety requirements guarantee that the refcount is nonzero.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:1057 `/// Creates an owned reference to a [`OPP`] from a valid pointer.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:1052 `AS_PTR`

## W-000033 OwnershipRefcountDrift

- Risk: High
- Score: 13.0
- Symbol: drm_gem_object_put
- Explanation: drm_gem_object_put has REFCOUNT_PUT C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['REFCOUNT_PUT']`
- /home/nya/workspace/bind-drift/vendor/linux/include/drm/drm_gem.h:578 `__drm_gem_object_put(obj);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/drm/gem/mod.rs:61 `dec_ref` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/drm/gem/mod.rs:57 `// SAFETY: `obj` is a valid pointer to an `Object<T>`.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/drm/gem/mod.rs:60 `// SAFETY: The safety requirements guarantee that the refcount is non-zero.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/drm/gem/mod.rs:61 `LIFETIME_NAMING_PATTERN`

## W-000034 NullabilityDrift

- Risk: High
- Score: 13.0
- Symbol: errname
- Explanation: errname has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/errname.h:12 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/error.rs:182 `Error::name` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/error.rs:178 `/// Returns a string representing the error, if one exists.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/error.rs:181 `// SAFETY: Just an FFI call, there are no extra safety requirements.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/error.rs:180 `OPTION_RETURN`

## W-000036 OwnershipRefcountDrift

- Risk: High
- Score: 13.0
- Symbol: get_task_struct
- Explanation: get_task_struct has REFCOUNT_GET C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['REFCOUNT_GET']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/sched/task.h:116 `refcount_inc(&t->usage);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/task.rs:354 `inc_ref` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/task.rs:349 `// SAFETY: The type invariants guarantee that `Task` is always refcounted.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/task.rs:353 `// SAFETY: The existence of a shared reference means that the refcount is nonzero.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/task.rs:354 `AS_PTR`

## W-000043 AllocationFreePairingDrift

- Risk: High
- Score: 13.0
- Symbol: mutex_destroy
- Explanation: mutex_destroy has FREE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['FREE']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/mutex.h:48 `static inline void mutex_destroy(struct mutex *lock) {}`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/configfs.rs:192 `drop` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/configfs.rs:189 `// SAFETY: We registered `self.subsystem` in the initializer returned by `Self::new`.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/configfs.rs:191 `// SAFETY: We initialized the mutex in `Subsystem::new`.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/configfs.rs:192 `LIFETIME_NAMING_PATTERN`

## W-000044 NullabilityDrift

- Risk: High
- Score: 13.0
- Symbol: of_match_device
- Explanation: of_match_device has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/of_device.h:69 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/driver.rs:345 `of_id_info` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/driver.rs:342 `// SAFETY:`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/driver.rs:350 `// SAFETY: `DeviceId` is a `#[repr(transparent)]` wrapper of `struct of_device_id``
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/driver.rs:345 `AS_PTR`

## W-000045 NullabilityDrift

- Risk: High
- Score: 13.0
- Symbol: pci_dev_get
- Explanation: pci_dev_get has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN', 'REFCOUNT_GET']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pci.h:2206 `static inline struct pci_dev *pci_dev_get(struct pci_dev *dev) { return NULL; }`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pci.rs:480 `inc_ref` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pci.rs:476 `// SAFETY: Instances of `Device` are always reference-counted.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pci.rs:479 `// SAFETY: The existence of a shared reference guarantees that the refcount is non-zero.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pci.rs:480 `LIFETIME_NAMING_PATTERN`

## W-000046 OwnershipRefcountDrift

- Risk: High
- Score: 13.0
- Symbol: pci_dev_get
- Explanation: pci_dev_get has REFCOUNT_GET C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN', 'REFCOUNT_GET']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pci.h:2206 `static inline struct pci_dev *pci_dev_get(struct pci_dev *dev) { return NULL; }`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pci.rs:480 `inc_ref` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pci.rs:476 `// SAFETY: Instances of `Device` are always reference-counted.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pci.rs:479 `// SAFETY: The existence of a shared reference guarantees that the refcount is non-zero.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pci.rs:480 `LIFETIME_NAMING_PATTERN`

## W-000055 AllocationFreePairingDrift

- Risk: High
- Score: 13.0
- Symbol: rcu_read_unlock
- Explanation: rcu_read_unlock has FREE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['FREE']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/rcupdate.h:869 `rcu_lock_release(&rcu_lock_map); /* Keep acq info for rls diags. */`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/rcu.rs:44 `drop` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/rcu.rs:43 `// SAFETY: By the type invariants, the RCU read side is locked, so it is ok to unlock it.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/rcu.rs:48 `/// Acquires the RCU read side lock.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/sync/rcu.rs:44 `LIFETIME_NAMING_PATTERN`

## W-000063 NullabilityDrift

- Risk: High
- Score: 13.0
- Symbol: sg_next
- Explanation: sg_next has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/scatterlist.h:110 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/scatterlist.rs:482 `next` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/scatterlist.rs:481 `// SAFETY: `entry.as_raw()` is a valid pointer to a `struct scatterlist`.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/scatterlist.rs:485 `// SAFETY: If `next` is not NULL, `sg_next()` guarantees to return a valid pointer to`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/scatterlist.rs:477 `OPTION_RETURN`

## W-000018 NullabilityDrift

- Risk: High
- Score: 12.8
- Symbol: dev_pm_opp_find_bw_floor
- Explanation: dev_pm_opp_find_bw_floor has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pm_opp.h:380 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:930 `Table::opp_from_bw` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:927 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:934 `// SAFETY: The `ptr` is guaranteed by the C code to be valid.`

## W-000021 NullabilityDrift

- Risk: High
- Score: 12.8
- Symbol: dev_pm_opp_find_freq_floor_indexed
- Explanation: dev_pm_opp_find_freq_floor_indexed has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pm_opp.h:338 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:879 `Table::set_opp` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:876 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:883 `// SAFETY: The `ptr` is guaranteed by the C code to be valid.`

## W-000023 NullabilityDrift

- Risk: High
- Score: 12.8
- Symbol: dev_pm_opp_find_level_exact
- Explanation: dev_pm_opp_find_level_exact has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pm_opp.h:356 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:894 `Table::opp_from_level` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:892 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:891 `ERR_PTR_MAPPING`

## W-000024 NullabilityDrift

- Risk: High
- Score: 12.8
- Symbol: dev_pm_opp_find_level_floor
- Explanation: dev_pm_opp_find_level_floor has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pm_opp.h:368 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:905 `Table::opp_from_level` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:902 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:909 `// SAFETY: The `ptr` is guaranteed by the C code to be valid.`

## W-000025 NullabilityDrift

- Risk: High
- Score: 12.8
- Symbol: dev_pm_opp_get_opp_table
- Explanation: dev_pm_opp_get_opp_table has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pm_opp.h:227 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:647 `Table::from_dev` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:642 `// SAFETY: The requirements are satisfied by the existence of the [`Device`] and its safety`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:647 `ERR_PTR_MAPPING`

## W-000032 OwnershipRefcountDrift

- Risk: High
- Score: 12.8
- Symbol: drm_gem_object_get
- Explanation: drm_gem_object_get has REFCOUNT_GET C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['REFCOUNT_GET']`
- /home/nya/workspace/bind-drift/vendor/linux/include/drm/drm_gem.h:558 `kref_get(&obj->refcount);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/drm/gem/mod.rs:53 `inc_ref` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/drm/gem/mod.rs:51 `// SAFETY: The existence of a shared reference guarantees that the refcount is`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/drm/gem/mod.rs:53 `LIFETIME_NAMING_PATTERN`

## W-000037 NullabilityDrift

- Risk: High
- Score: 12.8
- Symbol: i2c_verify_client
- Explanation: i2c_verify_client has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/i2c.h:493 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/i2c.rs:524 `try_from` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/i2c.rs:522 `// SAFETY: By the type invariant of `Device`, `dev.as_raw()` is a valid pointer to a`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/i2c.rs:521 `RESULT_RETURN`

## W-000038 NullabilityDrift

- Risk: High
- Score: 12.8
- Symbol: ioremap_np
- Explanation: ioremap_np has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/asm-generic/io.h:1198 `return NULL;`
- /home/nya/workspace/bind-drift/vendor/linux/include/asm-generic/iomap.h:89 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/io/mem.rs:257 `ioremap` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/io/mem.rs:254 `// SAFETY:`

## W-000047 NullabilityDrift

- Risk: High
- Score: 12.8
- Symbol: pci_iomap
- Explanation: pci_iomap has NULL_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['NULL_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/asm-generic/pci_iomap.h:37 `return NULL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pci/io.rs:178 `Bar<SIZE>::new` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pci/io.rs:174 `// SAFETY:`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pci/io.rs:178 `LIFETIME_NAMING_PATTERN`

## W-000049 OwnershipRefcountDrift

- Risk: High
- Score: 12.8
- Symbol: put_task_struct
- Explanation: put_task_struct has REFCOUNT_PUT C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['REFCOUNT_PUT']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/sched/task.h:130 `if (!refcount_dec_and_test(&t->usage))`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/task.rs:360 `dec_ref` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/task.rs:359 `// SAFETY: The safety requirements guarantee that the refcount is nonzero.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/task.rs:360 `AS_PTR`

## W-000064 OwnershipRefcountDrift

- Risk: High
- Score: 12.8
- Symbol: vma_end_read
- Explanation: vma_end_read has REFCOUNT_PUT C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['REFCOUNT_PUT']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/mmap_lock.h:264 `vma_refcount_put(vma);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/mm.rs:295 `drop` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/mm.rs:294 `// SAFETY: We hold the read lock by the type invariants.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/mm.rs:295 `AS_PTR`

## W-000017 NullabilityDrift

- Risk: High
- Score: 12.6
- Symbol: dev_pm_opp_find_bw_ceil
- Explanation: dev_pm_opp_find_bw_ceil has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pm_opp.h:374 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:924 `Table::opp_from_bw` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:921 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`

## W-000019 NullabilityDrift

- Risk: High
- Score: 12.6
- Symbol: dev_pm_opp_find_freq_ceil_indexed
- Explanation: dev_pm_opp_find_freq_ceil_indexed has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pm_opp.h:350 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:873 `Table::set_opp` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:870 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`

## W-000020 NullabilityDrift

- Risk: High
- Score: 12.6
- Symbol: dev_pm_opp_find_freq_exact_indexed
- Explanation: dev_pm_opp_find_freq_exact_indexed has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pm_opp.h:326 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:861 `Table::set_opp` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:857 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and`

## W-000022 NullabilityDrift

- Risk: High
- Score: 12.6
- Symbol: dev_pm_opp_find_level_ceil
- Explanation: dev_pm_opp_find_level_ceil has ERR_PTR_RETURN C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pm_opp.h:362 `return ERR_PTR(-EOPNOTSUPP);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:899 `Table::opp_from_level` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:896 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`

## W-000050 ErrorDrift

- Risk: High
- Score: 11.7
- Symbol: pwmchip_alloc
- Explanation: pwmchip_alloc has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pwm.h:567 `return ERR_PTR(-EINVAL);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:581 `bound_parent_device` unsafe=0
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:594 `bound_parent_device` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:576 `// SAFETY: Per the function's safety contract, the parent device is bound.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:581 `/// Allocates and wraps a PWM chip using `bindings::pwmchip_alloc`.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:582 `///`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:583 `AREF`

## W-000052 ErrorDrift

- Risk: High
- Score: 11.7
- Symbol: pwmchip_remove
- Explanation: pwmchip_remove has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pwm.h:584 `return -EINVAL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:714 `drop` unsafe=0
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:716 `drop` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:713 `// SAFETY: `chip_raw` points to a chip that was successfully registered.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:720 `/// Declares a kernel module that exposes a single PWM driver.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:721 `///`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:714 `LIFETIME_NAMING_PATTERN`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pwm.rs:716 `LIFETIME_NAMING_PATTERN`

## W-000035 ErrorDrift

- Risk: High
- Score: 11.45
- Symbol: firmware_request_nowarn
- Explanation: firmware_request_nowarn has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/firmware.h:142 `return -EINVAL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/firmware.rs:19 `None` unsafe=0
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/firmware.rs:35 `request_nowarn` unsafe=0
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/firmware.rs:92 `Firmware::request` unsafe=0
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/firmware.rs:39 `/// Abstraction around a C `struct firmware`.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/firmware.rs:40 `///`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/firmware.rs:91 `/// Send a request for an optional firmware module. See also`

## W-000015 ErrorDrift

- Risk: High
- Score: 11.3
- Symbol: debugfs_create_dir
- Explanation: debugfs_create_dir has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/debugfs.h:301 `return ERR_PTR(-ENODEV);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/debugfs/entry.rs:46 `Entry<::dynamic_dir` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/debugfs/entry.rs:100 `Entry<::dir` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/debugfs/entry.rs:42 `// SAFETY: The invariants of this function's arguments ensure the safety of this call.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/debugfs/entry.rs:95 `// SAFETY: The invariants of this function's arguments ensure the safety of this call.`

## W-000061 ErrorDrift

- Risk: High
- Score: 11.25
- Symbol: request_firmware
- Explanation: request_firmware has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/firmware.h:127 `return -EINVAL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/firmware.rs:19 `None` unsafe=0
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/firmware.rs:31 `request` unsafe=0
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/firmware.rs:86 `request_internal` unsafe=0
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/firmware.rs:81 `// SAFETY: `func` not bailing out with a non-zero error code, guarantees that `fw` is a`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/firmware.rs:86 `/// Send a firmware request and wait for it. See also `bindings::request_firmware`.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/firmware.rs:83 `NONNULL_MAPPING`

## W-000010 SleepabilityDrift

- Risk: High
- Score: 11.2
- Symbol: clk_prepare
- Explanation: clk_prepare has MAY_SLEEP C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['MAY_SLEEP']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/clk.h:367 `might_sleep();`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:194 `Clk::prepare` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:189 `/// [`clk_prepare`]: https://docs.kernel.org/core-api/kernel-api.html#c.clk_prepare`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:192 `// SAFETY: By the type invariants, self.as_raw() is a valid argument for`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:197 `/// Unprepare the clock.`

## W-000012 SleepabilityDrift

- Risk: High
- Score: 11.2
- Symbol: clk_unprepare
- Explanation: clk_unprepare has MAY_SLEEP C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['MAY_SLEEP']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/clk.h:373 `might_sleep();`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:206 `Clk::unprepare` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:201 `/// [`clk_unprepare`]: https://docs.kernel.org/core-api/kernel-api.html#c.clk_unprepare`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:204 `// SAFETY: By the type invariants, self.as_raw() is a valid argument for`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:209 `/// Prepare and enable the clock.`

## W-000029 ErrorDrift

- Risk: High
- Score: 11.2
- Symbol: devm_platform_ioremap_resource
- Explanation: devm_platform_ioremap_resource has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/platform_device.h:86 `return IOMEM_ERR_PTR(-EINVAL);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/error.rs:470 `From<core::convert::Infallible>::to_result` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/error.rs:465 `///     pdev: &mut PlatformDevice,`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/error.rs:466 `///     index: u32,`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/error.rs:467 `/// ) -> Result<*mut kernel::ffi::c_void> {`

## W-000048 ErrorDrift

- Risk: High
- Score: 11.2
- Symbol: pci_irq_vector
- Explanation: pci_irq_vector has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pci.h:1836 `return -EINVAL;`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pci.h:2227 `return -EINVAL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pci/irq.rs:106 `try_into` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pci/irq.rs:105 `// SAFETY: `self.as_raw` returns a valid pointer to a `struct pci_dev`.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pci/irq.rs:110 `// SAFETY: `irq` is guaranteed to be a valid IRQ number for `&self`.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/pci/irq.rs:104 `RESULT_RETURN`

## W-000060 ErrorDrift

- Risk: High
- Score: 11.2
- Symbol: regulator_get_voltage
- Explanation: regulator_get_voltage has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/regulator/consumer.h:504 `return -EINVAL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/regulator.rs:267 `Regulator<T>::get_voltage` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/regulator.rs:264 `/// Gets the current voltage of the regulator.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/regulator.rs:266 `// SAFETY: Safe as per the type invariants of `Regulator`.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/regulator.rs:265 `RESULT_RETURN`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/regulator.rs:267 `LIFETIME_NAMING_PATTERN`

## W-000006 ErrorDrift

- Risk: High
- Score: 11.0
- Symbol: clk_get_optional
- Explanation: clk_get_optional has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE', 'ERR_PTR_RETURN', 'NULL_RETURN', 'REFCOUNT_GET']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/clk.h:1232 `if (clk == ERR_PTR(-ENOENT))`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:319 `OptionalClk::get` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:314 `// SAFETY: It is safe to call [`clk_get_optional`] for a valid device pointer.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:318 `ERR_PTR_MAPPING`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/clk.rs:319 `LIFETIME_NAMING_PATTERN`

## W-000026 ErrorDrift

- Risk: High
- Score: 11.0
- Symbol: dev_pm_opp_get_sharing_cpus
- Explanation: dev_pm_opp_get_sharing_cpus has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pm_opp.h:479 `return -EINVAL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:767 `Table::sharing_cpus` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:762 `/// Gets sharing CPUs.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:765 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:767 `TO_RESULT_MAPPING`

## W-000027 ErrorDrift

- Risk: High
- Score: 11.0
- Symbol: dev_pm_opp_init_cpufreq_table
- Explanation: dev_pm_opp_init_cpufreq_table has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/pm_opp.h:503 `return -EINVAL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:46 `FreqTable::new` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:43 `// SAFETY: The requirements are satisfied by the existence of [`Device`] and its safety`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:45 `TO_RESULT_MAPPING`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/opp.rs:46 `LIFETIME_NAMING_PATTERN`

## W-000042 SleepabilityDrift

- Risk: High
- Score: 11.0
- Symbol: mmap_read_trylock
- Explanation: mmap_read_trylock has MAY_SLEEP C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['MAY_SLEEP']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/mmap_lock.h:611 `ret = down_read_trylock(&mm->mmap_lock) != 0;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/mm.rs:216 `MmWithUser::mmap_read_trylock` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/mm.rs:212 `/// Try to lock the mmap read lock.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/mm.rs:215 `// SAFETY: The pointer is valid since self is a reference.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/mm.rs:214 `OPTION_RETURN`

## W-000041 SleepabilityDrift

- Risk: High
- Score: 10.8
- Symbol: mmap_read_lock
- Explanation: mmap_read_lock has MAY_SLEEP C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['MAY_SLEEP']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/mmap_lock.h:592 `down_read(&mm->mmap_lock);`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/mm.rs:203 `MmWithUser::mmap_read_lock` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/mm.rs:199 `/// Lock the mmap read lock.`
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/mm.rs:202 `// SAFETY: The pointer is valid since self is a reference.`

## W-000001 SleepabilityDrift

- Risk: High
- Score: 10.6
- Symbol: __might_sleep
- Explanation: __might_sleep has MAY_SLEEP C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['MAY_SLEEP']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/kernel.h:132 `static inline void __might_sleep(const char *file, int line) { }`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/task.rs:430 `Eq::might_sleep` unsafe=1
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/task.rs:429 `AS_PTR`

## W-000062 ErrorDrift

- Risk: Medium
- Score: 9.85
- Symbol: request_firmware_direct
- Explanation: request_firmware_direct has ERROR_CODE C-side evidence and is used across a Rust unsafe boundary.
- Suggested action: Review the safe abstraction contract for stale error, ownership, allocation, or sleepability assumptions.

### C Evidence

- Old: `[]`
- New: `['ERROR_CODE']`
- /home/nya/workspace/bind-drift/vendor/linux/include/linux/firmware.h:168 `return -EINVAL;`

### Rust Evidence

- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/firmware.rs:20 `None` unsafe=0
- /home/nya/workspace/bind-drift/vendor/linux/rust/kernel/firmware.rs:17 `/// # Invariants`
