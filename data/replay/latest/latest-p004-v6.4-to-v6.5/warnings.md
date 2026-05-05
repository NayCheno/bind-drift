# BindDrift Ranked Warnings

## W-000001 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: errname
- Explanation: errname changed across the selected Linux versions.
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

- .binddrift/worktrees/v6.5/rust/kernel/error.rs:144 `Error::name` unsafe=1
- safe API `Error::name`
- safe API `Error::name`
- .binddrift/worktrees/v6.5/rust/kernel/error.rs:140 `/// Returns a string representing the error, if one exists.`
- .binddrift/worktrees/v6.5/rust/kernel/error.rs:143 `// SAFETY: Just an FFI call, there are no extra safety requirements.`
- .binddrift/worktrees/v6.5/rust/kernel/error.rs:148 `// SAFETY: The string returned by `errname` is static and `NUL`-terminated.`
- .binddrift/worktrees/v6.5/rust/kernel/error.rs:142 `OPTION_RETURN`
- wrapper_fix: `d2e3115d717197cb2bc020dd1f06b06538474ac3`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`
