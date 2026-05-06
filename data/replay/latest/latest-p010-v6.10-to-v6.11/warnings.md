# BindDrift Ranked Warnings

## W-000003 SignatureDrift

- Risk: Low
- Score: 6.0
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
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.11/rust/kernel/block/mq/gen_disk.rs:160 `GenDiskBuilder::capacity_sectors` unsafe=1
- safe API `GenDiskBuilder::capacity_sectors`
- .binddrift/worktrees/v6.11/rust/kernel/block/mq/gen_disk.rs:157 `// SAFETY: `gendisk` points to a valid and initialized instance of`
- .binddrift/worktrees/v6.11/rust/kernel/block/mq/gen_disk.rs:156 `TO_RESULT_MAPPING`
- wrapper_fix: `0c5928deada15a8d075516e6e0d9ee19011bb000`

## W-000004 SignatureDrift

- Risk: Low
- Score: 3.0
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
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.11/rust/kernel/error.rs:132 `Error::to_blk_status` unsafe=1
- safe API `Error::to_blk_status`
- .binddrift/worktrees/v6.11/rust/kernel/error.rs:131 `// SAFETY: `self.0` is a valid error due to its invariant.`
- wrapper_fix: `e9759c5b9ea555d09f426c70c880e9522e9b0576`

## W-000005 SignatureDrift

- Risk: Low
- Score: -1.0
- Symbol: firmware_request_nowarn
- Explanation: firmware_request_nowarn changed across the selected Linux versions.
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

- .binddrift/worktrees/v6.11/rust/kernel/firmware.rs:24 `request_nowarn` unsafe=0
- .binddrift/worktrees/v6.11/rust/kernel/firmware.rs:28 `/// Abstraction around a C `struct firmware`.`
- .binddrift/worktrees/v6.11/rust/kernel/firmware.rs:29 `///`
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

## W-000007 SignatureDrift

- Risk: Low
- Score: -4.0
- Symbol: request_firmware
- Explanation: request_firmware changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- direct_rust_use: `4.0`
- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- .binddrift/worktrees/v6.11/rust/kernel/firmware.rs:20 `request` unsafe=0
- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

## W-000001 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: blk_queue_flag_clear
- Explanation: blk_queue_flag_clear changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `5ddb88f22eb97218d9295e69c39e0ff7cc64e09c`

## W-000002 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: blk_queue_flag_set
- Explanation: blk_queue_flag_set changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `5ddb88f22eb97218d9295e69c39e0ff7cc64e09c`

## W-000006 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: firmware_request_platform
- Explanation: firmware_request_platform changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`

## W-000008 SignatureDrift

- Risk: Low
- Score: -8.0
- Symbol: request_firmware_direct
- Explanation: request_firmware_direct changed across the selected Linux versions.
- Suggested action: Inspect the Rust safe abstraction and generated binding for stale assumptions.

### C Evidence

- Old: `absent`
- New: `added`

### Score Breakdown

- binding_only_penalty: `-5.0`
- added_symbol_without_old_c_evidence_penalty: `-3.0`

### Rust Evidence

- wrapper_fix: `a23b018c3bf646274f02edd46bf448c20c826d94`
