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
IMPL_RE = re.compile(r"impl\b")
STRUCT_RE = re.compile(r"pub\s+struct\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)")
ERROR_MAPPING_PATTERNS = {
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


def _is_comment_line(stripped: str) -> bool:
    return stripped.startswith(("///", "//!","//", "/*", "*"))


def _is_import_line(stripped: str) -> bool:
    return stripped.startswith("use ") or stripped.startswith("pub use ")


def _return_mapping_type(ret: str | None) -> str | None:
    if not ret:
        return None
    if "Result" in ret:
        return "RESULT_RETURN"
    if "Option" in ret:
        return "OPTION_RETURN"
    return None


def _matching_angle_end(value: str, start: int) -> int | None:
    depth = 0
    for idx in range(start, len(value)):
        char = value[idx]
        if char == "<":
            depth += 1
        elif char == ">":
            depth -= 1
            if depth == 0:
                return idx
    return None


def _parse_impl_type(stripped: str) -> tuple[str, str | None] | None:
    if not stripped.startswith("impl"):
        return None
    rest = stripped[len("impl") :].strip()
    if rest.startswith("<"):
        end = _matching_angle_end(rest, 0)
        if end is None:
            return None
        rest = rest[end + 1 :].strip()
    rest = rest.split("{", 1)[0].strip()
    rest = rest.split(" where ", 1)[0].strip()
    if not rest:
        return None
    trait = None
    ty = rest
    if " for " in rest:
        trait, ty = rest.rsplit(" for ", 1)
        trait = trait.strip()
        ty = ty.strip()
    return ty, trait


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
    struct_stack: list[tuple[str, int]] = []
    pending_impls: list[tuple[str, str | None]] = []
    pending_structs: list[str] = []
    current_fn: tuple[str, int] | None = None

    for idx, line in enumerate(lines, start=1):
        stripped = line.strip()
        code_line = bool(stripped) and not _is_comment_line(stripped) and not _is_import_line(stripped)
        delta = _brace_delta(stripped)
        if match := STRUCT_RE.search(stripped):
            pending_structs.append(match.group("name"))
        if parsed_impl := _parse_impl_type(stripped):
            ty, trait = parsed_impl
            if trait in {"Drop", "Clone"}:
                lifetime_facts.append(
                    {
                        "version_id": version_id,
                        "rust_file": rel,
                        "line": idx,
                        "fact_type": f"IMPL_{trait.upper()}",
                        "rust_type": ty,
                        "uses_bindings": "[]",
                        "evidence_text": stripped[:500],
                    }
                )
            pending_impls.append((ty, trait))
        if "{" in stripped:
            while pending_structs:
                struct_stack.append((pending_structs.pop(), 0))
            while pending_impls:
                ty, _trait = pending_impls.pop()
                impl_stack.append((ty, 0))
        line_starts_unsafe = bool(re.search(r"\bunsafe\s*\{", stripped))
        active_type = impl_stack[-1][0] if impl_stack else (struct_stack[-1][0] if struct_stack else None)

        if match := PUB_FN_RE.search(stripped):
            if match.group("vis"):
                name = match.group("name")
                api_name = f"{impl_stack[-1][0]}::{name}" if impl_stack else name
                current_fn = (api_name, max(1, _brace_delta(stripped)))
                ret = (match.group("ret") or "()").strip()
                apis.append(
                    {
                        "version_id": version_id,
                        "rust_file": rel,
                        "api_name": api_name,
                        "receiver_type": impl_stack[-1][0] if impl_stack else None,
                        "visibility": match.group("vis"),
                        "return_type": ret,
                        "params": json.dumps(match.group("params").strip()),
                        "uses_bindings": "[]",
                        "line": idx,
                    }
                )
                if code_line and (mapping_type := _return_mapping_type(ret)):
                    error_mappings.append(
                        {
                            "version_id": version_id,
                            "rust_file": rel,
                            "line": idx,
                            "mapping_type": mapping_type,
                            "text": stripped[:500],
                            "nearby_binding_symbol": None,
                            "nearby_api": api_name,
                        }
                    )
            else:
                current_fn = (match.group("name"), max(1, _brace_delta(stripped)))

        for match in BINDING_RE.finditer(line if code_line else ""):
            uses.append(
                {
                    "version_id": version_id,
                    "rust_file": rel,
                    "line": idx,
                    "binding_symbol": match.group("name"),
                    "enclosing_unsafe_block": int(unsafe_depth > 0 or line_starts_unsafe),
                    "enclosing_function": current_fn[0] if current_fn else None,
                    "enclosing_impl": impl_stack[-1][0] if impl_stack else None,
                    "enclosing_type": active_type,
                }
            )

        for mapping_type, needle in ERROR_MAPPING_PATTERNS.items():
            if needle in stripped:
                if code_line:
                    error_mappings.append(
                        {
                            "version_id": version_id,
                            "rust_file": rel,
                            "line": idx,
                            "mapping_type": mapping_type,
                            "text": stripped[:500],
                            "nearby_binding_symbol": None,
                            "nearby_api": current_fn[0] if current_fn else None,
                        }
                    )
        for fact_type, needle in LIFETIME_PATTERNS.items():
            if needle in stripped and not _is_import_line(stripped):
                lifetime_facts.append(
                    {
                        "version_id": version_id,
                        "rust_file": rel,
                        "line": idx,
                        "fact_type": fact_type,
                        "rust_type": active_type,
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
        if struct_stack:
            ty, depth = struct_stack[-1]
            depth += delta
            if depth <= 0:
                struct_stack.pop()
            else:
                struct_stack[-1] = (ty, depth)
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
        mapping["nearby_api"] = mapping.get("nearby_api") or _nearest_api(apis, mapping["line"])
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
    for table in ("rust_binding_uses", "rust_safe_apis", "rust_safety_comments", "rust_lifetime_facts", "rust_error_mappings"):
        conn.execute(f"DELETE FROM {table} WHERE version_id=?", (vid,))
    conn.commit()
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
