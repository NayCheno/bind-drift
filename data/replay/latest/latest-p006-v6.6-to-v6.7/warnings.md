# BindDrift Ranked Warnings

## W-000002 FieldDrift

- Risk: Low
- Score: -5.0
- Symbol: kunit_case
- Explanation: kunit_case changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `[{'name': 'run_case', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'generate_params', 'type': '::core::option::Option<'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'module_name', 'type': '*mut core::ffi::c_char'}, {'name': 'log', 'type': '*mut core::ffi::c_char'}]`
- New: `[{'name': 'run_case', 'type': '::core::option::Option<unsafe extern "C" fn(test: *mut kunit)>'}, {'name': 'name', 'type': '*const core::ffi::c_char'}, {'name': 'generate_params', 'type': '::core::option::Option<'}, {'name': 'attr', 'type': 'kunit_attributes'}, {'name': 'status', 'type': 'kunit_status'}, {'name': 'module_name', 'type': '*mut core::ffi::c_char'}, {'name': 'log', 'type': '*mut string_stream'}]`

### Score Breakdown

- binding_only_penalty: `-5.0`

### Rust Evidence

- wrapper_fix: `7f87c7a003125d5af5ec7abbbc0ac21b4a4661ae`
- wrapper_fix: `be97f3c82021239476ce32cddde32948c597753e`

## W-000001 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: compat_ptr_ioctl
- Explanation: compat_ptr_ioctl changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `68aabb29a5469e4b7358e70e64a7fac433e27f06`
