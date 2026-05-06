# False-Positive Taxonomy

This analysis explains false-positive risk for the pooled review set. It is used to support a top-K review-prioritization claim, not an overall warning-set precision claim.

## Ranking Metrics

- `p_at_10`: `1.0`
- `p_at_20`: `1.0`
- `p_at_50`: `0.86`
- `p_at_100`: `0.43`
- `ndcg_at_20`: `1.0`
- `auprc_on_pooled_review_set`: `0.9444`

## Taxonomy

- Pooled rows: `500`
- `FALSE_POSITIVE` rows: `450`
- `BENIGN_DRIFT` rows: `3`

### `binding_only_or_generated_surface`

Count: `54`

- `W-000016` `latest-p012-v6.12-to-v6.13` `device_add_disk`: device_add_disk: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.
- `W-000177` `latest-p017-v6.17-to-v6.18` `set_bit`: set_bit: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.
- `W-000018` `latest-p012-v6.12-to-v6.13` `errno_to_blk_status`: errno_to_blk_status: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.

### `layout_ambiguity`

Count: `61`

- `W-000178` `latest-p017-v6.17-to-v6.18` `kunit_case`: kunit_case: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.
- `W-000001` `latest-p018-v6.18-to-v6.19` `queue_limits`: queue_limits: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.
- `W-000016` `latest-p013-v6.13-to-v6.14` `queue_limits`: queue_limits: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.

### `macro_constant_over_prioritization`

Count: `60`

- `W-000004` `latest-p012-v6.12-to-v6.13` `REFCOUNT_INIT`: REFCOUNT_INIT: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.
- `W-000003` `latest-p012-v6.12-to-v6.13` `PTR_ERR`: PTR_ERR: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.
- `W-000002` `latest-p012-v6.12-to-v6.13` `IS_ERR`: IS_ERR: broad-family wrapper evidence is auxiliary only. Without direct same-symbol/same-contract proof or a semantic C-to-Rust contract chain, the warning is unsupported as a Rust-impact target.

### `real_c_drift_no_rust_contract_impact`

Count: `3`

- `F-000825` `latest-p008-v6.8-to-v6.9` `SLAB_NO_MERGE`: SLAB_NO_MERGE: C-side drift is supported, but Rust impact evidence is absent or limited to generated exposure, so it is real but harmless for Rust.
- `F-001020` `latest-p018-v6.18-to-v6.19` `VM_STACK_EARLY`: VM_STACK_EARLY: C-side drift is supported, but Rust impact evidence is absent or limited to generated exposure, so it is real but harmless for Rust.
- `F-000613` `latest-p020-v7.0-to-HEAD_9207d47f966b` `vfs_llseek`: vfs_llseek: C-side drift is supported, but Rust impact evidence is absent or limited to generated exposure, so it is real but harmless for Rust.

### `weak_rust_reachability`

Count: `275`

- `F-000003` `latest-p001-v6.1-to-v6.2` `__percpu_counter_init`: __percpu_counter_init: packet marks an unsupported generated-binding target with no direct C proof, no Rust contract dependence, and no build or direct wrapper oracle.
- `F-000023` `latest-p001-v6.1-to-v6.2` `percpu_counter_add_batch`: percpu_counter_add_batch: packet marks an unsupported generated-binding target with no direct C proof, no Rust contract dependence, and no build or direct wrapper oracle.
- `F-000025` `latest-p001-v6.1-to-v6.2` `percpu_counter_set`: percpu_counter_set: packet marks an unsupported generated-binding target with no direct C proof, no Rust contract dependence, and no build or direct wrapper oracle.
