from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path
from typing import Any

from binddrift.artifact_paths import repo_relative, sanitize_local_paths
from binddrift.config import Config


ALLOWED_REVIEW_LABELS = {
    "TRUE_BUILD_BREAKAGE",
    "TRUE_WRAPPER_FIX",
    "TRUE_SEMANTIC_DRIFT",
    "BENIGN_DRIFT",
    "FALSE_POSITIVE",
    "UNCLEAR",
}

MERGE_FIELDS = [
    "reviewer1_label",
    "reviewer1_notes",
    "reviewer2_label",
    "reviewer2_notes",
    "adjudicated_label",
    "adjudication_notes",
]


def merge_pooled_review_roles(
    labels_csv: Path,
    *,
    reviewer1_jsonl: Path,
    reviewer2_jsonl: Path,
    adjudicator_jsonl: Path,
    output: Path | None = None,
    report: Path | None = None,
    cfg: Config | None = None,
    label_source: str = "binddrift_review_m3",
    overwrite_complete: bool = False,
) -> dict[str, Any]:
    """Backfill pooled review labels from independent reviewer/adjudicator JSONL.

    The merge deliberately updates only the reviewer/adjudicator fields plus
    `label_source`; warning identity, risk, score, type, and symbol columns are
    preserved from the locked pooled label CSV.
    """

    labels_csv = labels_csv.resolve()
    output = (output or labels_csv).resolve()
    report = (report or labels_csv.parent / "review_artifacts" / "pooled_review_role_merge_report.json").resolve()
    fieldnames, rows = _read_csv(labels_csv)
    for field in [*MERGE_FIELDS, "label_source"]:
        if field not in fieldnames:
            fieldnames.append(field)
            for row in rows:
                row[field] = ""

    reviewer1 = _load_jsonl_by_key(reviewer1_jsonl, role="reviewer1")
    reviewer2 = _load_jsonl_by_key(reviewer2_jsonl, role="reviewer2")
    adjudicator = _load_jsonl_by_key(adjudicator_jsonl, role="adjudicator")

    updated_rows = 0
    missing = {
        "reviewer1": [],
        "reviewer2": [],
        "adjudicator": [],
    }
    validation_errors: list[str] = []
    for row in rows:
        if _row_complete(row) and not overwrite_complete:
            continue
        key = _row_key(row)
        r1 = _lookup(reviewer1, row)
        r2 = _lookup(reviewer2, row)
        adj = _lookup(adjudicator, row)
        if r1 is None:
            missing["reviewer1"].append(key)
        if r2 is None:
            missing["reviewer2"].append(key)
        if adj is None:
            missing["adjudicator"].append(key)
        if not (r1 and r2 and adj):
            continue
        before = {field: row.get(field, "") for field in MERGE_FIELDS}
        _copy_if_present(row, r1, "reviewer1_label", "reviewer1_notes")
        _copy_if_present(row, r2, "reviewer2_label", "reviewer2_notes")
        _copy_if_present(row, adj, "adjudicated_label", "adjudication_notes")
        row["label_source"] = label_source
        _clear_legacy_fields(row)
        after = {field: row.get(field, "") for field in MERGE_FIELDS}
        if after != before:
            updated_rows += 1
        validation_errors.extend(_validate_row(row, key))

    _write_csv(output, fieldnames, rows)
    manifest_update = _refresh_pooled_manifest(labels_csv, output, rows, cfg=cfg)
    summary = _summary(
        rows,
        labels_csv=labels_csv,
        output=output,
        reviewer1_jsonl=reviewer1_jsonl,
        reviewer2_jsonl=reviewer2_jsonl,
        adjudicator_jsonl=adjudicator_jsonl,
        updated_rows=updated_rows,
        missing=missing,
        validation_errors=validation_errors,
        overwrite_complete=overwrite_complete,
        manifest_update=manifest_update,
        cfg=cfg,
    )
    report.parent.mkdir(parents=True, exist_ok=True)
    payload = sanitize_local_paths(summary, cfg) if cfg else summary
    report.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return payload


def _read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def _write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def _load_jsonl_by_key(path: Path, *, role: str) -> dict[str, dict[str, Any]]:
    rows: dict[str, dict[str, Any]] = {}
    with path.open(encoding="utf-8") as fh:
        for line_number, line in enumerate(fh, start=1):
            if not line.strip():
                continue
            row = json.loads(line)
            row["_source_line"] = line_number
            row["_role"] = role
            for key in _candidate_keys(row):
                rows.setdefault(key, row)
    return rows


def _candidate_keys(row: dict[str, Any]) -> list[str]:
    keys = []
    uid = str(row.get("warning_uid") or "").strip()
    warning_id = str(row.get("warning_id") or "").strip()
    pair_id = str((row.get("pair_id") or (row.get("versions") or {}).get("pair_id") or "")).strip()
    if uid:
        keys.append(uid)
    if pair_id and warning_id:
        keys.append(f"{pair_id}:{warning_id}")
    if warning_id:
        keys.append(warning_id)
    return keys


def _row_key(row: dict[str, str]) -> str:
    if row.get("warning_uid"):
        return row["warning_uid"]
    if row.get("pair_id") and row.get("warning_id"):
        return f"{row['pair_id']}:{row['warning_id']}"
    return row.get("warning_id", "")


def _lookup(rows: dict[str, dict[str, Any]], label_row: dict[str, str]) -> dict[str, Any] | None:
    for key in _candidate_keys(label_row):
        if key in rows:
            return rows[key]
    return None


def _row_complete(row: dict[str, str]) -> bool:
    return all((row.get(field) or "").strip() for field in MERGE_FIELDS)


def _copy_if_present(target: dict[str, str], source: dict[str, Any], label_field: str, notes_field: str) -> None:
    label = str(source.get(label_field) or source.get("label") or "").strip()
    notes = str(source.get(notes_field) or source.get("notes") or source.get("adjudication_notes") or "").strip()
    if label:
        target[label_field] = label
    if notes:
        target[notes_field] = notes


def _clear_legacy_fields(row: dict[str, str]) -> None:
    for field in ("label", "reviewer_notes"):
        if field in row:
            row[field] = ""


def _validate_row(row: dict[str, str], key: str) -> list[str]:
    errors: list[str] = []
    for field in ("reviewer1_label", "reviewer2_label", "adjudicated_label"):
        label = (row.get(field) or "").strip()
        if label and label not in ALLOWED_REVIEW_LABELS:
            errors.append(f"{key}: invalid {field}={label}")
    if (row.get("adjudicated_label") or "").strip() and not (row.get("adjudication_notes") or "").strip():
        errors.append(f"{key}: adjudicated label missing adjudication_notes")
    return errors


def _summary(
    rows: list[dict[str, str]],
    *,
    labels_csv: Path,
    output: Path,
    reviewer1_jsonl: Path,
    reviewer2_jsonl: Path,
    adjudicator_jsonl: Path,
    updated_rows: int,
    missing: dict[str, list[str]],
    validation_errors: list[str],
    overwrite_complete: bool,
    manifest_update: dict[str, Any] | None,
    cfg: Config | None,
) -> dict[str, Any]:
    complete = [row for row in rows if _row_complete(row)]
    double = [row for row in rows if row.get("reviewer1_label") and row.get("reviewer2_label")]
    adjudicated = [row for row in rows if row.get("adjudicated_label")]
    disagreements = [row for row in double if row.get("reviewer1_label") != row.get("reviewer2_label")]
    agreement_rate = round((len(double) - len(disagreements)) / len(double), 4) if double else None
    kappa = _cohen_kappa([(row.get("reviewer1_label", ""), row.get("reviewer2_label", "")) for row in double])
    return {
        "labels_csv": _path(cfg, labels_csv),
        "output": _path(cfg, output),
        "reviewer1_jsonl": _path(cfg, reviewer1_jsonl),
        "reviewer2_jsonl": _path(cfg, reviewer2_jsonl),
        "adjudicator_jsonl": _path(cfg, adjudicator_jsonl),
        "total_rows": len(rows),
        "updated_rows": updated_rows,
        "overwrite_complete": overwrite_complete,
        "complete_rows": len(complete),
        "double_labeled_rows": len(double),
        "adjudicated_rows": len(adjudicated),
        "agreement_rate": agreement_rate,
        "cohen_kappa": kappa,
        "disagreements": len(disagreements),
        "unclear_rows": sum(1 for row in rows if row.get("adjudicated_label") == "UNCLEAR"),
        "label_distribution": {
            "reviewer1_label": dict(Counter(row.get("reviewer1_label", "") for row in rows if row.get("reviewer1_label"))),
            "reviewer2_label": dict(Counter(row.get("reviewer2_label", "") for row in rows if row.get("reviewer2_label"))),
            "adjudicated_label": dict(Counter(row.get("adjudicated_label", "") for row in rows if row.get("adjudicated_label"))),
        },
        "pooled_review_manifest_update": manifest_update,
        "missing_matches": {role: {"count": len(keys), "warning_keys": sorted(keys)[:20]} for role, keys in missing.items()},
        "validation_errors": validation_errors[:50],
        "validation_error_count": len(validation_errors),
    }


def _refresh_pooled_manifest(labels_csv: Path, output: Path, rows: list[dict[str, str]], *, cfg: Config | None) -> dict[str, Any] | None:
    manifest_path = output.parent / "pooled_review_manifest.json"
    if output.name != "pooled_review_labels.csv" or not manifest_path.exists():
        return None
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    labeled = sum(1 for row in rows if (row.get("adjudicated_label") or "").strip())
    manifest["labels"] = {
        "label_rows": len(rows),
        "labeled_rows": labeled,
        "coverage": round(labeled / len(rows), 4) if rows else 0.0,
    }
    manifest["label_file"] = _path(cfg, output)
    manifest_path.write_text(json.dumps(sanitize_local_paths(manifest, cfg), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {
        "path": _path(cfg, manifest_path),
        "label_rows": len(rows),
        "labeled_rows": labeled,
        "coverage": manifest["labels"]["coverage"],
        "source_labels_csv": _path(cfg, labels_csv),
    }


def _path(cfg: Config | None, path: Path) -> str:
    return repo_relative(cfg, path) if cfg else str(path)


def _cohen_kappa(pairs: list[tuple[str, str]]) -> float | None:
    if not pairs:
        return None
    first = Counter(left for left, _right in pairs)
    second = Counter(right for _left, right in pairs)
    total = len(pairs)
    observed = sum(1 for left, right in pairs if left == right) / total
    expected = sum(first[label] * second[label] for label in set(first) | set(second)) / (total * total)
    if expected == 1.0:
        return 1.0 if observed == 1.0 else 0.0
    return round((observed - expected) / (1.0 - expected), 4)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Merge BindDrift pooled review role JSONL artifacts into labels CSV.")
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--labels", required=True)
    parser.add_argument("--reviewer1", required=True)
    parser.add_argument("--reviewer2", required=True)
    parser.add_argument("--adjudicator", required=True)
    parser.add_argument("--output")
    parser.add_argument("--report")
    parser.add_argument("--label-source", default="binddrift_review_m3")
    parser.add_argument("--overwrite-complete", action="store_true", help="Replace existing complete reviewer/adjudicator fields.")
    args = parser.parse_args(argv)
    cfg = Config.from_args(repo_root=args.repo_root)
    result = merge_pooled_review_roles(
        Path(args.labels),
        reviewer1_jsonl=Path(args.reviewer1),
        reviewer2_jsonl=Path(args.reviewer2),
        adjudicator_jsonl=Path(args.adjudicator),
        output=Path(args.output) if args.output else None,
        report=Path(args.report) if args.report else None,
        cfg=cfg,
        label_source=args.label_source,
        overwrite_complete=args.overwrite_complete,
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
