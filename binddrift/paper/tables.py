from __future__ import annotations

import json
from pathlib import Path

from binddrift.config import Config


def generate_paper_tables(cfg: Config) -> dict[str, object]:
    tables_dir = cfg.repo_root / "paper/tables"
    tables_dir.mkdir(parents=True, exist_ok=True)
    known = {
        "evaluation_summary": tables_dir / "evaluation_summary.json",
        "baselines_ablations": tables_dir / "baselines_ablations.json",
    }
    index = {
        name: {"path": str(path), "available": path.exists()}
        for name, path in known.items()
    }
    out = tables_dir / "table_index.json"
    out.write_text(json.dumps(index, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return {"table_index": str(out), "tables": index}
