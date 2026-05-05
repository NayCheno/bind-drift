# Positive: LayoutFieldDrift for `queue_limits`

## Summary

`queue_limits` produced `W-000016` and is included as an adjudicated positive review target with label `TRUE_WRAPPER_FIX`.

## Old Version Evidence

- Version: `v6.13`
- Old value or indicators: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

## New Version Evidence

- Version: `v6.14`
- New value or indicators: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

## C-Side Diff

- Old indicators/value: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`
- New indicators/value: `[{'name': 'features', 'type': 'blk_features_t'}, {'name': 'flags', 'type': 'blk_flags_t'}, {'name': 'seg_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'virt_boundary_mask', 'type': 'ffi::c_ulong'}, {'name': 'max_hw_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_dev_sectors', 'type': 'ffi::c_uint'}, {'name': 'chunk_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_segment_size', 'type': 'ffi::c_uint'}, {'name': 'min_segment_size', 'type': 'ffi::c_uint'}, {'name': 'physical_block_size', 'type': 'ffi::c_uint'}, {'name': 'logical_block_size', 'type': 'ffi::c_uint'}, {'name': 'alignment_offset', 'type': 'ffi::c_uint'}, {'name': 'io_min', 'type': 'ffi::c_uint'}, {'name': 'io_opt', 'type': 'ffi::c_uint'}, {'name': 'max_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_user_discard_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_secure_erase_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_write_zeroes_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_hw_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'max_zone_append_sectors', 'type': 'ffi::c_uint'}, {'name': 'discard_granularity', 'type': 'ffi::c_uint'}, {'name': 'discard_alignment', 'type': 'ffi::c_uint'}, {'name': 'zone_write_granularity', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_max_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_boundary', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_boundary_sectors', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_min', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_hw_unit_max', 'type': 'ffi::c_uint'}, {'name': 'atomic_write_unit_max', 'type': 'ffi::c_uint'}, {'name': 'max_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_integrity_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_discard_segments', 'type': 'ffi::c_ushort'}, {'name': 'max_open_zones', 'type': 'ffi::c_uint'}, {'name': 'max_active_zones', 'type': 'ffi::c_uint'}, {'name': 'dma_alignment', 'type': 'ffi::c_uint'}, {'name': 'dma_pad_mask', 'type': 'ffi::c_uint'}, {'name': 'integrity', 'type': 'blk_integrity'}]`

## Rust-Side Dependency

- `.binddrift/worktrees/v6.14/rust/kernel/block/mq/gen_disk.rs:96` in `GenDiskBuilder::capacity_sectors`
- `.binddrift/worktrees/v6.14/rust/kernel/block/mq/gen_disk.rs:97` in `GenDiskBuilder::capacity_sectors`
- safe API `GenDiskBuilder::capacity_sectors`
- `.binddrift/worktrees/v6.14/rust/kernel/block/mq/gen_disk.rs:96`: `// SAFETY: `bindings::queue_limits` contain only fields that are valid when zeroed.`
- `.binddrift/worktrees/v6.14/rust/kernel/block/mq/gen_disk.rs:95` error mapping `RESULT_RETURN`
- wrapper_fix: `5e3b7009f116f684ac6b93d8924506154f3b1f6d`

## Safe API / Contract Assumption

The warning reaches a public safe Rust API, so the maintainer review question is whether that API's documented contract remains synchronized with the C-side behavior.

## Manual Review Label

- Adjudicated label: `TRUE_WRAPPER_FIX`
- Reviewer 1: `TRUE_WRAPPER_FIX` -- The queue_limits field drift reaches a Rust safe API path in block gen_disk, and the oracle directly says Rust block code stopped using removed queue limit APIs. The fix commit matches queue_limits and rust/kernel/block/mq/gen_disk.rs, which is the same exposure path.
- Reviewer 2: `TRUE_WRAPPER_FIX` -- queue_limits reaches GenDiskBuilder::capacity_sectors, whose safety comment says zeroed queue_limits fields are valid. The wrapper-fix oracle changes the same gen_disk.rs file and is specifically about not using removed queue limit APIs.
- Adjudication: queue_limits reaches GenDiskBuilder::capacity_sectors, whose safety comment relies on zero-valid queue_limits fields. 5e3b7009f116 directly changes rust/kernel/block/mq/gen_disk.rs to avoid removed queue limit APIs and matches queue_limits. No build log is present.

## Why This Is Not Generated-Binding-Only

The case has Rust reachability or contract/oracle evidence beyond a generated binding delta; generated-binding-only rows are excluded from positive case selection.

## Why Compiler Alone Does Not Catch It

The compiler checks the current Rust/C binding shape. This case is about whether a Rust abstraction, helper, or safety invariant remains synchronized with an evolving C-side contract across versions.

## Alternative Explanation Considered

Review considered whether this was semantic drift; adjudication classifies it as wrapper-fix-backed validation instead of standalone semantic evidence.

## Maintainer Review Implication

A maintainer should inspect the Rust wrapper or safe abstraction path when carrying this C-side change across versions.

## Reproduction Pointers

- Warning: `W-000016`
- Warning UID: `d8a8b6a3a16e833d8d47b8d4164dff971b6c69bc11ddb2d48d8385c6a002dac0`
- Replay pair: `latest-p013-v6.13-to-v6.14`
- Drift type: `LayoutFieldDrift`
- C symbol: `queue_limits`
- Risk: `High`
- Score: `15.0`
