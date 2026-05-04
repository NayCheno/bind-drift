from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.kernel import default_version_id


BINDING_RE = re.compile(r"(?:crate::|\$crate::)?bindings::(?P<name>[A-Za-z_][A-Za-z0-9_]*)")
PUB_FN_RE = re.compile(
    r"(?P<vis>pub(?:\([^)]*\))?)?\s*(?:unsafe\s+)?fn\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*\((?P<params>[^)]*)\)\s*(?:->\s*(?P<ret>[^{;]+))?"
)
IMPL_RE = re.compile(r"impl(?:<[^>]+>)?\s+(?:(?P<trait>Drop|Clone)\s+for\s+)?(?P<ty>[A-Za-z_][A-Za-z0-9_:<>]*)")
STRUCT_RE = re.compile(r"pub\s+struct\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)")
ERROR_MAPPING_PATTERNS = {
    "RESULT_RETURN": "Result<",
    "OPTION_RETURN": "Option<",
    "ERR_PTR_MAPPING": "from_err_ptr",
    "TO_RESULT_MAPPING": "to_result",
    "NONNULL_MAPPING": "NonNull::new",
    "IS_ERR_MAPPING": "IS_ERR",
    "PTR_ERR_MAPPING": "PTR_ERR",
}
LIFETIME_PATTERNS = {
    "FROM_RAW": "from_raw",
    "INTO_RAW": "into_raw",
    "AS_PTR": "as_ptr",
    "OPAQUE": "Opaque<",
    "AREF": "ARef<",
    "FOREIGN_OWNABLE": "ForeignOwnable",
    "MANUALLY_DROP": "ManuallyDrop",
}


def _brace_delta(line: str) -> int:
    return line.count("{") - line.count("}")


def _nearest_api(apis: list[dict[str, Any]], line_no: int) -> str | None:
    before = [api for api in apis if api["line"] <= line_no]
    if not before:
        return None
    return before[-1]["api_name"]


def _nearest_binding(uses: list[dict[str, Any]], line_no: int) -> str | None:
    near = [use for use in uses if abs(use["line"] - line_no) <= 5]
    return near[-1]["binding_symbol"] if near else None


def _parse_file(
    path: Path, version_id: str
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    rel = str(path)
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    uses: list[dict[str, Any]] = []
    apis: list[dict[str, Any]] = []
    comments: list[dict[str, Any]] = []
    lifetime_facts: list[dict[str, Any]] = []
    error_mappings: list[dict[str, Any]] = []
    unsafe_depth = 0
    impl_stack: list[tuple[str, int]] = []
    current_fn: tuple[str, int] | None = None
    current_type: str | None = None

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        if match := STRUCT_RE.search(stripped):
            current_type = match.group("name")
        if match := IMPL_RE.match(stripped):
            ty = match.group("ty")
            if match.group("trait"):
                ty = f"{match.group('trait')} for {ty}"
                lifetime_facts.append(
                    {
                        "version_id": version_id,
                        "rust_file": rel,
                        "line": idx,
                        "fact_type": f"IMPL_{match.group('trait').upper()}",
                        "rust_type": match.group("ty"),
                        "uses_bindings": "[]",
                        "evidence_text": stripped[:500],
                    }
                )
            impl_stack.append((ty, max(1, _brace_delta(stripped))))
            current_type = ty
        line_starts_unsafe = bool(re.search(r"\bunsafe\s*\{", stripped))

        for match in BINDING_RE.finditer(line):
            uses.append(
                {
                    "version_id": version_id,
                    "rust_file": rel,
                    "line": idx,
                    "binding_symbol": match.group("name"),
                    "enclosing_unsafe_block": int(unsafe_depth > 0 or line_starts_unsafe),
                    "enclosing_function": current_fn[0] if current_fn else None,
                    "enclosing_impl": impl_stack[-1][0] if impl_stack else None,
                    "enclosing_type": current_type,
                }
            )

        for mapping_type, needle in ERROR_MAPPING_PATTERNS.items():
            if needle in stripped:
                error_mappings.append(
                    {
                        "version_id": version_id,
                        "rust_file": rel,
                        "line": idx,
                        "mapping_type": mapping_type,
                        "text": stripped[:500],
                        "nearby_binding_symbol": None,
                        "nearby_api": None,
                    }
                )
        for fact_type, needle in LIFETIME_PATTERNS.items():
            if needle in stripped:
                lifetime_facts.append(
                    {
                        "version_id": version_id,
                        "rust_file": rel,
                        "line": idx,
                        "fact_type": fact_type,
                        "rust_type": current_type,
                        "uses_bindings": "[]",
                        "evidence_text": stripped[:500],
                    }
                )

        if "SAFETY:" in stripped or stripped.startswith("///") or stripped.startswith("//!"):
            comments.append(
                {
                    "version_id": version_id,
                    "rust_file": rel,
                    "line": idx,
                    "text": stripped,
                    "nearby_binding_symbol": None,
                    "nearby_api": None,
                }
            )

        if match := PUB_FN_RE.search(stripped):
            if match.group("vis"):
                name = match.group("name")
                api_name = f"{impl_stack[-1][0]}::{name}" if impl_stack else name
                current_fn = (api_name, max(1, _brace_delta(stripped)))
                apis.append(
                    {
                        "version_id": version_id,
                        "rust_file": rel,
                        "api_name": api_name,
                        "receiver_type": impl_stack[-1][0] if impl_stack else None,
                        "visibility": match.group("vis"),
                        "return_type": (match.group("ret") or "()").strip(),
                        "params": json.dumps(match.group("params").strip()),
                        "uses_bindings": "[]",
                        "line": idx,
                    }
                )
            else:
                current_fn = (match.group("name"), max(1, _brace_delta(stripped)))

        delta = _brace_delta(stripped)
        if current_fn:
            current_fn = (current_fn[0], current_fn[1] + delta)
            if current_fn[1] <= 0:
                current_fn = None
        if impl_stack:
            ty, depth = impl_stack[-1]
            depth += delta
            if depth <= 0:
                impl_stack.pop()
            else:
                impl_stack[-1] = (ty, depth)
        if line_starts_unsafe:
            unsafe_depth = max(0, unsafe_depth + delta)
        elif unsafe_depth:
            unsafe_depth = max(0, unsafe_depth + delta)

    uses_by_api: dict[str, set[str]] = {}
    for use in uses:
        api = use["enclosing_function"]
        if api:
            uses_by_api.setdefault(api, set()).add(use["binding_symbol"])
    for api in apis:
        api["uses_bindings"] = json.dumps(sorted(uses_by_api.get(api["api_name"], set())))
    for comment in comments:
        comment["nearby_binding_symbol"] = _nearest_binding(uses, comment["line"])
        comment["nearby_api"] = _nearest_api(apis, comment["line"])
    for mapping in error_mappings:
        mapping["nearby_binding_symbol"] = _nearest_binding(uses, mapping["line"])
        mapping["nearby_api"] = _nearest_api(apis, mapping["line"])
    uses_by_line: dict[int, set[str]] = {}
    for use in uses:
        uses_by_line.setdefault(use["line"], set()).add(use["binding_symbol"])
    for fact in lifetime_facts:
        nearby = set()
        for line_no in range(fact["line"] - 3, fact["line"] + 4):
            nearby.update(uses_by_line.get(line_no, set()))
        fact["uses_bindings"] = json.dumps(sorted(nearby))
    return uses, apis, comments, lifetime_facts, error_mappings


def extract_rust_usage(cfg: Config, version_id: str | None = None) -> dict[str, Any]:
    cfg.ensure_dirs()
    vid = version_id or default_version_id(cfg)
    root = cfg.linux_tree / "rust/kernel"
    all_uses: list[dict[str, Any]] = []
    all_apis: list[dict[str, Any]] = []
    all_comments: list[dict[str, Any]] = []
    all_lifetime_facts: list[dict[str, Any]] = []
    all_error_mappings: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*.rs")):
        uses, apis, comments, lifetime_facts, error_mappings = _parse_file(path, vid)
        all_uses.extend(uses)
        all_apis.extend(apis)
        all_comments.extend(comments)
        all_lifetime_facts.extend(lifetime_facts)
        all_error_mappings.extend(error_mappings)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(conn, "rust_binding_uses", all_uses)
    upsert_many(conn, "rust_safe_apis", all_apis)
    upsert_many(conn, "rust_safety_comments", all_comments)
    upsert_many(conn, "rust_lifetime_facts", all_lifetime_facts)
    upsert_many(conn, "rust_error_mappings", all_error_mappings)
    return {
        "database": str(cfg.database),
        "version_id": vid,
        "rust_files": len(list(root.rglob("*.rs"))) if root.exists() else 0,
        "binding_uses": len(all_uses),
        "safe_apis": len(all_apis),
        "safety_comments": len(all_comments),
        "lifetime_facts": len(all_lifetime_facts),
        "error_mappings": len(all_error_mappings),
    }
