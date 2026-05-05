# BindDrift Ranked Warnings

## W-000001 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: REFCOUNT_INIT
- Explanation: REFCOUNT_INIT changed across the selected Linux versions.
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

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:156 `Arc<T>::try_new` unsafe=1
- safe API `Arc<T>::try_new`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:151 `/// Constructs a new reference counted instance of `T`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:155 `// SAFETY: There are no safety requirements for this FFI call.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:152 `RESULT_RETURN`
- weak lifetime name /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:156 `LIFETIME_NAMING_PATTERN`
- wrapper_fix: `bb38f35b35f9de0cebc4d62ea73482454e38cef3`
- wrapper_fix: `076acb647c1f448177d8b3b0e4f33de959713d7d`
- wrapper_fix: `9ba1aaf25ab7dadb910348b6857865e87b4c5689`

## W-000002 SignatureDrift

- Risk: Low
- Score: 3.0
- Symbol: refcount_dec_and_test
- Explanation: refcount_dec_and_test changed across the selected Linux versions.
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

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:255 `drop` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:254 `// SAFETY: Also by the type invariant, we are allowed to decrement the refcount.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:259 `// SAFETY: The pointer was initialised from the result of `Box::leak`.`
- weak lifetime name /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:255 `LIFETIME_NAMING_PATTERN`
- wrapper_fix: `bb38f35b35f9de0cebc4d62ea73482454e38cef3`
- wrapper_fix: `076acb647c1f448177d8b3b0e4f33de959713d7d`
- wrapper_fix: `9ba1aaf25ab7dadb910348b6857865e87b4c5689`

## W-000003 SignatureDrift

- Risk: Low
- Score: 3.0
- Symbol: refcount_inc
- Explanation: refcount_inc changed across the selected Linux versions.
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

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:237 `clone` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:235 `// SAFETY: By the type invariant, there is necessarily a reference to the object, so it is`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:239 `// SAFETY: We just incremented the refcount. This increment is now owned by the new `Arc`.`
- weak lifetime name /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.3/rust/kernel/sync/arc.rs:237 `LIFETIME_NAMING_PATTERN`
- wrapper_fix: `bb38f35b35f9de0cebc4d62ea73482454e38cef3`
- wrapper_fix: `076acb647c1f448177d8b3b0e4f33de959713d7d`
- wrapper_fix: `9ba1aaf25ab7dadb910348b6857865e87b4c5689`
