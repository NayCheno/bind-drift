from __future__ import annotations

import json
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize
from binddrift.warnings import read_warnings
from .metrics import labeled_summary, load_manual_labels


BASELINES = ["BindgenOnly", "CSignatureDiff", "BuildOnly", "GrepUsage", "NoRanking", "Tier1Only"]
ABLATIONS = ["NoGraph", "NoTier2", "NoRanking", "NoSafetyComment", "NoCommitText"]


def generate_baselines(cfg: Config) -> dict[str, Any]:
    conn = connect(cfg.database)
    initialize(conn)
    warnings = read_warnings(cfg.warnings_jsonl)
    labels = load_manual_labels(cfg.data_dir / "manual_review.csv")
    metrics = labeled_summary(warnings, labels)
    counts = {
        "binding_functions": conn.execute("SELECT COUNT(*) AS n FROM binding_functions").fetchone()["n"],
        "c_functions": conn.execute("SELECT COUNT(*) AS n FROM c_functions").fetchone()["n"],
        "rust_binding_uses": conn.execute("SELECT COUNT(*) AS n FROM rust_binding_uses").fetchone()["n"],
        "graph_edges": conn.execute("SELECT COUNT(*) AS n FROM graph_edges").fetchone()["n"],
        "warnings": len(warnings),
    }
    rows = []
    for name in BASELINES:
        rows.append(
            {
                "variant": name,
                "kind": "baseline",
                "candidate_count": _candidate_count(name, counts),
                "precision_at_k": metrics["precision_at_k"],
                "recall": None,
                "note": "Precision values are populated only when manual labels are present.",
            }
        )
    for name in ABLATIONS:
        rows.append(
            {
                "variant": name,
                "kind": "ablation",
                "candidate_count": _candidate_count(name, counts),
                "precision_at_k": metrics["precision_at_k"],
                "recall": None,
                "note": "Precision values are populated only when manual labels are present.",
            }
        )
    path = cfg.repo_root / "paper/tables/baselines_ablations.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps({"counts": counts, "variants": rows}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"baseline_table": str(path), "variants": len(rows), "counts": counts}


def _candidate_count(name: str, counts: dict[str, int]) -> int:
    if name == "BindgenOnly":
        return counts["binding_functions"]
    if name == "CSignatureDiff":
        return counts["c_functions"]
    if name == "BuildOnly":
        return 0
    if name == "GrepUsage":
        return counts["rust_binding_uses"]
    if name == "Tier1Only":
        return counts["warnings"]
    if name == "NoGraph":
        return counts["c_functions"]
    return counts["warnings"]
