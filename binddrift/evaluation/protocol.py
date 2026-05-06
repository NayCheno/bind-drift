from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.warnings import read_warnings
from binddrift.run_manifest import canonical_run_dir, repo_relative, sha256_file


PROTOCOL_NAME = "evaluation_protocol.json"
PROTOCOL_VERSION = "ccfb-strict-v2"
CLAIM_BOUNDARY = "evidence-backed warning prioritization"
PRIMARY_WARNING_SET = "oracle_blind_ranked_warnings"

FORBIDDEN_PRIMARY_SCORE_COMPONENTS = {
    "adjudicated_label",
    "build_oracle_hit",
    "build_oracle_label",
    "build_breakage_label",
    "label",
    "manual_label",
    "reviewer1_label",
    "reviewer2_label",
    "true_reason",
    "wrapper_fix_hit",
    "wrapper_fix_label",
}

FORBIDDEN_CLAIM_PHRASES = [
    "bug detector",
    "automatically detects bugs",
    "proves unsoundness",
    "outperforms all baselines",
    "complete detection",
]


class EvaluationProtocolError(RuntimeError):
    pass


def protocol_path(cfg: Config, run_id: str = "latest") -> Path:
    return canonical_run_dir(cfg, run_id) / PROTOCOL_NAME


def default_evaluation_protocol(run_id: str = "latest", pair_ids: list[str] | None = None) -> dict[str, Any]:
    pairs = pair_ids or [f"{run_id}-p{idx:03d}" for idx in range(1, 21)]
    return {
        "protocol_version": PROTOCOL_VERSION,
        "claim_boundary": CLAIM_BOUNDARY,
        "primary_warning_set": PRIMARY_WARNING_SET,
        "oracle_usage": {
            "wrapper_fix_oracle": "labels_and_auxiliary_validation_only",
            "build_oracle": "labels_and_auxiliary_validation_only",
            "not_allowed_in_primary_score": True,
        },
        "splits": {
            "dev_pairs": pairs[:10],
            "validation_pairs": pairs[10:15],
            "locked_test_pairs": pairs[15:],
        },
        "primary_metrics": [
            "P@10",
            "P@20",
            "P@50",
            "P@100",
            "NDCG@20",
            "AUPRC_on_pooled_review_set",
        ],
        "baseline_metrics": [
            "relative_lift_over_best_simple_baseline",
            "absolute_lift_over_random",
            "warning_volume_reduction",
        ],
        "manual_review_policy": {
            "double_review": True,
            "adjudication_required": True,
            "cohen_kappa_required": True,
            "unclear_is_not_true_positive": True,
            "review_method": "LLM-assisted independent double review with adjudication",
            "review_roles": ["evidence_collector", "reviewer1", "reviewer2", "adjudicator"],
            "reviewers_blind_to_ranker": True,
            "reviewers_blind_to_rank_and_score": True,
            "reviewers_blind_to_each_other": True,
            "reviewers_blind_to_oracles": False,
            "oracle_evidence_visibility": "build and wrapper evidence may be visible for labels, but remains auxiliary validation only",
            "label_source_for_metrics": "adjudicated_label",
            "cohen_kappa_minimum": 0.70,
            "agreement_rate_minimum": 0.80,
            "unclear_rate_maximum": 0.05,
            "reviewer_disagreement_examples_minimum": 10,
            "llm_assisted_boundary": {
                "not_human_expert_manual_review": True,
                "llm_participates_in_primary_score": False,
                "reviewer_roles_receive_adjudicated_labels": False,
            },
        },
        "locked_split_policy": {
            "locked_test_pairs_final_run_only": True,
            "manifest_records_locked_split_hash": True,
        },
    }


def warning_pair_ids(cfg: Config, run_id: str = "latest") -> list[str]:
    run_dir = canonical_run_dir(cfg, run_id)
    pair_ids = sorted(
        {
            str(warning.get("pair_id"))
            for warning in read_warnings(run_dir / "promoted_warnings.jsonl")
            if warning.get("pair_id")
        }
    )
    return pair_ids


def write_default_evaluation_protocol(cfg: Config, run_id: str = "latest") -> Path:
    path = protocol_path(cfg, run_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    pairs = warning_pair_ids(cfg, run_id)
    path.write_text(
        json.dumps(default_evaluation_protocol(run_id, pair_ids=pairs or None), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def load_evaluation_protocol(cfg: Config, run_id: str = "latest") -> dict[str, Any]:
    path = protocol_path(cfg, run_id)
    if not path.exists():
        raise EvaluationProtocolError(f"missing evaluation protocol: {path}")
    protocol = json.loads(path.read_text(encoding="utf-8"))
    validate_evaluation_protocol(protocol)
    validate_protocol_pair_splits(cfg, protocol, run_id=run_id)
    return {
        **protocol,
        "path": str(path),
        "repo_relative_path": repo_relative(cfg, path),
        "sha256": sha256_file(path),
    }


def validate_evaluation_protocol(protocol: dict[str, Any]) -> None:
    required = {
        "protocol_version",
        "claim_boundary",
        "primary_warning_set",
        "oracle_usage",
        "splits",
        "primary_metrics",
        "baseline_metrics",
        "manual_review_policy",
        "locked_split_policy",
    }
    missing = sorted(required - set(protocol))
    if missing:
        raise EvaluationProtocolError("evaluation_protocol missing fields: " + ", ".join(missing))
    if protocol["protocol_version"] != PROTOCOL_VERSION:
        raise EvaluationProtocolError(f"unsupported protocol_version: {protocol['protocol_version']}")
    if protocol["claim_boundary"] != CLAIM_BOUNDARY:
        raise EvaluationProtocolError(f"unsupported claim_boundary: {protocol['claim_boundary']}")
    if protocol["primary_warning_set"] != PRIMARY_WARNING_SET:
        raise EvaluationProtocolError(f"unsupported primary_warning_set: {protocol['primary_warning_set']}")
    oracle_usage = protocol.get("oracle_usage") or {}
    if oracle_usage.get("not_allowed_in_primary_score") is not True:
        raise EvaluationProtocolError("oracle_usage.not_allowed_in_primary_score must be true")
    policy = protocol.get("manual_review_policy") or {}
    for key in ("double_review", "adjudication_required", "cohen_kappa_required", "unclear_is_not_true_positive"):
        if policy.get(key) is not True:
            raise EvaluationProtocolError(f"manual_review_policy.{key} must be true")
    if policy.get("label_source_for_metrics") not in (None, "adjudicated_label"):
        raise EvaluationProtocolError("manual_review_policy.label_source_for_metrics must be adjudicated_label")
    for key in ("reviewers_blind_to_ranker", "reviewers_blind_to_rank_and_score", "reviewers_blind_to_each_other"):
        if key in policy and policy.get(key) is not True:
            raise EvaluationProtocolError(f"manual_review_policy.{key} must be true")
    if "reviewers_blind_to_oracles" in policy and policy.get("reviewers_blind_to_oracles") is not False:
        raise EvaluationProtocolError("manual_review_policy.reviewers_blind_to_oracles must be false when oracle evidence is label evidence")
    if policy.get("cohen_kappa_minimum", 0.70) < 0.70:
        raise EvaluationProtocolError("manual_review_policy.cohen_kappa_minimum must be at least 0.70")
    if policy.get("agreement_rate_minimum", 0.80) < 0.80:
        raise EvaluationProtocolError("manual_review_policy.agreement_rate_minimum must be at least 0.80")
    if policy.get("unclear_rate_maximum", 0.05) > 0.05:
        raise EvaluationProtocolError("manual_review_policy.unclear_rate_maximum must be at most 0.05")
    llm_boundary = policy.get("llm_assisted_boundary") or {}
    if llm_boundary:
        if llm_boundary.get("llm_participates_in_primary_score") is not False:
            raise EvaluationProtocolError("manual_review_policy.llm_assisted_boundary.llm_participates_in_primary_score must be false")
        if llm_boundary.get("reviewer_roles_receive_adjudicated_labels") is not False:
            raise EvaluationProtocolError("manual_review_policy.llm_assisted_boundary.reviewer_roles_receive_adjudicated_labels must be false")
    locked = protocol.get("locked_split_policy") or {}
    for key in ("locked_test_pairs_final_run_only", "manifest_records_locked_split_hash"):
        if locked.get(key) is not True:
            raise EvaluationProtocolError(f"locked_split_policy.{key} must be true")


def validate_protocol_pair_splits(cfg: Config, protocol: dict[str, Any], run_id: str = "latest") -> None:
    expected = set(warning_pair_ids(cfg, run_id))
    if not expected:
        return
    splits = protocol.get("splits") or {}
    actual = {
        str(pair_id)
        for key in ("dev_pairs", "validation_pairs", "locked_test_pairs")
        for pair_id in (splits.get(key) or [])
    }
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise EvaluationProtocolError(
            "evaluation_protocol split pair_ids do not match canonical warning pairs"
            f"; missing={missing[:5]} extra={extra[:5]}"
        )


def assert_oracle_blind_components(score_components: dict[str, Any], *, context: str = "primary score") -> None:
    leaked = sorted(FORBIDDEN_PRIMARY_SCORE_COMPONENTS & {str(key) for key in score_components})
    if leaked:
        raise EvaluationProtocolError(f"{context} uses forbidden oracle/manual score components: {', '.join(leaked)}")


def protocol_provenance(protocol: dict[str, Any]) -> dict[str, Any]:
    return {
        "protocol_version": protocol["protocol_version"],
        "claim_boundary": protocol["claim_boundary"],
        "primary_warning_set": protocol["primary_warning_set"],
        "evaluation_protocol": protocol.get("repo_relative_path") or protocol.get("path"),
        "evaluation_protocol_sha256": protocol.get("sha256"),
    }
