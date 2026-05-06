# BindDrift Ranked Warnings

## W-000018 SignatureDrift

- Risk: High
- Score: 17.0
- Symbol: security_secid_to_secctx
- Explanation: security_secid_to_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['u32 secid', 'char **secdata', 'u32 *seclen'], 'return_type': 'static inline int'}`
- New: `{'params': ['u32 secid', 'struct lsm_context *cp'], 'return_type': 'static inline int'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/security.rs:31 `SecurityCtx::from_secid` unsafe=1
- safe API `SecurityCtx::from_secid`
- vendor/linux/rust/kernel/security.rs:27 `// SAFETY: `struct lsm_context` can be initialized to all zeros.`
- vendor/linux/rust/kernel/security.rs:30 `// SAFETY: Just a C FFI call. The pointer is valid for writes.`
- vendor/linux/rust/kernel/security.rs:26 `RESULT_RETURN`
- vendor/linux/rust/kernel/security.rs:31 `TO_RESULT_MAPPING`

## W-000003 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: faux_device_create
- Explanation: faux_device_create changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/faux.rs:31 `Registration::new` unsafe=1
- safe API `Registration::new`
- vendor/linux/rust/kernel/faux.rs:26 `/// Create and register a new faux device with the given name.`
- vendor/linux/rust/kernel/faux.rs:28 `// SAFETY:`
- vendor/linux/rust/kernel/faux.rs:27 `RESULT_RETURN`
- weak lifetime name vendor/linux/rust/kernel/faux.rs:31 `LIFETIME_NAMING_PATTERN`
- wrapper_fix: `78418f300d3999f1cf8a9ac71065bf2eca61f4dd`

## W-000008 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: pci_enable_device_mem
- Explanation: pci_enable_device_mem changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/pci.rs:385 `Device::enable_device_mem` unsafe=1
- safe API `Device::enable_device_mem`
- vendor/linux/rust/kernel/pci.rs:382 `/// Enable memory resources for this device.`
- vendor/linux/rust/kernel/pci.rs:384 `// SAFETY: `self.as_raw` is guaranteed to be a pointer to a valid `struct pci_dev`.`
- vendor/linux/rust/kernel/pci.rs:383 `RESULT_RETURN`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000017 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: security_release_secctx
- Explanation: security_release_secctx changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['char *secdata', 'u32 seclen'], 'return_type': 'static inline void'}`
- New: `{'params': ['struct lsm_context *cp'], 'return_type': 'static inline void'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/security.rs:68 `drop` unsafe=1
- vendor/linux/rust/kernel/security.rs:65 `// SAFETY: By the invariant of `Self`, this frees a context that came from a successful`
- weak lifetime name vendor/linux/rust/kernel/security.rs:68 `LIFETIME_NAMING_PATTERN`

## W-000001 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: dev_set_drvdata
- Explanation: dev_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/device.rs:202 `Device<CoreInternal>::set_drvdata` unsafe=1
- safe API `Device<CoreInternal>::set_drvdata`
- vendor/linux/rust/kernel/device.rs:199 `/// Store a pointer to the bound driver's private data.`
- vendor/linux/rust/kernel/device.rs:201 `// SAFETY: By the type invariants, `self.as_raw()` is a valid pointer to a `struct device`.`
- vendor/linux/rust/kernel/device.rs:205 `/// Take ownership of the private data stored in this [`Device`].`
- vendor/linux/rust/kernel/device.rs:200 `FOREIGN_OWNABLE`
- wrapper_fix: `0242623384c767b1156b61b67894b4ecf6682b8b`

## W-000007 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: regulator_get_voltage
- Explanation: regulator_get_voltage changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/regulator.rs:269 `Regulator<T>::get_voltage` unsafe=1
- safe API `Regulator<T>::get_voltage`
- vendor/linux/rust/kernel/regulator.rs:266 `/// Gets the current voltage of the regulator.`
- vendor/linux/rust/kernel/regulator.rs:268 `// SAFETY: Safe as per the type invariants of `Regulator`.`
- vendor/linux/rust/kernel/regulator.rs:267 `RESULT_RETURN`
- vendor/linux/rust/kernel/regulator.rs:269 `AS_PTR`
- wrapper_fix: `8121353a4bf8e38afee26299419a78ec108e14a6`

## W-000008 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: regulator_is_enabled
- Explanation: regulator_is_enabled changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/regulator.rs:383 `Regulator<T>::is_enabled` unsafe=1
- safe API `Regulator<T>::is_enabled`
- vendor/linux/rust/kernel/regulator.rs:380 `/// Checks if the regulator is enabled.`
- vendor/linux/rust/kernel/regulator.rs:382 `// SAFETY: Safe as per the type invariants of `Regulator`.`
- vendor/linux/rust/kernel/regulator.rs:383 `AS_PTR`
- wrapper_fix: `8121353a4bf8e38afee26299419a78ec108e14a6`

## W-000174 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: clear_bit
- Explanation: clear_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/bitmap.rs:378 `Bitmap::clear_bit_atomic` unsafe=1
- safe API `Bitmap::clear_bit_atomic`
- vendor/linux/rust/kernel/bitmap.rs:376 `// SAFETY: `index` is within bounds and the caller has ensured that`
- vendor/linux/rust/kernel/bitmap.rs:381 `/// Copy `src` into this [`Bitmap`] and set any remaining bits to zero.`
- vendor/linux/rust/kernel/bitmap.rs:382 `///`
- vendor/linux/rust/kernel/bitmap.rs:378 `AS_PTR`
- wrapper_fix: `6cf93a9ed39e9f86c7f69c28078500270e70a695`
- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`
- wrapper_fix: `6a069876eb1402478900ee0eb7d7fe276bb1f4e3`

## W-000175 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: refcount_dec
- Explanation: refcount_dec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/sync/refcount.rs:81 `Refcount::dec` unsafe=1
- safe API `Refcount::dec`
- vendor/linux/rust/kernel/sync/refcount.rs:76 `/// Provides release memory ordering, such that prior loads and stores are done`
- vendor/linux/rust/kernel/sync/refcount.rs:77 `/// before.`
- vendor/linux/rust/kernel/sync/refcount.rs:80 `// SAFETY: `self.as_ptr()` is valid.`
- vendor/linux/rust/kernel/sync/refcount.rs:80 `AS_PTR`
- vendor/linux/rust/kernel/sync/refcount.rs:81 `AS_PTR`
- wrapper_fix: `bb38f35b35f9de0cebc4d62ea73482454e38cef3`
- wrapper_fix: `9ba1aaf25ab7dadb910348b6857865e87b4c5689`

## W-000176 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: refcount_set
- Explanation: refcount_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/sync/refcount.rs:56 `Refcount::set` unsafe=1
- safe API `Refcount::set`
- vendor/linux/rust/kernel/sync/refcount.rs:52 `/// Set a refcount's value.`
- vendor/linux/rust/kernel/sync/refcount.rs:55 `// SAFETY: `self.as_ptr()` is valid.`
- vendor/linux/rust/kernel/sync/refcount.rs:59 `/// Increment a refcount.`
- vendor/linux/rust/kernel/sync/refcount.rs:55 `AS_PTR`
- vendor/linux/rust/kernel/sync/refcount.rs:56 `AS_PTR`
- wrapper_fix: `bb38f35b35f9de0cebc4d62ea73482454e38cef3`
- wrapper_fix: `9ba1aaf25ab7dadb910348b6857865e87b4c5689`

## W-000007 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_ACCOUNT
- Explanation: VM_ACCOUNT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00100000	/* Is a VM accounted object */`
- New: `INIT_VM_FLAG(ACCOUNT)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:438 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:434 `/// Lock the pages covered when they are faulted in.`

## W-000008 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_ARCH_1
- Explanation: VM_ARCH_1 changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x01000000	/* Architecture-specific flag */`
- New: `INIT_VM_FLAG(ARCH_1)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:450 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:446 `/// Synchronous page faults. (DAX-specific)`

## W-000009 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_DONTCOPY
- Explanation: VM_DONTCOPY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00020000      /* Do not copy this vma on fork */`
- New: `INIT_VM_FLAG(DONTCOPY)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:429 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:425 `/// Memory mapped I/O or similar.`

## W-000010 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_DONTDUMP
- Explanation: VM_DONTDUMP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x04000000	/* Do not include in the core dump */`
- New: `INIT_VM_FLAG(DONTDUMP)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:456 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:452 `/// Wipe VMA contents in child on fork.`

## W-000011 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_DONTEXPAND
- Explanation: VM_DONTEXPAND changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00040000	/* Cannot expand with mremap() */`
- New: `INIT_VM_FLAG(DONTEXPAND)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:432 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:428 `/// Do not copy this vma on fork.`

## W-000012 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_EXEC
- Explanation: VM_EXEC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000004`
- New: `INIT_VM_FLAG(EXEC)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:405 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:401 `/// Mapping allows writes.`

## W-000013 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_HUGEPAGE
- Explanation: VM_HUGEPAGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x20000000	/* MADV_HUGEPAGE marked this vma */`
- New: `INIT_VM_FLAG(HUGEPAGE)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:465 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:461 `/// Can contain `struct page` and pure PFN pages.`

## W-000014 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_HUGETLB
- Explanation: VM_HUGETLB changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00400000	/* Huge TLB Page VM */`
- New: `INIT_VM_FLAG(HUGETLB)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:444 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:440 `/// Should the VM suppress accounting.`

## W-000015 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_IO
- Explanation: VM_IO changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00004000	/* Memory mapped I/O or similar */`
- New: `INIT_VM_FLAG(IO)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:426 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:422 `/// Page-ranges managed without `struct page`, just pure PFN.`

## W-000016 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_LOCKONFAULT
- Explanation: VM_LOCKONFAULT changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00080000	/* Lock the pages covered when they are faulted in */`
- New: `INIT_VM_FLAG(LOCKONFAULT)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:435 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:431 `/// Cannot expand with mremap().`

## W-000017 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_MAYEXEC
- Explanation: VM_MAYEXEC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000040`
- New: `INIT_VM_FLAG(MAYEXEC)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:417 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:413 `/// Mapping may be updated to allow writes.`

## W-000018 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_MAYREAD
- Explanation: VM_MAYREAD changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000010	/* limits for mprotect() etc */`
- New: `INIT_VM_FLAG(MAYREAD)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:411 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:407 `/// Mapping is shared.`

## W-000019 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_MAYSHARE
- Explanation: VM_MAYSHARE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000080`
- New: `INIT_VM_FLAG(MAYSHARE)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:420 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:416 `/// Mapping may be updated to allow execution.`

## W-000020 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_MAYWRITE
- Explanation: VM_MAYWRITE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000020`
- New: `INIT_VM_FLAG(MAYWRITE)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:414 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:410 `/// Mapping may be updated to allow reads.`

## W-000021 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_MERGEABLE
- Explanation: VM_MERGEABLE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `BIT(31)		/* KSM may merge identical pages */`
- New: `INIT_VM_FLAG(MERGEABLE)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:471 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:467 `/// MADV_NOHUGEPAGE marked this vma.`
- vendor/linux/rust/kernel/mm/virt.rs:470 `/// KSM may merge identical pages.`

## W-000022 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_MIXEDMAP
- Explanation: VM_MIXEDMAP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x10000000	/* Can contain "struct page" and pure PFN pages */`
- New: `INIT_VM_FLAG(MIXEDMAP)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:462 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:458 `/// Not soft dirty clean area.`

## W-000023 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_NOHUGEPAGE
- Explanation: VM_NOHUGEPAGE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x40000000	/* MADV_NOHUGEPAGE marked this vma */`
- New: `INIT_VM_FLAG(NOHUGEPAGE)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:468 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:464 `/// MADV_HUGEPAGE marked this vma.`

## W-000024 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_NORESERVE
- Explanation: VM_NORESERVE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00200000	/* should the VM suppress accounting */`
- New: `INIT_VM_FLAG(NORESERVE)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:441 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:437 `/// Is a VM accounted object.`

## W-000025 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_PFNMAP
- Explanation: VM_PFNMAP changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000400	/* Page-ranges managed without "struct page", just pure PFN */`
- New: `INIT_VM_FLAG(PFNMAP)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:423 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:419 `/// Mapping may be updated to be shared.`

## W-000026 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_READ
- Explanation: VM_READ changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000001	/* currently active flags */`
- New: `INIT_VM_FLAG(READ)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:399 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:395 `/// No flags are set.`

## W-000027 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_SHARED
- Explanation: VM_SHARED changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000008`
- New: `INIT_VM_FLAG(SHARED)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:408 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:404 `/// Mapping allows execution.`

## W-000028 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_SOFTDIRTY
- Explanation: VM_SOFTDIRTY changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0`
- New: `VM_NONE`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:459 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:455 `/// Do not include in the core dump.`

## W-000029 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_SYNC
- Explanation: VM_SYNC changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00800000	/* Synchronous page faults */`
- New: `INIT_VM_FLAG(SYNC)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:447 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:443 `/// Huge TLB Page VM.`

## W-000030 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_WIPEONFORK
- Explanation: VM_WIPEONFORK changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x02000000	/* Wipe VMA contents in child. */`
- New: `INIT_VM_FLAG(WIPEONFORK)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:453 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:449 `/// Architecture-specific flag.`

## W-000031 MacroConstDrift

- Risk: Medium
- Score: 10.0
- Symbol: VM_WRITE
- Explanation: VM_WRITE changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `0x00000002`
- New: `INIT_VM_FLAG(WRITE)`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/mm/virt.rs:402 `None` unsafe=0
- vendor/linux/rust/kernel/mm/virt.rs:398 `/// Mapping allows reads.`

## W-000004 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: dma_free_attrs
- Explanation: dma_free_attrs changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['struct device *dev', 'size_t size', 'void *cpu_addr', 'dma_addr_t dma_handle', 'unsigned long attrs'], 'return_type': 'static void'}`
- New: `{'params': ['struct device *dev', 'size_t size', 'void *cpu_addr', 'dma_addr_t dma_handle', 'unsigned long attrs'], 'return_type': 'static inline void'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`

### Rust Evidence

- vendor/linux/rust/kernel/dma.rs:652 `drop` unsafe=1
- vendor/linux/rust/kernel/dma.rs:648 `// SAFETY: Device pointer is guaranteed as valid by the type invariant on `Device`.`
- weak lifetime name vendor/linux/rust/kernel/dma.rs:652 `LIFETIME_NAMING_PATTERN`

## W-000177 SignatureDrift

- Risk: Medium
- Score: 9.0
- Symbol: set_bit
- Explanation: set_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': [{'name': '', 'type': '&mut self'}, {'name': 'index', 'type': 'usize'}, {'name': 'val', 'type': 'bool) { debug_assert!(index / 8 < self.storage.as_ref().len()'}], 'return_type': '()'}`
- New: `{'params': [{'name': 'nr', 'type': 'ffi::c_ulong'}, {'name': 'addr', 'type': '*mut ffi::c_ulong'}], 'return_type': '()'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- vendor/linux/rust/kernel/bitmap.rs:327 `Bitmap::set_bit_atomic` unsafe=1
- safe API `Bitmap::set_bit_atomic`
- vendor/linux/rust/kernel/bitmap.rs:325 `// SAFETY: `index` is within bounds and the caller has ensured that`
- vendor/linux/rust/kernel/bitmap.rs:330 `/// Clear `index` bit.`
- vendor/linux/rust/kernel/bitmap.rs:331 `///`
- vendor/linux/rust/kernel/bitmap.rs:327 `AS_PTR`
- wrapper_fix: `6cf93a9ed39e9f86c7f69c28078500270e70a695`
- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`

## W-000006 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: request
- Explanation: request changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'q', 'type': '*mut request_queue'}, {'name': 'mq_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'mq_hctx', 'type': '*mut blk_mq_hw_ctx'}, {'name': 'cmd_flags', 'type': 'blk_opf_t'}, {'name': 'rq_flags', 'type': 'req_flags_t'}, {'name': 'tag', 'type': 'ffi::c_int'}, {'name': 'internal_tag', 'type': 'ffi::c_int'}, {'name': 'timeout', 'type': 'ffi::c_uint'}, {'name': '__data_len', 'type': 'ffi::c_uint'}, {'name': '__sector', 'type': 'sector_t'}, {'name': 'bio', 'type': '*mut bio'}, {'name': 'biotail', 'type': '*mut bio'}, {'name': '__bindgen_anon_1', 'type': 'request__bindgen_ty_1'}, {'name': 'part', 'type': '*mut block_device'}, {'name': 'start_time_ns', 'type': 'u64_'}, {'name': 'io_start_time_ns', 'type': 'u64_'}, {'name': 'stats_sectors', 'type': 'ffi::c_ushort'}, {'name': 'nr_phys_segments', 'type': 'ffi::c_ushort'}, {'name': 'nr_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'state', 'type': 'mq_rq_state'}, {'name': 'ref_', 'type': 'atomic_t'}, {'name': 'deadline', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'request__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'request__bindgen_ty_3'}, {'name': 'elv', 'type': 'request__bindgen_ty_4'}, {'name': 'flush', 'type': 'request__bindgen_ty_5'}, {'name': 'fifo_time', 'type': 'u64_'}, {'name': 'end_io', 'type': 'rq_end_io_fn'}, {'name': 'end_io_data', 'type': '*mut ffi::c_void'}]`
- New: `[{'name': 'q', 'type': '*mut request_queue'}, {'name': 'mq_ctx', 'type': '*mut blk_mq_ctx'}, {'name': 'mq_hctx', 'type': '*mut blk_mq_hw_ctx'}, {'name': 'cmd_flags', 'type': 'blk_opf_t'}, {'name': 'rq_flags', 'type': 'req_flags_t'}, {'name': 'tag', 'type': 'ffi::c_int'}, {'name': 'internal_tag', 'type': 'ffi::c_int'}, {'name': 'timeout', 'type': 'ffi::c_uint'}, {'name': '__data_len', 'type': 'ffi::c_uint'}, {'name': '__sector', 'type': 'sector_t'}, {'name': 'bio', 'type': '*mut bio'}, {'name': 'biotail', 'type': '*mut bio'}, {'name': '__bindgen_anon_1', 'type': 'request__bindgen_ty_1'}, {'name': 'part', 'type': '*mut block_device'}, {'name': 'start_time_ns', 'type': 'u64_'}, {'name': 'io_start_time_ns', 'type': 'u64_'}, {'name': 'stats_sectors', 'type': 'ffi::c_ushort'}, {'name': 'nr_phys_segments', 'type': 'ffi::c_ushort'}, {'name': 'nr_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'phys_gap_bit', 'type': 'ffi::c_uchar'}, {'name': 'crypt_ctx', 'type': '*mut bio_crypt_ctx'}, {'name': 'crypt_keyslot', 'type': '*mut blk_crypto_keyslot'}, {'name': 'state', 'type': 'mq_rq_state'}, {'name': 'ref_', 'type': 'atomic_t'}, {'name': 'deadline', 'type': 'ffi::c_ulong'}, {'name': '__bindgen_anon_2', 'type': 'request__bindgen_ty_2'}, {'name': '__bindgen_anon_3', 'type': 'request__bindgen_ty_3'}, {'name': 'elv', 'type': 'request__bindgen_ty_4'}, {'name': 'flush', 'type': 'request__bindgen_ty_5'}, {'name': 'fifo_time', 'type': 'u64_'}, {'name': 'end_io', 'type': 'rq_end_io_fn'}, {'name': 'end_io_data', 'type': '*mut ffi::c_void'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- vendor/linux/rust/kernel/block/mq/operations.rs:158 `complete_callback` unsafe=0
- vendor/linux/rust/kernel/block/mq/operations.rs:219 `complete_callback` unsafe=0
- vendor/linux/rust/kernel/block/mq/operations.rs:246 `complete_callback` unsafe=0
- vendor/linux/rust/kernel/block/mq/request.rs:60 `None` unsafe=0
- vendor/linux/rust/kernel/block/mq/request.rs:72 `Request<T>::aref_from_raw` unsafe=0
- safe API `Request<T>::aref_from_raw`
- safe API `Request<T>::complete`
- safe API `Request<T>::wrapper_ptr`
- vendor/linux/rust/kernel/block/mq/operations.rs:153 `/// # Safety`
- vendor/linux/rust/kernel/block/mq/operations.rs:154 `///`
- vendor/linux/rust/kernel/block/mq/operations.rs:155 `/// This function may only be called by blk-mq C infrastructure. `rq` must`
- vendor/linux/rust/kernel/block/mq/request.rs:76 `NONNULL_MAPPING`
- vendor/linux/rust/kernel/block/mq/request.rs:60 `OPAQUE`
- vendor/linux/rust/kernel/block/mq/request.rs:63 `AREF`
- vendor/linux/rust/kernel/block/mq/request.rs:72 `AREF`
- wrapper_fix: `28e848386b92645f93b9f2fdba5882c3ca7fb3e2`
- wrapper_fix: `a307bf1db5448eccd72a1d7857f7661c6330d5ad`

## W-000001 FieldDrift

- Risk: Medium
- Score: 9.0
- Symbol: device
- Explanation: device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'em_pd', 'type': '*mut em_perf_domain'}, {'name': 'pins', 'type': '*mut dev_pin_info'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_ops', 'type': '*mut dma_map_ops'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_mem', 'type': '*mut dma_coherent_mem'}, {'name': 'cma_area', 'type': '*mut cma'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`
- New: `[{'name': 'kobj', 'type': 'kobject'}, {'name': 'parent', 'type': '*mut device'}, {'name': 'p', 'type': '*mut device_private'}, {'name': 'init_name', 'type': '*const ffi::c_char'}, {'name': 'type_', 'type': '*const device_type'}, {'name': 'bus', 'type': '*const bus_type'}, {'name': 'driver', 'type': '*mut device_driver'}, {'name': 'platform_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_data', 'type': '*mut ffi::c_void'}, {'name': 'driver_override', 'type': 'device__bindgen_ty_1'}, {'name': 'mutex', 'type': 'mutex'}, {'name': 'links', 'type': 'dev_links_info'}, {'name': 'power', 'type': 'dev_pm_info'}, {'name': 'pm_domain', 'type': '*mut dev_pm_domain'}, {'name': 'em_pd', 'type': '*mut em_perf_domain'}, {'name': 'pins', 'type': '*mut dev_pin_info'}, {'name': 'msi', 'type': 'dev_msi_info'}, {'name': 'dma_ops', 'type': '*mut dma_map_ops'}, {'name': 'dma_mask', 'type': '*mut u64_'}, {'name': 'coherent_dma_mask', 'type': 'u64_'}, {'name': 'bus_dma_limit', 'type': 'u64_'}, {'name': 'dma_range_map', 'type': '*mut bus_dma_region'}, {'name': 'dma_parms', 'type': '*mut device_dma_parameters'}, {'name': 'dma_pools', 'type': 'list_head'}, {'name': 'dma_mem', 'type': '*mut dma_coherent_mem'}, {'name': 'cma_area', 'type': '*mut cma'}, {'name': 'dma_io_tlb_mem', 'type': '*mut io_tlb_mem'}, {'name': 'archdata', 'type': 'dev_archdata'}, {'name': 'of_node', 'type': '*mut device_node'}, {'name': 'fwnode', 'type': '*mut fwnode_handle'}, {'name': 'numa_node', 'type': 'ffi::c_int'}, {'name': 'devt', 'type': 'dev_t'}, {'name': 'id', 'type': 'u32_'}, {'name': 'devres_lock', 'type': 'spinlock_t'}, {'name': 'devres_head', 'type': 'list_head'}, {'name': 'class', 'type': '*const class'}, {'name': 'groups', 'type': '*mut *const attribute_group'}, {'name': 'release', 'type': '::core::option::Option<unsafe extern "C" fn(dev: *mut device)>'}, {'name': 'iommu_group', 'type': '*mut iommu_group'}, {'name': 'iommu', 'type': '*mut dev_iommu'}, {'name': 'physical_location', 'type': '*mut device_physical_location'}, {'name': 'removable', 'type': 'device_removable'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': '__bindgen_padding_0', 'type': '[u8; 3usize]'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- vendor/linux/rust/kernel/auxiliary.rs:269 `release` unsafe=0
- vendor/linux/rust/kernel/device.rs:170 `None` unsafe=0
- vendor/linux/rust/kernel/device.rs:183 `Device::get_device` unsafe=0
- vendor/linux/rust/kernel/device.rs:338 `Device<Ctx>::as_raw` unsafe=0
- vendor/linux/rust/kernel/device.rs:369 `Device<Ctx>::parent` unsafe=0
- safe API `Device::get_device`
- safe API `Device<Ctx>::as_raw`
- safe API `Device<Ctx>::parent`
- vendor/linux/rust/kernel/auxiliary.rs:265 `// SAFETY: A `struct auxiliary_device` always has a parent.`
- vendor/linux/rust/kernel/device.rs:165 `///`
- vendor/linux/rust/kernel/device.rs:166 `/// [`AlwaysRefCounted`]: kernel::sync::aref::AlwaysRefCounted`
- vendor/linux/rust/kernel/device.rs:170 `OPAQUE`
- vendor/linux/rust/kernel/device.rs:183 `AREF`
- vendor/linux/rust/kernel/device.rs:185 `FROM_RAW`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`
- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`

## W-000014 FieldDrift

- Risk: Medium
- Score: 8.0
- Symbol: pci_dev
- Explanation: pci_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'aer_cap', 'type': 'u16_'}, {'name': 'aer_stats', 'type': '*mut aer_stats'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 17usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': 'match_driver', 'type': 'bool_'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 5usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 17usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 17usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- vendor/linux/rust/kernel/pci.rs:58 `None` unsafe=0
- vendor/linux/rust/kernel/pci.rs:86 `remove_callback` unsafe=0
- vendor/linux/rust/kernel/pci.rs:364 `as_raw` unsafe=0
- vendor/linux/rust/kernel/pci.rs:367 `as_raw` unsafe=1
- vendor/linux/rust/kernel/pci.rs:359 `/// a `bindings::pci_dev`.`
- vendor/linux/rust/kernel/pci.rs:365 `// SAFETY: By the type invariant `self.0.as_raw` is a pointer to the `struct device``
- vendor/linux/rust/kernel/pci.rs:370 `/// Returns the PCI vendor ID.`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000015 FieldDrift

- Risk: Medium
- Score: 8.0
- Symbol: platform_device
- Explanation: platform_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[]`
- New: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'id_auto', 'type': 'bool_'}, {'name': 'dev', 'type': 'device'}, {'name': 'platform_dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'num_resources', 'type': 'u32_'}, {'name': 'resource', 'type': '*mut resource'}, {'name': 'id_entry', 'type': '*const platform_device_id'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'mfd_cell', 'type': '*mut mfd_cell'}, {'name': 'archdata', 'type': 'pdev_archdata'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- vendor/linux/rust/kernel/platform.rs:56 `probe_callback` unsafe=0
- vendor/linux/rust/kernel/platform.rs:77 `remove_callback` unsafe=0
- vendor/linux/rust/kernel/platform.rs:189 `as_raw` unsafe=0
- vendor/linux/rust/kernel/platform.rs:192 `as_raw` unsafe=1
- vendor/linux/rust/kernel/platform.rs:57 `// SAFETY: The platform bus only ever calls the probe callback with a valid `pdev`.`
- vendor/linux/rust/kernel/platform.rs:59 `// SAFETY: `dev` is guaranteed to be embedded in a valid `struct platform_device` by the`
- vendor/linux/rust/kernel/platform.rs:184 `/// `bindings::platform_device`.`
- wrapper_fix: `ef4dc4cc7001e9cce8a3b556362171648be9ad92`
- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`
- wrapper_fix: `0242623384c767b1156b61b67894b4ecf6682b8b`

## W-000016 FieldDrift

- Risk: Medium
- Score: 8.0
- Symbol: queue_limits
- Explanation: queue_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`
- New: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- vendor/linux/rust/kernel/block/mq/gen_disk.rs:97 `GenDiskBuilder::capacity_sectors` unsafe=1
- safe API `GenDiskBuilder::capacity_sectors`
- vendor/linux/rust/kernel/block/mq/gen_disk.rs:96 `// SAFETY: `bindings::queue_limits` contain only fields that are valid when zeroed.`
- wrapper_fix: `5e3b7009f116f684ac6b93d8924506154f3b1f6d`

## W-000002 MacroConstDrift

- Risk: Medium
- Score: 8.0
- Symbol: init_wait
- Explanation: init_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `\`
- New: `init_wait_func(wait, autoremove_wake_function)`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- c_source_diff_strength: `3.0`
- weak_name_match_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/sync/condvar.rs:123 `CondVar::new` unsafe=1
- safe API `CondVar::new`
- weak lifetime name vendor/linux/rust/kernel/sync/condvar.rs:123 `LIFETIME_NAMING_PATTERN`

## W-000005 FieldDrift

- Risk: Medium
- Score: 8.0
- Symbol: queue_limits
- Explanation: queue_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`
- New: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- vendor/linux/rust/kernel/block/mq/gen_disk.rs:97 `GenDiskBuilder::capacity_sectors` unsafe=1
- safe API `GenDiskBuilder::capacity_sectors`
- vendor/linux/rust/kernel/block/mq/gen_disk.rs:96 `// SAFETY: `bindings::queue_limits` contain only fields that are valid when zeroed.`
- wrapper_fix: `5e3b7009f116f684ac6b93d8924506154f3b1f6d`

## W-000010 FieldDrift

- Risk: Medium
- Score: 8.0
- Symbol: queue_limits
- Explanation: queue_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`
- New: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- vendor/linux/rust/kernel/block/mq/gen_disk.rs:97 `GenDiskBuilder::capacity_sectors` unsafe=1
- safe API `GenDiskBuilder::capacity_sectors`
- vendor/linux/rust/kernel/block/mq/gen_disk.rs:96 `// SAFETY: `bindings::queue_limits` contain only fields that are valid when zeroed.`
- wrapper_fix: `5e3b7009f116f684ac6b93d8924506154f3b1f6d`

## W-000005 FieldDrift

- Risk: Medium
- Score: 8.0
- Symbol: queue_limits
- Explanation: queue_limits changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`
- New: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'max_fast_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_wzeroes_unmap_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_write_streams', 'type': 'ffi::c_ushort'}, {'name': 'write_stream_granularity', 'type': 'ffi::c_uint'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- vendor/linux/rust/kernel/block/mq/gen_disk.rs:111 `GenDiskBuilder::capacity_sectors` unsafe=1
- safe API `GenDiskBuilder::capacity_sectors`
- vendor/linux/rust/kernel/block/mq/gen_disk.rs:106 `// SAFETY: T::QueueData was created by the call to `into_foreign()` above`
- vendor/linux/rust/kernel/block/mq/gen_disk.rs:110 `// SAFETY: `bindings::queue_limits` contain only fields that are valid when zeroed.`
- wrapper_fix: `5e3b7009f116f684ac6b93d8924506154f3b1f6d`

## W-000011 SignatureDrift

- Risk: Low
- Score: 7.0
- Symbol: pci_set_master
- Explanation: pci_set_master changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/pci.rs:396 `Device::set_master` unsafe=1
- safe API `Device::set_master`
- vendor/linux/rust/kernel/pci.rs:393 `/// Enable bus-mastering for this device.`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000001 FieldDrift

- Risk: Low
- Score: 7.0
- Symbol: pci_dev
- Explanation: pci_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'aer_cap', 'type': 'u16_'}, {'name': 'aer_stats', 'type': '*mut aer_stats'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 17usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': 'match_driver', 'type': 'bool_'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 5usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 17usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 17usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`
- New: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'aer_cap', 'type': 'u16_'}, {'name': 'aer_stats', 'type': '*mut aer_stats'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 17usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': 'match_driver', 'type': 'bool_'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 17usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 17usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- vendor/linux/rust/kernel/pci.rs:62 `None` unsafe=0
- vendor/linux/rust/kernel/pci.rs:89 `remove_callback` unsafe=0
- vendor/linux/rust/kernel/pci.rs:254 `None` unsafe=0
- vendor/linux/rust/kernel/pci.rs:364 `as_raw` unsafe=0
- vendor/linux/rust/kernel/pci.rs:249 `/// # Invariants`
- vendor/linux/rust/kernel/pci.rs:250 `///`
- vendor/linux/rust/kernel/pci.rs:251 `/// A [`Device`] instance represents a valid `struct device` created by the C portion of the kernel.`
- vendor/linux/rust/kernel/pci.rs:254 `OPAQUE`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000004 FieldDrift

- Risk: Low
- Score: 7.0
- Symbol: pci_dev
- Explanation: pci_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'aer_cap', 'type': 'u16_'}, {'name': 'aer_stats', 'type': '*mut aer_stats'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 17usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': 'match_driver', 'type': 'bool_'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 17usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 17usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`
- New: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'aer_cap', 'type': 'u16_'}, {'name': 'aer_info', 'type': '*mut aer_info'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 17usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 17usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 17usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- vendor/linux/rust/kernel/pci.rs:62 `None` unsafe=0
- vendor/linux/rust/kernel/pci.rs:89 `remove_callback` unsafe=0
- vendor/linux/rust/kernel/pci.rs:257 `None` unsafe=0
- vendor/linux/rust/kernel/pci.rs:367 `as_raw` unsafe=0
- vendor/linux/rust/kernel/pci.rs:474 `try_from` unsafe=1
- vendor/linux/rust/kernel/pci.rs:252 `/// # Invariants`
- vendor/linux/rust/kernel/pci.rs:253 `///`
- vendor/linux/rust/kernel/pci.rs:254 `/// A [`Device`] instance represents a valid `struct device` created by the C portion of the kernel.`
- vendor/linux/rust/kernel/pci.rs:257 `OPAQUE`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000002 FieldDrift

- Risk: Low
- Score: 7.0
- Symbol: pci_dev
- Explanation: pci_dev changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'aer_cap', 'type': 'u16_'}, {'name': 'aer_info', 'type': '*mut aer_info'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 17usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 17usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 17usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`
- New: `[{'name': 'bus_list', 'type': 'list_head'}, {'name': 'bus', 'type': '*mut pci_bus'}, {'name': 'subordinate', 'type': '*mut pci_bus'}, {'name': 'sysdata', 'type': '*mut ffi::c_void'}, {'name': 'procent', 'type': '*mut proc_dir_entry'}, {'name': 'slot', 'type': '*mut pci_slot'}, {'name': 'devfn', 'type': 'ffi::c_uint'}, {'name': 'vendor', 'type': 'ffi::c_ushort'}, {'name': 'device', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_vendor', 'type': 'ffi::c_ushort'}, {'name': 'subsystem_device', 'type': 'ffi::c_ushort'}, {'name': 'class', 'type': 'ffi::c_uint'}, {'name': 'revision', 'type': 'u8_'}, {'name': 'hdr_type', 'type': 'u8_'}, {'name': 'aer_cap', 'type': 'u16_'}, {'name': 'aer_info', 'type': '*mut aer_info'}, {'name': 'rcec_ea', 'type': '*mut rcec_ea'}, {'name': 'rcec', 'type': '*mut pci_dev'}, {'name': 'devcap', 'type': 'u32_'}, {'name': 'rebar_cap', 'type': 'u16_'}, {'name': 'pcie_cap', 'type': 'u8_'}, {'name': 'msi_cap', 'type': 'u8_'}, {'name': 'msix_cap', 'type': 'u8_'}, {'name': '_bitfield_align_1', 'type': '[u8; 0]'}, {'name': '_bitfield_1', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'rom_base_reg', 'type': 'u8_'}, {'name': 'pin', 'type': 'u8_'}, {'name': 'pcie_flags_reg', 'type': 'u16_'}, {'name': 'dma_alias_mask', 'type': '*mut ffi::c_ulong'}, {'name': 'driver', 'type': '*mut pci_driver'}, {'name': 'dma_mask', 'type': 'u64_'}, {'name': 'msi_addr_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'current_state', 'type': 'pci_power_t'}, {'name': 'pm_cap', 'type': 'u8_'}, {'name': '_bitfield_align_2', 'type': '[u8; 0]'}, {'name': '_bitfield_2', 'type': '__BindgenBitfieldUnit<[u8; 3usize]>'}, {'name': 'd3hot_delay', 'type': 'ffi::c_uint'}, {'name': 'd3cold_delay', 'type': 'ffi::c_uint'}, {'name': 'l1ss', 'type': 'u16_'}, {'name': 'link_state', 'type': '*mut pcie_link_state'}, {'name': '_bitfield_align_3', 'type': '[u8; 0]'}, {'name': '_bitfield_3', 'type': '__BindgenBitfieldUnit<[u8; 1usize]>'}, {'name': 'error_state', 'type': 'pci_channel_state_t'}, {'name': 'dev', 'type': 'device'}, {'name': 'cfg_size', 'type': 'ffi::c_int'}, {'name': 'irq', 'type': 'ffi::c_uint'}, {'name': 'resource', 'type': '[resource; 17usize]'}, {'name': 'driver_exclusive_resource', 'type': 'resource'}, {'name': '_bitfield_align_4', 'type': '[u8; 0]'}, {'name': '_bitfield_4', 'type': '__BindgenBitfieldUnit<[u8; 6usize]>'}, {'name': 'dev_flags', 'type': 'pci_dev_flags_t'}, {'name': 'enable_cnt', 'type': 'atomic_t'}, {'name': 'pcie_cap_lock', 'type': 'spinlock_t'}, {'name': 'saved_config_space', 'type': '[u32_; 16usize]'}, {'name': 'saved_cap_space', 'type': 'hlist_head'}, {'name': 'res_attr', 'type': '[*mut bin_attribute; 17usize]'}, {'name': 'res_attr_wc', 'type': '[*mut bin_attribute; 17usize]'}, {'name': 'msix_base', 'type': '*mut ffi::c_void'}, {'name': 'msi_lock', 'type': 'raw_spinlock_t'}, {'name': 'vpd', 'type': 'pci_vpd'}, {'name': 'link_bwctrl', 'type': '*mut pcie_bwctrl_data'}, {'name': '__bindgen_anon_1', 'type': 'pci_dev__bindgen_ty_1'}, {'name': 'ats_cap', 'type': 'u16_'}, {'name': 'ats_stu', 'type': 'u8_'}, {'name': 'pasid_cap', 'type': 'u16_'}, {'name': 'pasid_features', 'type': 'u16_'}, {'name': 'acs_cap', 'type': 'u16_'}, {'name': 'acs_capabilities', 'type': 'u16_'}, {'name': 'supported_speeds', 'type': 'u8_'}, {'name': 'rom', 'type': 'phys_addr_t'}, {'name': 'romlen', 'type': 'usize'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'priv_flags', 'type': 'ffi::c_ulong'}, {'name': 'reset_methods', 'type': '[u8_; 8usize]'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- vendor/linux/rust/kernel/pci.rs:101 `None` unsafe=0
- vendor/linux/rust/kernel/pci.rs:123 `remove_callback` unsafe=0
- vendor/linux/rust/kernel/pci.rs:339 `None` unsafe=0
- vendor/linux/rust/kernel/pci.rs:345 `as_raw` unsafe=0
- vendor/linux/rust/kernel/pci.rs:466 `None` unsafe=0
- vendor/linux/rust/kernel/pci.rs:124 `// SAFETY: The PCI bus only ever calls the remove callback with a valid pointer to a`
- vendor/linux/rust/kernel/pci.rs:334 `///`
- vendor/linux/rust/kernel/pci.rs:335 `/// A [`Device`] instance represents a valid `struct pci_dev` created by the C portion of the`
- vendor/linux/rust/kernel/pci.rs:339 `OPAQUE`
- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000003 FieldDrift

- Risk: Low
- Score: 7.0
- Symbol: platform_device
- Explanation: platform_device changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'id_auto', 'type': 'bool_'}, {'name': 'dev', 'type': 'device'}, {'name': 'platform_dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'num_resources', 'type': 'u32_'}, {'name': 'resource', 'type': '*mut resource'}, {'name': 'id_entry', 'type': '*const platform_device_id'}, {'name': 'driver_override', 'type': '*const ffi::c_char'}, {'name': 'mfd_cell', 'type': '*mut mfd_cell'}, {'name': 'archdata', 'type': 'pdev_archdata'}]`
- New: `[{'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'id', 'type': 'ffi::c_int'}, {'name': 'id_auto', 'type': 'bool_'}, {'name': 'dev', 'type': 'device'}, {'name': 'platform_dma_mask', 'type': 'u64_'}, {'name': 'dma_parms', 'type': 'device_dma_parameters'}, {'name': 'num_resources', 'type': 'u32_'}, {'name': 'resource', 'type': '*mut resource'}, {'name': 'id_entry', 'type': '*const platform_device_id'}, {'name': 'mfd_cell', 'type': '*mut mfd_cell'}, {'name': 'archdata', 'type': 'pdev_archdata'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- vendor/linux/rust/kernel/platform.rs:95 `probe_callback` unsafe=0
- vendor/linux/rust/kernel/platform.rs:111 `remove_callback` unsafe=0
- vendor/linux/rust/kernel/platform.rs:257 `None` unsafe=0
- vendor/linux/rust/kernel/platform.rs:262 `as_raw` unsafe=0
- vendor/linux/rust/kernel/platform.rs:325 `None` unsafe=0
- vendor/linux/rust/kernel/platform.rs:96 `// SAFETY: The platform bus only ever calls the probe callback with a valid pointer to a`
- vendor/linux/rust/kernel/platform.rs:112 `// SAFETY: The platform bus only ever calls the remove callback with a valid pointer to a`
- vendor/linux/rust/kernel/platform.rs:252 `///`
- vendor/linux/rust/kernel/platform.rs:257 `OPAQUE`
- wrapper_fix: `ef4dc4cc7001e9cce8a3b556362171648be9ad92`
- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`
- wrapper_fix: `0242623384c767b1156b61b67894b4ecf6682b8b`

## W-000004 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: faux_device_destroy
- Explanation: faux_device_destroy changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/faux.rs:55 `drop` unsafe=1
- vendor/linux/rust/kernel/faux.rs:54 `// SAFETY: `self.0` is a valid registered faux_device via our type invariants.`
- vendor/linux/rust/kernel/faux.rs:59 `// SAFETY: The faux device API is thread-safe as guaranteed by the device core, as long as`
- vendor/linux/rust/kernel/faux.rs:52 `IMPL_DROP`
- wrapper_fix: `78418f300d3999f1cf8a9ac71065bf2eca61f4dd`

## W-000004 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: poll_wait
- Explanation: poll_wait changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/sync/poll.rs:61 `PollTable<'a>::register_wait` unsafe=1
- safe API `PollTable<'a>::register_wait`
- vendor/linux/rust/kernel/sync/poll.rs:65 `/// A wrapper around [`CondVar`] that makes it usable with [`PollTable`].`
- vendor/linux/rust/kernel/sync/poll.rs:66 `///`
- vendor/linux/rust/kernel/sync/poll.rs:61 `AS_PTR`
- wrapper_fix: `de747bd023c09b5b7f3bf5c952d7b1da77a9caaa`

## W-000005 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: regulator_disable
- Explanation: regulator_disable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/regulator.rs:299 `disable_internal` unsafe=1
- vendor/linux/rust/kernel/regulator.rs:393 `drop` unsafe=1
- vendor/linux/rust/kernel/regulator.rs:298 `// SAFETY: Safe as per the type invariants of `Regulator`.`
- vendor/linux/rust/kernel/regulator.rs:304 `/// Obtains a [`Regulator`] instance from the system.`
- vendor/linux/rust/kernel/regulator.rs:390 `// SAFETY: By the type invariants, we know that `self` owns a`
- vendor/linux/rust/kernel/regulator.rs:294 `TO_RESULT_MAPPING`
- vendor/linux/rust/kernel/regulator.rs:299 `TO_RESULT_MAPPING`
- vendor/linux/rust/kernel/regulator.rs:299 `AS_PTR`
- vendor/linux/rust/kernel/regulator.rs:393 `AS_PTR`
- wrapper_fix: `8121353a4bf8e38afee26299419a78ec108e14a6`

## W-000006 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: regulator_enable
- Explanation: regulator_enable changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/regulator.rs:294 `enable_internal` unsafe=1
- vendor/linux/rust/kernel/regulator.rs:293 `// SAFETY: Safe as per the type invariants of `Regulator`.`
- vendor/linux/rust/kernel/regulator.rs:294 `AS_PTR`
- wrapper_fix: `8121353a4bf8e38afee26299419a78ec108e14a6`

## W-000009 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: regulator_put
- Explanation: regulator_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/regulator.rs:397 `drop` unsafe=1
- vendor/linux/rust/kernel/regulator.rs:395 `// SAFETY: By the type invariants, we know that `self` owns a reference,`
- vendor/linux/rust/kernel/regulator.rs:401 `/// A voltage.`
- vendor/linux/rust/kernel/regulator.rs:402 `///`
- vendor/linux/rust/kernel/regulator.rs:397 `AS_PTR`
- wrapper_fix: `8121353a4bf8e38afee26299419a78ec108e14a6`

## W-000173 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: bitmap_copy_and_extend
- Explanation: bitmap_copy_and_extend changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/bitmap.rs:406 `Bitmap::copy_and_extend` unsafe=1
- safe API `Bitmap::copy_and_extend`
- vendor/linux/rust/kernel/bitmap.rs:404 `// SAFETY: access to `self` and `src` is within bounds.`
- vendor/linux/rust/kernel/bitmap.rs:408 `AS_PTR`
- wrapper_fix: `0452b4ab2961093f23bb289b0112351b917fb23c`
- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`

## W-000178 FieldDrift

- Risk: Low
- Score: 6.0
- Symbol: kunit_case
- Explanation: kunit_case changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'run_case', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'generate_params', 'type': '::core::option::Option<'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'module_name', 'type': '*mut ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}]`
- New: `[{'name': 'run_case', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'name', 'type': '*const ffi::c_char'}, {'name': 'generate_params', 'type': '::core::option::Option<'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'param_init', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit) -> ffi::c_int>'}, {'name': 'param_exit', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'module_name', 'type': '*mut ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}]`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- vendor/linux/rust/kernel/kunit.rs:202 `is_test_result_ok` unsafe=0
- vendor/linux/rust/kernel/kunit.rs:203 `is_test_result_ok` unsafe=0
- vendor/linux/rust/kernel/kunit.rs:223 `kunit_case_null` unsafe=0
- vendor/linux/rust/kernel/kunit.rs:224 `kunit_case_null` unsafe=0
- vendor/linux/rust/kernel/kunit.rs:296 `test_fn` unsafe=1
- safe API `is_test_result_ok`
- vendor/linux/rust/kernel/kunit.rs:197 `/// Use [`kunit_case_null`] to generate such a delimiter.`
- vendor/linux/rust/kernel/kunit.rs:218 `/// Represents the NULL test case delimiter.`
- vendor/linux/rust/kernel/kunit.rs:219 `///`
- wrapper_fix: `7f87c7a003125d5af5ec7abbbc0ac21b4a4661ae`
- wrapper_fix: `be97f3c82021239476ce32cddde32948c597753e`

## W-000001 SignatureDrift

- Risk: Low
- Score: 3.0
- Symbol: devm_add_action
- Explanation: devm_add_action changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/devres.rs:119 `new` unsafe=1
- vendor/linux/rust/kernel/devres.rs:116 `// SAFETY: `devm_add_action` guarantees to call `Self::devres_callback` once `dev` is`
- vendor/linux/rust/kernel/devres.rs:122 `// SAFETY: We just created another reference to `inner` in order to pass it to`
- weak lifetime name vendor/linux/rust/kernel/devres.rs:119 `LIFETIME_NAMING_PATTERN`
- wrapper_fix: `ba268514ea14b44570030e8ed2aef92a38679e85`

## W-000001 SignatureDrift

- Risk: Low
- Score: 3.0
- Symbol: dev_is_pci
- Explanation: dev_is_pci changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/pci.rs:467 `try_from` unsafe=1
- vendor/linux/rust/kernel/pci.rs:465 `// SAFETY: By the type invariant of `Device`, `dev.as_raw()` is a valid pointer to a`
- wrapper_fix: `473b9f331718267815649cd93801da832200db71`

## W-000002 SignatureDrift

- Risk: Low
- Score: 3.0
- Symbol: drm_gem_object_get
- Explanation: drm_gem_object_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/drm/gem/mod.rs:61 `inc_ref` unsafe=1
- vendor/linux/rust/kernel/drm/gem/mod.rs:57 `// SAFETY: All gem objects are refcounted.`
- vendor/linux/rust/kernel/drm/gem/mod.rs:60 `// SAFETY: The existence of a shared reference guarantees that the refcount is non-zero.`
- vendor/linux/rust/kernel/drm/gem/mod.rs:65 `// SAFETY: We either hold the only refcount on `obj`, or one of many - meaning that no one`
- weak lifetime name vendor/linux/rust/kernel/drm/gem/mod.rs:61 `LIFETIME_NAMING_PATTERN`
- wrapper_fix: `38cb08c3fcd3f3b1d0225dcec8ae50fab5751549`
- wrapper_fix: `5ae65bdcb867555540169ef57876658262a67d87`

## W-000003 SignatureDrift

- Risk: Low
- Score: 3.0
- Symbol: drm_gem_object_put
- Explanation: drm_gem_object_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/drm/gem/mod.rs:73 `dec_ref` unsafe=1
- vendor/linux/rust/kernel/drm/gem/mod.rs:70 `// SAFETY:`
- vendor/linux/rust/kernel/drm/gem/mod.rs:77 `/// Trait which must be implemented by drivers using base GEM objects.`
- weak lifetime name vendor/linux/rust/kernel/drm/gem/mod.rs:73 `LIFETIME_NAMING_PATTERN`
- wrapper_fix: `38cb08c3fcd3f3b1d0225dcec8ae50fab5751549`
- wrapper_fix: `5ae65bdcb867555540169ef57876658262a67d87`

## W-000002 SignatureDrift

- Risk: Low
- Score: 3.0
- Symbol: fsleep
- Explanation: fsleep changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/time/delay.rs:47 `fsleep` unsafe=1
- safe API `fsleep`
- vendor/linux/rust/kernel/time/delay.rs:42 `// SAFETY: It is always safe to call `fsleep()` with any duration.`
- wrapper_fix: `d4b29ddf82a458935f1bd4909b8a7a13df9d3bdc`

## W-000001 SignatureDrift

- Risk: Low
- Score: 3.0
- Symbol: __clear_bit
- Explanation: __clear_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/bitmap.rs:351 `Bitmap::clear_bit` unsafe=1
- safe API `Bitmap::clear_bit`
- vendor/linux/rust/kernel/bitmap.rs:350 `// SAFETY: `index` is within bounds.`
- vendor/linux/rust/kernel/bitmap.rs:354 `/// Clear `index` bit, atomically.`
- vendor/linux/rust/kernel/bitmap.rs:355 `///`
- wrapper_fix: `6cf93a9ed39e9f86c7f69c28078500270e70a695`
- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`

## W-000002 SignatureDrift

- Risk: Low
- Score: 3.0
- Symbol: __set_bit
- Explanation: __set_bit changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/bitmap.rs:300 `Bitmap::set_bit` unsafe=1
- safe API `Bitmap::set_bit`
- vendor/linux/rust/kernel/bitmap.rs:299 `// SAFETY: Bit `index` is within bounds.`
- vendor/linux/rust/kernel/bitmap.rs:303 `/// Set bit with index `index`, atomically.`
- vendor/linux/rust/kernel/bitmap.rs:304 `///`
- wrapper_fix: `6cf93a9ed39e9f86c7f69c28078500270e70a695`
- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`

## W-000013 SignatureDrift

- Risk: Low
- Score: 1.0
- Symbol: platform_set_drvdata
- Explanation: platform_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/platform.rs:69 `probe_callback` unsafe=1
- vendor/linux/rust/kernel/platform.rs:67 `// SAFETY: By the type invariant `pdev.as_raw` returns a valid pointer to a`
- wrapper_fix: `ef4dc4cc7001e9cce8a3b556362171648be9ad92`

## W-000003 SignatureDrift

- Risk: Low
- Score: -1.0
- Symbol: pwmchip_release
- Explanation: pwmchip_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/pwm.rs:310 `release_callback` unsafe=1
- vendor/linux/rust/kernel/pwm.rs:307 `// SAFETY: `dev` is the valid pointer passed into this callback, which is`
- weak lifetime name vendor/linux/rust/kernel/pwm.rs:310 `LIFETIME_NAMING_PATTERN`
- wrapper_fix: `6fe9e919c144f1296d38e2abb10c7ac4320aa7fa`

## W-000004 SignatureDrift

- Risk: Low
- Score: -1.0
- Symbol: pwmchip_remove
- Explanation: pwmchip_remove changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/pwm.rs:709 `drop` unsafe=1
- vendor/linux/rust/kernel/pwm.rs:705 `// SAFETY: `chip_raw` points to a chip that was successfully registered.`
- vendor/linux/rust/kernel/pwm.rs:714 `/// Declares a kernel module that exposes a single PWM driver.`
- weak lifetime name vendor/linux/rust/kernel/pwm.rs:709 `LIFETIME_NAMING_PATTERN`
- wrapper_fix: `6fe9e919c144f1296d38e2abb10c7ac4320aa7fa`

## W-000003 SignatureDrift

- Risk: Low
- Score: -3.0
- Symbol: platform_set_drvdata
- Explanation: platform_set_drvdata changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `present`
- New: `removed`

### Score Breakdown

- multi_version_consistency: `2.0`
- binding_only_penalty: `-5.0`

### Rust Evidence

- wrapper_fix: `ef4dc4cc7001e9cce8a3b556362171648be9ad92`

## W-000006 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: pci_dev_get
- Explanation: pci_dev_get changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000007 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: pci_dev_put
- Explanation: pci_dev_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `7b948a2af6b5d64a25c14da8f63d8084ea527cd9`

## W-000012 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: platform_device_put
- Explanation: platform_device_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `4d320e30ee04c25c660eca2bb33e846ebb71a79a`

## W-000005 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: pci_alloc_irq_vectors
- Explanation: pci_alloc_irq_vectors changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `473b9f331718267815649cd93801da832200db71`

## W-000009 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: pci_free_irq_vectors
- Explanation: pci_free_irq_vectors changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `473b9f331718267815649cd93801da832200db71`

## W-000010 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: pci_irq_vector
- Explanation: pci_irq_vector changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `473b9f331718267815649cd93801da832200db71`

## W-000001 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: pwmchip_alloc
- Explanation: pwmchip_alloc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- vendor/linux/rust/kernel/pwm.rs:595 `bound_parent_device` unsafe=1
- wrapper_fix: `6fe9e919c144f1296d38e2abb10c7ac4320aa7fa`

## W-000002 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: pwmchip_put
- Explanation: pwmchip_put changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `a2633dc243c35754a0c2270131d8a199c987c9bf`

## W-000002 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: devm_platform_ioremap_resource
- Explanation: devm_platform_ioremap_resource changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `752417b3f0e7721f1d630f40da22d57e0dae043e`
- wrapper_fix: `69d5fbb0159673ea6737204f4d458a220e81a0c9`

## W-000003 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_add
- Explanation: atomic64_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000004 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_add_negative
- Explanation: atomic64_add_negative changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000005 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_add_negative_acquire
- Explanation: atomic64_add_negative_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000006 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_add_negative_relaxed
- Explanation: atomic64_add_negative_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000007 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_add_negative_release
- Explanation: atomic64_add_negative_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000008 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_add_return
- Explanation: atomic64_add_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000009 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_add_return_acquire
- Explanation: atomic64_add_return_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000010 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_add_return_relaxed
- Explanation: atomic64_add_return_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000011 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_add_return_release
- Explanation: atomic64_add_return_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000012 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_add_unless
- Explanation: atomic64_add_unless changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000013 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_and
- Explanation: atomic64_and changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000014 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_andnot
- Explanation: atomic64_andnot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000015 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_cmpxchg
- Explanation: atomic64_cmpxchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000016 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_cmpxchg_acquire
- Explanation: atomic64_cmpxchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000017 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_cmpxchg_relaxed
- Explanation: atomic64_cmpxchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000018 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_cmpxchg_release
- Explanation: atomic64_cmpxchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000019 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_dec
- Explanation: atomic64_dec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000020 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_dec_and_test
- Explanation: atomic64_dec_and_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000021 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_dec_if_positive
- Explanation: atomic64_dec_if_positive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000022 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_dec_return
- Explanation: atomic64_dec_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000023 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_dec_return_acquire
- Explanation: atomic64_dec_return_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000024 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_dec_return_relaxed
- Explanation: atomic64_dec_return_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000025 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_dec_return_release
- Explanation: atomic64_dec_return_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000026 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_dec_unless_positive
- Explanation: atomic64_dec_unless_positive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000027 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_add
- Explanation: atomic64_fetch_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000028 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_add_acquire
- Explanation: atomic64_fetch_add_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000029 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_add_relaxed
- Explanation: atomic64_fetch_add_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000030 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_add_release
- Explanation: atomic64_fetch_add_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000031 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_add_unless
- Explanation: atomic64_fetch_add_unless changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000032 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_and
- Explanation: atomic64_fetch_and changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000033 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_and_acquire
- Explanation: atomic64_fetch_and_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000034 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_and_relaxed
- Explanation: atomic64_fetch_and_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000035 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_and_release
- Explanation: atomic64_fetch_and_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000036 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_andnot
- Explanation: atomic64_fetch_andnot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000037 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_andnot_acquire
- Explanation: atomic64_fetch_andnot_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000038 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_andnot_relaxed
- Explanation: atomic64_fetch_andnot_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000039 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_andnot_release
- Explanation: atomic64_fetch_andnot_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000040 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_dec
- Explanation: atomic64_fetch_dec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000041 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_dec_acquire
- Explanation: atomic64_fetch_dec_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000042 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_dec_relaxed
- Explanation: atomic64_fetch_dec_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000043 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_dec_release
- Explanation: atomic64_fetch_dec_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000044 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_inc
- Explanation: atomic64_fetch_inc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000045 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_inc_acquire
- Explanation: atomic64_fetch_inc_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000046 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_inc_relaxed
- Explanation: atomic64_fetch_inc_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000047 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_inc_release
- Explanation: atomic64_fetch_inc_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000048 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_or
- Explanation: atomic64_fetch_or changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000049 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_or_acquire
- Explanation: atomic64_fetch_or_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000050 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_or_relaxed
- Explanation: atomic64_fetch_or_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000051 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_or_release
- Explanation: atomic64_fetch_or_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000052 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_sub
- Explanation: atomic64_fetch_sub changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000053 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_sub_acquire
- Explanation: atomic64_fetch_sub_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000054 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_sub_relaxed
- Explanation: atomic64_fetch_sub_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000055 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_sub_release
- Explanation: atomic64_fetch_sub_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000056 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_xor
- Explanation: atomic64_fetch_xor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000057 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_xor_acquire
- Explanation: atomic64_fetch_xor_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000058 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_xor_relaxed
- Explanation: atomic64_fetch_xor_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000059 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_fetch_xor_release
- Explanation: atomic64_fetch_xor_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000060 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_inc
- Explanation: atomic64_inc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000061 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_inc_and_test
- Explanation: atomic64_inc_and_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000062 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_inc_not_zero
- Explanation: atomic64_inc_not_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000063 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_inc_return
- Explanation: atomic64_inc_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000064 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_inc_return_acquire
- Explanation: atomic64_inc_return_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000065 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_inc_return_relaxed
- Explanation: atomic64_inc_return_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000066 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_inc_return_release
- Explanation: atomic64_inc_return_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000067 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_inc_unless_negative
- Explanation: atomic64_inc_unless_negative changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000068 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_or
- Explanation: atomic64_or changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000069 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_read
- Explanation: atomic64_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000070 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_read_acquire
- Explanation: atomic64_read_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000071 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_set
- Explanation: atomic64_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000072 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_set_release
- Explanation: atomic64_set_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000073 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_sub
- Explanation: atomic64_sub changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000074 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_sub_and_test
- Explanation: atomic64_sub_and_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000075 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_sub_return
- Explanation: atomic64_sub_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000076 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_sub_return_acquire
- Explanation: atomic64_sub_return_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000077 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_sub_return_relaxed
- Explanation: atomic64_sub_return_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000078 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_sub_return_release
- Explanation: atomic64_sub_return_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000079 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_try_cmpxchg
- Explanation: atomic64_try_cmpxchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000080 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_try_cmpxchg_acquire
- Explanation: atomic64_try_cmpxchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000081 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_try_cmpxchg_relaxed
- Explanation: atomic64_try_cmpxchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000082 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_try_cmpxchg_release
- Explanation: atomic64_try_cmpxchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000083 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_xchg
- Explanation: atomic64_xchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000084 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_xchg_acquire
- Explanation: atomic64_xchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000085 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_xchg_relaxed
- Explanation: atomic64_xchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000086 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_xchg_release
- Explanation: atomic64_xchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000087 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic64_xor
- Explanation: atomic64_xor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000088 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_add
- Explanation: atomic_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000089 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_add_negative
- Explanation: atomic_add_negative changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000090 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_add_negative_acquire
- Explanation: atomic_add_negative_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000091 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_add_negative_relaxed
- Explanation: atomic_add_negative_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000092 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_add_negative_release
- Explanation: atomic_add_negative_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000093 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_add_return
- Explanation: atomic_add_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000094 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_add_return_acquire
- Explanation: atomic_add_return_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000095 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_add_return_relaxed
- Explanation: atomic_add_return_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000096 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_add_return_release
- Explanation: atomic_add_return_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000097 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_add_unless
- Explanation: atomic_add_unless changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000098 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_and
- Explanation: atomic_and changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000099 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_andnot
- Explanation: atomic_andnot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000100 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_cmpxchg
- Explanation: atomic_cmpxchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000101 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_cmpxchg_acquire
- Explanation: atomic_cmpxchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000102 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_cmpxchg_relaxed
- Explanation: atomic_cmpxchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000103 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_cmpxchg_release
- Explanation: atomic_cmpxchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000104 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_dec
- Explanation: atomic_dec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000105 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_dec_and_test
- Explanation: atomic_dec_and_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000106 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_dec_if_positive
- Explanation: atomic_dec_if_positive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000107 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_dec_return
- Explanation: atomic_dec_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000108 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_dec_return_acquire
- Explanation: atomic_dec_return_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000109 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_dec_return_relaxed
- Explanation: atomic_dec_return_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000110 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_dec_return_release
- Explanation: atomic_dec_return_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000111 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_dec_unless_positive
- Explanation: atomic_dec_unless_positive changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000112 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_add
- Explanation: atomic_fetch_add changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000113 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_add_acquire
- Explanation: atomic_fetch_add_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000114 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_add_relaxed
- Explanation: atomic_fetch_add_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000115 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_add_release
- Explanation: atomic_fetch_add_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000116 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_add_unless
- Explanation: atomic_fetch_add_unless changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000117 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_and
- Explanation: atomic_fetch_and changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000118 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_and_acquire
- Explanation: atomic_fetch_and_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000119 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_and_relaxed
- Explanation: atomic_fetch_and_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000120 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_and_release
- Explanation: atomic_fetch_and_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000121 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_andnot
- Explanation: atomic_fetch_andnot changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000122 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_andnot_acquire
- Explanation: atomic_fetch_andnot_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000123 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_andnot_relaxed
- Explanation: atomic_fetch_andnot_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000124 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_andnot_release
- Explanation: atomic_fetch_andnot_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000125 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_dec
- Explanation: atomic_fetch_dec changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000126 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_dec_acquire
- Explanation: atomic_fetch_dec_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000127 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_dec_relaxed
- Explanation: atomic_fetch_dec_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000128 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_dec_release
- Explanation: atomic_fetch_dec_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000129 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_inc
- Explanation: atomic_fetch_inc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000130 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_inc_acquire
- Explanation: atomic_fetch_inc_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000131 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_inc_relaxed
- Explanation: atomic_fetch_inc_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000132 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_inc_release
- Explanation: atomic_fetch_inc_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000133 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_or
- Explanation: atomic_fetch_or changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000134 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_or_acquire
- Explanation: atomic_fetch_or_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000135 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_or_relaxed
- Explanation: atomic_fetch_or_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000136 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_or_release
- Explanation: atomic_fetch_or_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000137 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_sub
- Explanation: atomic_fetch_sub changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000138 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_sub_acquire
- Explanation: atomic_fetch_sub_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000139 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_sub_relaxed
- Explanation: atomic_fetch_sub_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000140 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_sub_release
- Explanation: atomic_fetch_sub_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000141 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_xor
- Explanation: atomic_fetch_xor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000142 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_xor_acquire
- Explanation: atomic_fetch_xor_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000143 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_xor_relaxed
- Explanation: atomic_fetch_xor_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000144 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_fetch_xor_release
- Explanation: atomic_fetch_xor_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000145 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_inc
- Explanation: atomic_inc changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000146 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_inc_and_test
- Explanation: atomic_inc_and_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000147 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_inc_not_zero
- Explanation: atomic_inc_not_zero changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000148 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_inc_return
- Explanation: atomic_inc_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000149 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_inc_return_acquire
- Explanation: atomic_inc_return_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000150 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_inc_return_relaxed
- Explanation: atomic_inc_return_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000151 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_inc_return_release
- Explanation: atomic_inc_return_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000152 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_inc_unless_negative
- Explanation: atomic_inc_unless_negative changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000153 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_or
- Explanation: atomic_or changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000154 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_read
- Explanation: atomic_read changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000155 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_read_acquire
- Explanation: atomic_read_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000156 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_set
- Explanation: atomic_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000157 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_set_release
- Explanation: atomic_set_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000158 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_sub
- Explanation: atomic_sub changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000159 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_sub_and_test
- Explanation: atomic_sub_and_test changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000160 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_sub_return
- Explanation: atomic_sub_return changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000161 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_sub_return_acquire
- Explanation: atomic_sub_return_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000162 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_sub_return_relaxed
- Explanation: atomic_sub_return_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000163 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_sub_return_release
- Explanation: atomic_sub_return_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000164 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_try_cmpxchg
- Explanation: atomic_try_cmpxchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000165 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_try_cmpxchg_acquire
- Explanation: atomic_try_cmpxchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000166 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_try_cmpxchg_relaxed
- Explanation: atomic_try_cmpxchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000167 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_try_cmpxchg_release
- Explanation: atomic_try_cmpxchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000168 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_xchg
- Explanation: atomic_xchg changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000169 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_xchg_acquire
- Explanation: atomic_xchg_acquire changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000170 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_xchg_relaxed
- Explanation: atomic_xchg_relaxed changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000171 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_xchg_release
- Explanation: atomic_xchg_release changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`

## W-000172 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: atomic_xor
- Explanation: atomic_xor changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `fdd7c7e0d2ab3987882c570612d4622f437292c7`
