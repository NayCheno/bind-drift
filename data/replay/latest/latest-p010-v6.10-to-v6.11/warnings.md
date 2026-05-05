# BindDrift Ranked Warnings

## W-000009 SignatureDrift

- Risk: High
- Score: 18.0
- Symbol: ERR_PTR
- Explanation: ERR_PTR changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `{'params': ['-ENODEV'], 'return_type': 'return'}`
- New: `{'params': ['-EINVAL'], 'return_type': 'return'}`

### Score Breakdown

- direct_rust_use: `4.0`
- safe_api_exposure: `4.0`
- safety_comment: `3.0`
- c_source_diff_strength: `3.0`
- wrapper_fix_hit: `4.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/error.rs:139 `Error::to_blk_status` unsafe=1
- safe API `Error::to_blk_status`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/error.rs:135 `/// Returns the error encoded as a pointer.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/error.rs:138 `// SAFETY: `self.0` is a valid error due to its invariant.`
- wrapper_fix: `c7e20faa5fcad7a177cf6c306138010343dd6d3e`
- wrapper_fix: `7bc186731e87482662c4f86da455f435fe838fb6`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`

## W-000003 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: device_add_disk
- Explanation: device_add_disk changed across the selected Linux versions.
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

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/block/mq/gen_disk.rs:160 `GenDiskBuilder::capacity_sectors` unsafe=1
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/block/mq/gen_disk.rs:179 `None` unsafe=0
- safe API `GenDiskBuilder::capacity_sectors`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/block/mq/gen_disk.rs:157 `// SAFETY: `gendisk` points to a valid and initialized instance of`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/block/mq/gen_disk.rs:174 `///`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/block/mq/gen_disk.rs:175 `/// # Invariants`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/block/mq/gen_disk.rs:156 `TO_RESULT_MAPPING`
- wrapper_fix: `0c5928deada15a8d075516e6e0d9ee19011bb000`

## W-000005 SignatureDrift

- Risk: Medium
- Score: 10.0
- Symbol: firmware_request_nowarn
- Explanation: firmware_request_nowarn changed across the selected Linux versions.
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

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:12 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:24 `request_nowarn` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:80 `Firmware::request` unsafe=0
- safe API `Firmware::request`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:28 `/// Abstraction around a C `struct firmware`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:29 `///`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:79 `/// Send a request for an optional firmware module. See also`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:75 `RESULT_RETURN`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

## W-000004 SignatureDrift

- Risk: Low
- Score: 7.0
- Symbol: errno_to_blk_status
- Explanation: errno_to_blk_status changed across the selected Linux versions.
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

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/error.rs:132 `Error::to_blk_status` unsafe=1
- safe API `Error::to_blk_status`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/error.rs:131 `// SAFETY: `self.0` is a valid error due to its invariant.`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`

## W-000007 SignatureDrift

- Risk: Low
- Score: 6.0
- Symbol: request_firmware
- Explanation: request_firmware changed across the selected Linux versions.
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

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:12 `None` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:20 `request` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:74 `request_internal` unsafe=0
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:69 `// SAFETY: `func` not bailing out with a non-zero error code, guarantees that `fw` is a`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:74 `/// Send a firmware request and wait for it. See also `bindings::request_firmware`.`
- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:71 `NONNULL_MAPPING`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

## W-000006 SignatureDrift

- Risk: Low
- Score: 0.0
- Symbol: firmware_request_platform
- Explanation: firmware_request_platform changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:13 `None` unsafe=0
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

## W-000008 SignatureDrift

- Risk: Low
- Score: 0.0
- Symbol: request_firmware_direct
- Explanation: request_firmware_direct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- /home/nya/workspace/bind-drift/.binddrift/worktrees/v6.11/rust/kernel/firmware.rs:13 `None` unsafe=0
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

## W-000001 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: blk_queue_flag_clear
- Explanation: blk_queue_flag_clear changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `5ddb88f22eb97218d9295e69c39e0ff7cc64e09c`

## W-000002 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: blk_queue_flag_set
- Explanation: blk_queue_flag_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- wrapper_fix_hit: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `5ddb88f22eb97218d9295e69c39e0ff7cc64e09c`
