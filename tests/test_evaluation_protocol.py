import json
from pathlib import Path

import pytest

from binddrift.config import Config
from binddrift.evaluation.protocol import (
    EvaluationProtocolError,
    assert_oracle_blind_components,
    load_evaluation_protocol,
    write_default_evaluation_protocol,
)


def test_default_evaluation_protocol_locks_claim_boundary(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    path = write_default_evaluation_protocol(cfg)

    protocol = load_evaluation_protocol(cfg)

    assert path.exists()
    assert protocol["protocol_version"] == "ccfb-strict-v1"
    assert protocol["claim_boundary"] == "evidence-backed warning prioritization"
    assert protocol["primary_warning_set"] == "oracle_blind_ranked_warnings"
    assert protocol["oracle_usage"]["not_allowed_in_primary_score"] is True
    assert protocol["manual_review_policy"]["unclear_is_not_true_positive"] is True


def test_default_evaluation_protocol_uses_canonical_pair_ids(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    run_dir = tmp_path / "data/replay/latest"
    run_dir.mkdir(parents=True)
    (run_dir / "promoted_warnings.jsonl").write_text(
        '{"pair_id":"latest-p002-v6.2-to-v6.3"}\n'
        '{"pair_id":"latest-p001-v6.1-to-v6.2"}\n',
        encoding="utf-8",
    )

    write_default_evaluation_protocol(cfg)
    protocol = load_evaluation_protocol(cfg)
    split_ids = protocol["splits"]["dev_pairs"] + protocol["splits"]["validation_pairs"] + protocol["splits"]["locked_test_pairs"]

    assert split_ids == ["latest-p001-v6.1-to-v6.2", "latest-p002-v6.2-to-v6.3"]


def test_evaluation_protocol_rejects_oracle_enabled_primary_score(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    path = write_default_evaluation_protocol(cfg)
    data = json.loads(path.read_text(encoding="utf-8"))
    data["oracle_usage"]["not_allowed_in_primary_score"] = False
    path.write_text(json.dumps(data), encoding="utf-8")

    with pytest.raises(EvaluationProtocolError, match="not_allowed_in_primary_score"):
        load_evaluation_protocol(cfg)


def test_evaluation_protocol_rejects_stale_split_ids(tmp_path: Path):
    cfg = Config.from_args(repo_root=tmp_path)
    run_dir = tmp_path / "data/replay/latest"
    run_dir.mkdir(parents=True)
    (run_dir / "promoted_warnings.jsonl").write_text(
        '{"pair_id":"latest-p999-vX-to-vY"}\n',
        encoding="utf-8",
    )
    path = write_default_evaluation_protocol(cfg)
    data = json.loads(path.read_text(encoding="utf-8"))
    data["splits"] = {"dev_pairs": ["latest-p001"], "validation_pairs": [], "locked_test_pairs": []}
    path.write_text(json.dumps(data), encoding="utf-8")

    with pytest.raises(EvaluationProtocolError, match="split pair_ids"):
        load_evaluation_protocol(cfg)


def test_oracle_blind_component_guard_rejects_forbidden_features():
    with pytest.raises(EvaluationProtocolError, match="wrapper_fix_hit"):
        assert_oracle_blind_components({"rust_direct_use": 2.0, "wrapper_fix_hit": 4.0})
