# BindDrift Ranked Warnings

## W-000003 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: PTR_ERR
- Explanation: PTR_ERR changed across the selected Linux versions.
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

- .binddrift/worktrees/v6.4/rust/kernel/error.rs:225 `to_result` unsafe=1
- safe API `to_result`
- .binddrift/worktrees/v6.4/rust/kernel/error.rs:222 `// SAFETY: The FFI function does not deref the pointer.`
- .binddrift/worktrees/v6.4/rust/kernel/error.rs:224 `// SAFETY: The FFI function does not deref the pointer.`
- .binddrift/worktrees/v6.4/rust/kernel/error.rs:223 `IS_ERR_MAPPING`
- .binddrift/worktrees/v6.4/rust/kernel/error.rs:225 `PTR_ERR_MAPPING`
- wrapper_fix: `752417b3f0e7721f1d630f40da22d57e0dae043e`

## W-000001 SignatureDrift

- Risk: Low
- Score: 3.0
- Symbol: ERR_PTR
- Explanation: ERR_PTR changed across the selected Linux versions.
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

- .binddrift/worktrees/v6.4/rust/kernel/error.rs:114 `Error::to_errno` unsafe=1
- safe API `Error::to_errno`
- .binddrift/worktrees/v6.4/rust/kernel/error.rs:110 `/// Returns the error encoded as a pointer.`
- .binddrift/worktrees/v6.4/rust/kernel/error.rs:113 `// SAFETY: self.0 is a valid error due to its invariant.`
- wrapper_fix: `c7e20faa5fcad7a177cf6c306138010343dd6d3e`
- wrapper_fix: `7bc186731e87482662c4f86da455f435fe838fb6`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`

## W-000002 SignatureDrift

- Risk: Low
- Score: 3.0
- Symbol: IS_ERR
- Explanation: IS_ERR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- contract_mapping: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.4/rust/kernel/error.rs:223 `to_result` unsafe=1
- safe API `to_result`
- .binddrift/worktrees/v6.4/rust/kernel/error.rs:219 `ERR_PTR_MAPPING`
- wrapper_fix: `752417b3f0e7721f1d630f40da22d57e0dae043e`

## W-000004 SignatureDrift

- Risk: Low
- Score: 2.0
- Symbol: put_task_struct
- Explanation: put_task_struct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- contract_mapping: `3.0`
- safety_comment: `3.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.4/rust/kernel/task.rs:153 `dec_ref` unsafe=1
- .binddrift/worktrees/v6.4/rust/kernel/task.rs:152 `// SAFETY: The safety requirements guarantee that the refcount is nonzero.`
- .binddrift/worktrees/v6.4/rust/kernel/task.rs:153 `AS_PTR`
- wrapper_fix: `8ad1a41f7e23287f07a3516c700bc32501d4f104`
