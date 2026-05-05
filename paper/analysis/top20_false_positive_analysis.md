# Top-20 False Positive Analysis

This analysis covers false positives in the oracle-blind top-20 ranking. Warnings remain review targets, not confirmed bugs.

- Primary P@10: 0.3
- Ranking claim: evidence gate claim only; ranking improvement not supported
- Top-20 false positives: 7

## Rank 1: PTR_ERR (SignatureDrift)

- Warning: `W-000006`
- Pair: `latest-p015-v6.15-to-v6.16`
- Score: `16.75`
- Tier: `A`
- Failure taxonomy: `generic_error_pointer_helper_overprioritized`
- Dominant components: `c_source_diff=2.0`, `contract_evidence=2.0`, `rust_direct_use=2.0`
- Audit note: high C/Rust reachability evidence was not sufficient to establish supported Rust contract impact under adjudication.

## Rank 2: ERR_PTR (SignatureDrift)

- Warning: `W-000009`
- Pair: `latest-p010-v6.10-to-v6.11`
- Score: `16.4`
- Tier: `A`
- Failure taxonomy: `generic_error_pointer_helper_overprioritized`
- Dominant components: `c_source_diff=2.0`, `contract_evidence=2.0`, `rust_direct_use=2.0`
- Audit note: high C/Rust reachability evidence was not sufficient to establish supported Rust contract impact under adjudication.

## Rank 4: kmap_local_page (SignatureDrift)

- Warning: `W-000003`
- Pair: `latest-p014-v6.14-to-v6.15`
- Score: `15.75`
- Tier: `A`
- Failure taxonomy: `signature_change_without_supported_rust_contract_impact`
- Dominant components: `c_source_diff=2.0`, `contract_evidence=2.0`, `rust_direct_use=2.0`
- Audit note: high C/Rust reachability evidence was not sufficient to establish supported Rust contract impact under adjudication.

## Rank 5: resource_size_t (SignatureDrift)

- Warning: `W-000011`
- Pair: `latest-p020-v7.0-to-HEAD_6d35786de281`
- Score: `15.75`
- Tier: `A`
- Failure taxonomy: `signature_change_without_supported_rust_contract_impact`
- Dominant components: `c_source_diff=2.0`, `contract_evidence=2.0`, `rust_direct_use=2.0`
- Audit note: high C/Rust reachability evidence was not sufficient to establish supported Rust contract impact under adjudication.

## Rank 6: vma_lookup (SignatureDrift)

- Warning: `W-000181`
- Pair: `latest-p017-v6.17-to-v6.18`
- Score: `15.75`
- Tier: `A`
- Failure taxonomy: `signature_change_without_supported_rust_contract_impact`
- Dominant components: `c_source_diff=2.0`, `contract_evidence=2.0`, `rust_direct_use=2.0`
- Audit note: high C/Rust reachability evidence was not sufficient to establish supported Rust contract impact under adjudication.

## Rank 9: queue_work_on (SignatureDrift)

- Warning: `W-000180`
- Pair: `latest-p017-v6.17-to-v6.18`
- Score: `14.05`
- Tier: `A`
- Failure taxonomy: `signature_change_without_supported_rust_contract_impact`
- Dominant components: `c_source_diff=2.0`, `contract_evidence=2.0`, `rust_direct_use=2.0`
- Audit note: high C/Rust reachability evidence was not sufficient to establish supported Rust contract impact under adjudication.

## Rank 10: dev_get_drvdata (SignatureDrift)

- Warning: `W-000028`
- Pair: `latest-p018-v6.18-to-v6.19`
- Score: `13.4`
- Tier: `A`
- Failure taxonomy: `signature_change_without_supported_rust_contract_impact`
- Dominant components: `c_source_diff=2.0`, `contract_evidence=2.0`, `rust_direct_use=2.0`
- Audit note: high C/Rust reachability evidence was not sufficient to establish supported Rust contract impact under adjudication.
