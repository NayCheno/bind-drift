from __future__ import annotations

from typing import Any

from binddrift.config import Config
from binddrift.dataset import extract_dataset
from binddrift.detectors.tier1 import run_tier1
from binddrift.detectors.tier2 import run_tier2
from binddrift.environment import capture_environment, write_environment
from binddrift.evaluation.evaluator import run_evaluation
from binddrift.extractors.bindgen import extract_bindings
from binddrift.extractors.c_api import extract_c_api
from binddrift.extractors.rust_usage import extract_rust_usage
from binddrift.graph.builder import build_graph
from binddrift.kernel import prepare_kernel_build
from binddrift.paper.cases import generate_case_studies
from binddrift.paper.tables import generate_paper_tables
from binddrift.ranking.scorer import rank_warnings


def run_pilot_replay(cfg: Config, commit_limit: int = 50, c_max_files: int = 50) -> dict[str, Any]:
    env = capture_environment(cfg)
    write_environment(cfg, env)
    results = {
        "env": {"linux_commit": env["linux_commit"], "bindgen_available": env["tools"]["bindgen"].get("available", False)},
        "commits": extract_dataset(cfg, limit=commit_limit),
        "kernel_prepare": prepare_kernel_build(cfg),
        "bindings": extract_bindings(cfg),
        "rust": extract_rust_usage(cfg),
        "c": extract_c_api(cfg, roots=["rust/helpers"], max_files=c_max_files),
        "graph": build_graph(cfg),
        "tier1": run_tier1(cfg),
    }
    results["tier2"] = run_tier2(cfg, append=True)
    results["ranking"] = rank_warnings(cfg)
    results["evaluation"] = run_evaluation(cfg)
    results["cases"] = generate_case_studies(cfg)
    results["tables"] = generate_paper_tables(cfg)
    return results
