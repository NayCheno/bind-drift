# BindDrift Ranked Warnings

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

- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:327 `Bitmap::set_bit_atomic` unsafe=1
- safe API `Bitmap::set_bit_atomic`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:325 `// SAFETY: `index` is within bounds and the caller has ensured that`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:330 `/// Clear `index` bit.`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:331 `///`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:327 `AS_PTR`
- wrapper_fix: `6cf93a9ed39e9f86c7f69c28078500270e70a695`
- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`

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

- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:406 `Bitmap::copy_and_extend` unsafe=1
- safe API `Bitmap::copy_and_extend`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:404 `// SAFETY: access to `self` and `src` is within bounds.`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:408 `AS_PTR`
- wrapper_fix: `0452b4ab2961093f23bb289b0112351b917fb23c`
- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`

## W-000174 SignatureDrift

- Risk: Low
- Score: 6.0
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
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:378 `Bitmap::clear_bit_atomic` unsafe=1
- safe API `Bitmap::clear_bit_atomic`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:376 `// SAFETY: `index` is within bounds and the caller has ensured that`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:381 `/// Copy `src` into this [`Bitmap`] and set any remaining bits to zero.`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:382 `///`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:378 `AS_PTR`
- wrapper_fix: `6cf93a9ed39e9f86c7f69c28078500270e70a695`
- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`
- wrapper_fix: `6a069876eb1402478900ee0eb7d7fe276bb1f4e3`

## W-000175 SignatureDrift

- Risk: Low
- Score: 6.0
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
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:81 `Refcount::dec` unsafe=1
- safe API `Refcount::dec`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:76 `/// Provides release memory ordering, such that prior loads and stores are done`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:77 `/// before.`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:80 `// SAFETY: `self.as_ptr()` is valid.`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:80 `AS_PTR`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:81 `AS_PTR`
- wrapper_fix: `bb38f35b35f9de0cebc4d62ea73482454e38cef3`
- wrapper_fix: `9ba1aaf25ab7dadb910348b6857865e87b4c5689`

## W-000176 SignatureDrift

- Risk: Low
- Score: 6.0
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
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:56 `Refcount::set` unsafe=1
- safe API `Refcount::set`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:52 `/// Set a refcount's value.`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:55 `// SAFETY: `self.as_ptr()` is valid.`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:59 `/// Increment a refcount.`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:55 `AS_PTR`
- .binddrift/worktrees/v6.18/rust/kernel/sync/refcount.rs:56 `AS_PTR`
- wrapper_fix: `bb38f35b35f9de0cebc4d62ea73482454e38cef3`
- wrapper_fix: `9ba1aaf25ab7dadb910348b6857865e87b4c5689`

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

- .binddrift/worktrees/v6.18/rust/kernel/kunit.rs:202 `is_test_result_ok` unsafe=0
- .binddrift/worktrees/v6.18/rust/kernel/kunit.rs:203 `is_test_result_ok` unsafe=0
- .binddrift/worktrees/v6.18/rust/kernel/kunit.rs:223 `kunit_case_null` unsafe=0
- .binddrift/worktrees/v6.18/rust/kernel/kunit.rs:224 `kunit_case_null` unsafe=0
- .binddrift/worktrees/v6.18/rust/kernel/kunit.rs:296 `test_fn` unsafe=1
- safe API `is_test_result_ok`
- .binddrift/worktrees/v6.18/rust/kernel/kunit.rs:197 `/// Use [`kunit_case_null`] to generate such a delimiter.`
- .binddrift/worktrees/v6.18/rust/kernel/kunit.rs:218 `/// Represents the NULL test case delimiter.`
- .binddrift/worktrees/v6.18/rust/kernel/kunit.rs:219 `///`
- wrapper_fix: `7f87c7a003125d5af5ec7abbbc0ac21b4a4661ae`
- wrapper_fix: `be97f3c82021239476ce32cddde32948c597753e`

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

- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:351 `Bitmap::clear_bit` unsafe=1
- safe API `Bitmap::clear_bit`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:350 `// SAFETY: `index` is within bounds.`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:354 `/// Clear `index` bit, atomically.`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:355 `///`
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

- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:300 `Bitmap::set_bit` unsafe=1
- safe API `Bitmap::set_bit`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:299 `// SAFETY: Bit `index` is within bounds.`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:303 `/// Set bit with index `index`, atomically.`
- .binddrift/worktrees/v6.18/rust/kernel/bitmap.rs:304 `///`
- wrapper_fix: `6cf93a9ed39e9f86c7f69c28078500270e70a695`
- wrapper_fix: `11eca92a2caebcc2b3b65ca290385ff4b0498946`

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
