# False-Positive Taxonomy

This analysis explains false-positive risk for the pooled review set. It is used to support a top-K review-prioritization claim, not an overall warning-set precision claim.

## Ranking Metrics

- `p_at_10`: `1.0`
- `p_at_20`: `1.0`
- `p_at_50`: `0.86`
- `p_at_100`: `0.43`
- `ndcg_at_20`: `1.0`
- `auprc_on_pooled_review_set`: `0.9013`

## Taxonomy

- Pooled rows: `800`
- `FALSE_POSITIVE` rows: `530`
- `BENIGN_DRIFT` rows: `219`

### `binding_only_or_generated_surface`

Count: `309`

- `F-000010` `latest-p001-v6.1-to-v6.2` `apply_fineibt`: Unsupported generated binding target calibration is present; adjudicated FALSE_POSITIVE per v3 policy.
- `F-000011` `latest-p001-v6.1-to-v6.2` `callthunks_patch_builtin_calls`: Unsupported generated binding target calibration is present; adjudicated FALSE_POSITIVE per v3 policy.
- `F-000012` `latest-p001-v6.1-to-v6.2` `callthunks_patch_module_calls`: Unsupported generated binding target calibration is present; adjudicated FALSE_POSITIVE per v3 policy.

### `layout_ambiguity`

Count: `94`

- `F-000040` `latest-p001-v6.1-to-v6.2` `folio`: Unsupported generated binding target calibration is present; adjudicated FALSE_POSITIVE per v3 policy.
- `F-000041` `latest-p001-v6.1-to-v6.2` `mm_struct__bindgen_ty_1`: Unsupported generated binding target calibration is present; adjudicated FALSE_POSITIVE per v3 policy.
- `F-000044` `latest-p001-v6.1-to-v6.2` `page__bindgen_ty_1__bindgen_ty_5`: Unsupported generated binding target calibration is present; adjudicated FALSE_POSITIVE per v3 policy.

### `macro_constant_over_prioritization`

Count: `107`

- `F-000050` `latest-p001-v6.1-to-v6.2` `ENDBR_INSN_SIZE`: Unsupported generated binding target calibration is present; adjudicated FALSE_POSITIVE per v3 policy.
- `F-000054` `latest-p001-v6.1-to-v6.2` `PERCPU_DYNAMIC_EARLY_SIZE`: Unsupported generated binding target calibration is present; adjudicated FALSE_POSITIVE per v3 policy.
- `F-000056` `latest-p001-v6.1-to-v6.2` `pageflags___NR_PAGEFLAGS`: Unsupported generated binding target calibration is present; adjudicated FALSE_POSITIVE per v3 policy.

### `real_c_drift_no_rust_contract_impact`

Count: `219`

- `W-000018` `latest-p012-v6.12-to-v6.13` `errno_to_blk_status`: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.
- `W-000019` `latest-p012-v6.12-to-v6.13` `firmware_request_nowarn`: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.
- `W-000003` `latest-p012-v6.12-to-v6.13` `PTR_ERR`: Reviewer 1 BENIGN_DRIFT vs Reviewer 2 UNCLEAR falls in the broad-family wrapper/Rust-exposure calibration class; real context exists, but no direct same-contract wrapper oracle or semantic-drift rule is satisfied, so BENIGN_DRIFT per v3 policy.

### `weak_rust_reachability`

Count: `20`

- `F-000002` `latest-p001-v6.1-to-v6.2` `__percpu_counter_compare`: Unsupported generated binding target calibration is present; adjudicated FALSE_POSITIVE per v3 policy.
- `F-000003` `latest-p001-v6.1-to-v6.2` `__percpu_counter_init`: Unsupported generated binding target calibration is present; adjudicated FALSE_POSITIVE per v3 policy.
- `F-000004` `latest-p001-v6.1-to-v6.2` `__percpu_counter_sum`: Unsupported generated binding target calibration is present; adjudicated FALSE_POSITIVE per v3 policy.
