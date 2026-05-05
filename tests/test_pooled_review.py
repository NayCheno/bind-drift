import csv
import json
from pathlib import Path

from binddrift.config import Config
from binddrift.evaluation.evaluate_rankers import evaluate_rankers
from binddrift.evaluation.pooled_review import generate_pooled_review_set
from binddrift.evaluation.protocol import write_default_evaluation_protocol
from binddrift.run_manifest import write_run_manifest
from binddrift.warnings import make_warning_uid


def _write_review_fixture(tmp_path: Path) -> Config:
    cfg = Config.from_args(repo_root=tmp_path)
    run_dir = tmp_path / "data/replay/latest"
    run_dir.mkdir(parents=True)
    warnings = []
    for idx, (symbol, drift_type, label) in enumerate(
        [
            ("foo_get", "SignatureDrift", "TRUE_WRAPPER_FIX"),
            ("bar_null", "FieldDrift", "FALSE_POSITIVE"),
            ("baz_ref", "MacroConstDrift", "BENIGN_DRIFT"),
        ],
        start=1,
    ):
        warning = {
            "warning_id": f"W-{idx}",
            "run_id": "latest",
            "pair_id": "latest-p001-v6.1-to-v6.2",
            "old_version": "v6.1",
            "new_version": "v6.2",
            "promotion_status": "promoted",
            "type": drift_type,
            "risk": "High",
            "score": float(10 - idx),
            "c_evidence_level": "c_source_diff",
            "promotion_reasons": ["direct_binding_use"],
            "c_side": {"symbol": symbol, "old": "a", "new": "b"},
            "rust_side": {"uses": [{"rust_file": "x.rs"}]},
        }
        warning["warning_uid"] = make_warning_uid(warning)
        warnings.append((warning, label))
    for name in ("warnings.jsonl", "promoted_warnings.jsonl"):
        (run_dir / name).write_text(
            "".join(json.dumps(warning, sort_keys=True) + "\n" for warning, _label in warnings),
            encoding="utf-8",
        )
    (run_dir / "drift_facts.jsonl").write_text('{"fact_id":"F-1"}\n', encoding="utf-8")
    (run_dir / "single_version_review_targets.jsonl").write_text("", encoding="utf-8")
    with (run_dir / "manual_review.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "warning_uid",
                "warning_id",
                "pair_id",
                "reviewer1_label",
                "reviewer1_notes",
                "reviewer2_label",
                "reviewer2_notes",
                "adjudicated_label",
                "adjudication_notes",
                "label",
            ],
        )
        writer.writeheader()
        for warning, label in warnings:
            writer.writerow(
                {
                    "warning_uid": warning["warning_uid"],
                    "warning_id": warning["warning_id"],
                    "pair_id": warning["pair_id"],
                    "reviewer1_label": label,
                    "reviewer1_notes": "r1",
                    "reviewer2_label": label,
                    "reviewer2_notes": "r2",
                    "adjudicated_label": label,
                    "adjudication_notes": "adj",
                    "label": "",
                }
            )
    write_default_evaluation_protocol(cfg)
    write_run_manifest(cfg)
    return cfg


def test_generate_pooled_review_set_merges_existing_labels(tmp_path: Path):
    cfg = _write_review_fixture(tmp_path)

    result = generate_pooled_review_set(cfg, rankers=["binddrift_oracle_blind", "no_ranking"])

    assert result["pool_rows"] == 3
    assert result["labels"]["coverage"] == 1.0
    labels = list(csv.DictReader(open(result["label_file"], newline="", encoding="utf-8")))
    assert {row["adjudicated_label"] for row in labels} == {"TRUE_WRAPPER_FIX", "FALSE_POSITIVE", "BENIGN_DRIFT"}
    pool_rows = [json.loads(line) for line in Path(result["pool"]).read_text(encoding="utf-8").splitlines()]
    assert all(row["pooled_review"] is True for row in pool_rows)


def test_generate_pooled_review_set_preserves_existing_non_manual_labels(tmp_path: Path):
    cfg = _write_review_fixture(tmp_path)
    first = generate_pooled_review_set(cfg, rankers=["binddrift_oracle_blind", "no_ranking"])
    label_file = Path(first["label_file"])
    rows = list(csv.DictReader(label_file.open(newline="", encoding="utf-8")))
    preserved_uid = rows[-1]["warning_uid"]
    manual_path = tmp_path / "data/replay/latest/manual_review.csv"
    manual_rows = [row for row in csv.DictReader(manual_path.open(newline="", encoding="utf-8")) if row["warning_uid"] != preserved_uid]
    with manual_path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=manual_rows[0], lineterminator="\n")
        writer.writeheader()
        writer.writerows(manual_rows)
    rows[-1]["reviewer1_label"] = "UNCLEAR"
    rows[-1]["reviewer1_notes"] = "r1 pending evidence"
    rows[-1]["reviewer2_label"] = "UNCLEAR"
    rows[-1]["reviewer2_notes"] = "r2 pending evidence"
    rows[-1]["adjudicated_label"] = "UNCLEAR"
    rows[-1]["adjudication_notes"] = "adjudicated from pooled review artifacts"
    rows[-1]["label_source"] = "existing_binddrift_review_artifacts"
    with label_file.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=rows[0], lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    write_run_manifest(cfg)

    second = generate_pooled_review_set(cfg, rankers=["binddrift_oracle_blind", "no_ranking"])

    merged = {row["warning_uid"]: row for row in csv.DictReader(open(second["label_file"], newline="", encoding="utf-8"))}
    assert merged[preserved_uid]["adjudicated_label"] == "UNCLEAR"
    assert merged[preserved_uid]["label_source"] == "existing_binddrift_review_artifacts"


def test_evaluate_rankers_uses_same_pooled_labels(tmp_path: Path):
    cfg = _write_review_fixture(tmp_path)
    pooled = generate_pooled_review_set(cfg, rankers=["binddrift_oracle_blind", "no_ranking"])

    table = evaluate_rankers(
        cfg,
        pool=Path(pooled["pool"]),
        labels=Path(pooled["label_file"]),
        output=tmp_path / "paper/tables/ranking_pooled_evaluation.json",
        rankers=["binddrift_oracle_blind", "no_ranking"],
    )

    assert table["label_coverage"]["coverage"] == 1.0
    assert table["coverage_acceptance"]["passes"] is True
    assert {row["ranker"] for row in table["rankers"]} == {"binddrift_oracle_blind", "no_ranking"}
    assert table["rankers"][0]["p_at_10"] == 0.3333
    assert {row["evaluated_pool_rows"] for row in table["rankers"]} == {3}
    assert len({json.dumps(row["label_distribution"], sort_keys=True) for row in table["rankers"]}) == 1
    assert table["comparison_against_best_simple_baseline"]["paired_bootstrap_significance"]["method"] == "paired_rank_position_bootstrap"
    for row in table["rankers"]:
        for metric in ("p_at_20", "p_at_50", "ndcg_at_20"):
            lo, hi = row["bootstrap_ci"][metric]
            observed = row[metric]
            assert lo <= observed <= hi


def test_evaluate_rankers_counts_uncovered_pool_rows_as_misses(tmp_path: Path):
    cfg = _write_review_fixture(tmp_path)
    pooled = generate_pooled_review_set(cfg, rankers=["binddrift_oracle_blind", "c_indicator"])

    table = evaluate_rankers(
        cfg,
        pool=Path(pooled["pool"]),
        labels=Path(pooled["label_file"]),
        output=tmp_path / "paper/tables/ranking_pooled_evaluation.json",
        rankers=["binddrift_oracle_blind", "c_indicator"],
    )

    by_ranker = {row["ranker"]: row for row in table["rankers"]}
    assert by_ranker["c_indicator"]["candidate_count"] == 0
    assert by_ranker["c_indicator"]["review_pool_ranked_count"] == 0
    assert by_ranker["c_indicator"]["p_at_10"] == 0.0
    assert by_ranker["c_indicator"]["auprc_on_pooled_review_set"] == 0.0
    assert by_ranker["c_indicator"]["label_distribution"] == by_ranker["binddrift_oracle_blind"]["label_distribution"]
