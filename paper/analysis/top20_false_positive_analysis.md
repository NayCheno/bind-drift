# Top-20 False Positive Analysis

This analysis covers false positives in the oracle-blind top-20 ranking. Warnings remain review targets, not confirmed bugs.

- Primary P@10: 0.9
- Ranking claim: ranking improvement claim may be considered only if baseline lift gate also passes
- Top-20 false positives: 3

## Rank 10: device_add_disk (SignatureDrift)

- Warning: `W-000016`
- Pair: `latest-p012-v6.12-to-v6.13`
- Score: `18.15`
- Tier: `C`
- Failure taxonomy: `signature_change_without_supported_rust_contract_impact`
- Dominant components: `rust_direct_use=4.0`, `safety_comment_proximity=3.0`, `safe_api_exposure=2.5`
- Audit note: high C/Rust reachability evidence was not sufficient to establish supported Rust contract impact under adjudication.

## Rank 13: set_bit (SignatureDrift)

- Warning: `W-000177`
- Pair: `latest-p017-v6.17-to-v6.18`
- Score: `16.65`
- Tier: `C`
- Failure taxonomy: `signature_change_without_supported_rust_contract_impact`
- Dominant components: `rust_direct_use=4.0`, `safety_comment_proximity=3.0`, `safe_api_exposure=2.5`
- Audit note: high C/Rust reachability evidence was not sufficient to establish supported Rust contract impact under adjudication.

## Rank 15: errno_to_blk_status (SignatureDrift)

- Warning: `W-000018`
- Pair: `latest-p012-v6.12-to-v6.13`
- Score: `15.8`
- Tier: `C`
- Failure taxonomy: `signature_change_without_supported_rust_contract_impact`
- Dominant components: `rust_direct_use=4.0`, `safety_comment_proximity=3.0`, `safe_api_exposure=2.5`
- Audit note: high C/Rust reachability evidence was not sufficient to establish supported Rust contract impact under adjudication.
