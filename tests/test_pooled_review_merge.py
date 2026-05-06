import csv
import json
from pathlib import Path

from binddrift.evaluation.pooled_review_merge import merge_pooled_review_roles


def _write_jsonl(path: Path, rows: list[dict]) -> None:
    path.write_text("".join(json.dumps(row, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


def test_merge_pooled_review_roles_backfills_only_review_fields(tmp_path: Path) -> None:
    labels = tmp_path / "pooled_review_labels.csv"
    with labels.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "warning_uid",
                "warning_id",
                "pair_id",
                "ranker_source",
                "type",
                "symbol",
                "risk",
                "score",
                "reviewer1_label",
                "reviewer1_notes",
                "reviewer2_label",
                "reviewer2_notes",
                "adjudicated_label",
                "adjudication_notes",
                "label",
                "reviewer_notes",
            ],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerow(
            {
                "warning_uid": "u1",
                "warning_id": "W-1",
                "pair_id": "p1",
                "ranker_source": "no_ranking",
                "type": "SignatureDrift",
                "symbol": "foo",
                "risk": "Low",
                "score": "1.0",
                "label": "stale",
                "reviewer_notes": "stale",
            }
        )

    reviewer1 = tmp_path / "r1.jsonl"
    reviewer2 = tmp_path / "r2.jsonl"
    adjudicator = tmp_path / "adj.jsonl"
    _write_jsonl(reviewer1, [{"warning_uid": "u1", "warning_id": "W-1", "pair_id": "p1", "reviewer1_label": "FALSE_POSITIVE", "reviewer1_notes": "binding only"}])
    _write_jsonl(reviewer2, [{"warning_uid": "u1", "warning_id": "W-1", "pair_id": "p1", "reviewer2_label": "FALSE_POSITIVE", "reviewer2_notes": "no rust impact"}])
    _write_jsonl(adjudicator, [{"warning_uid": "u1", "warning_id": "W-1", "pair_id": "p1", "adjudicated_label": "FALSE_POSITIVE", "adjudication_notes": "unsupported generated binding evidence"}])

    report = merge_pooled_review_roles(
        labels,
        reviewer1_jsonl=reviewer1,
        reviewer2_jsonl=reviewer2,
        adjudicator_jsonl=adjudicator,
        label_source="unit_test_review",
    )

    rows = list(csv.DictReader(labels.open(newline="", encoding="utf-8")))
    assert rows[0]["warning_id"] == "W-1"
    assert rows[0]["type"] == "SignatureDrift"
    assert rows[0]["symbol"] == "foo"
    assert rows[0]["reviewer1_label"] == "FALSE_POSITIVE"
    assert rows[0]["reviewer2_label"] == "FALSE_POSITIVE"
    assert rows[0]["adjudicated_label"] == "FALSE_POSITIVE"
    assert rows[0]["label"] == ""
    assert rows[0]["reviewer_notes"] == ""
    assert rows[0]["label_source"] == "unit_test_review"
    assert report["updated_rows"] == 1
    assert report["complete_rows"] == 1
    assert report["validation_error_count"] == 0


def test_merge_pooled_review_roles_reports_missing_matches(tmp_path: Path) -> None:
    labels = tmp_path / "pooled_review_labels.csv"
    labels.write_text(
        "warning_uid,warning_id,pair_id,reviewer1_label,reviewer1_notes,reviewer2_label,reviewer2_notes,adjudicated_label,adjudication_notes\n"
        "u1,W-1,p1,,,,,,\n",
        encoding="utf-8",
    )
    empty = tmp_path / "empty.jsonl"
    empty.write_text("", encoding="utf-8")

    report = merge_pooled_review_roles(
        labels,
        reviewer1_jsonl=empty,
        reviewer2_jsonl=empty,
        adjudicator_jsonl=empty,
    )

    assert report["updated_rows"] == 0
    assert report["complete_rows"] == 0
    assert report["missing_matches"]["reviewer1"]["count"] == 1
    assert report["missing_matches"]["reviewer2"]["count"] == 1
    assert report["missing_matches"]["adjudicator"]["count"] == 1


def test_merge_pooled_review_roles_can_overwrite_complete_rows(tmp_path: Path) -> None:
    labels = tmp_path / "pooled_review_labels.csv"
    labels.write_text(
        "warning_uid,warning_id,pair_id,reviewer1_label,reviewer1_notes,reviewer2_label,reviewer2_notes,adjudicated_label,adjudication_notes,label_source\n"
        "u1,W-1,p1,UNCLEAR,old r1,UNCLEAR,old r2,UNCLEAR,old adj,old_source\n",
        encoding="utf-8",
    )
    reviewer1 = tmp_path / "r1.jsonl"
    reviewer2 = tmp_path / "r2.jsonl"
    adjudicator = tmp_path / "adj.jsonl"
    _write_jsonl(reviewer1, [{"warning_uid": "u1", "warning_id": "W-1", "pair_id": "p1", "reviewer1_label": "FALSE_POSITIVE", "reviewer1_notes": "r1"}])
    _write_jsonl(reviewer2, [{"warning_uid": "u1", "warning_id": "W-1", "pair_id": "p1", "reviewer2_label": "FALSE_POSITIVE", "reviewer2_notes": "r2"}])
    _write_jsonl(adjudicator, [{"warning_uid": "u1", "warning_id": "W-1", "pair_id": "p1", "adjudicated_label": "FALSE_POSITIVE", "adjudication_notes": "adj"}])

    report = merge_pooled_review_roles(
        labels,
        reviewer1_jsonl=reviewer1,
        reviewer2_jsonl=reviewer2,
        adjudicator_jsonl=adjudicator,
        label_source="new_source",
        overwrite_complete=True,
    )

    row = next(csv.DictReader(labels.open(newline="", encoding="utf-8")))
    assert row["adjudicated_label"] == "FALSE_POSITIVE"
    assert row["label_source"] == "new_source"
    assert report["updated_rows"] == 1
    assert report["overwrite_complete"] is True
