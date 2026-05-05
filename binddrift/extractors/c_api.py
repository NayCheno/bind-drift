from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.kernel import default_version_id


FUNC_RE = re.compile(
    r"^[ \t]*(?P<ret>(?:(?:static|extern|inline|const|struct|enum|unsigned|signed|long|short|void|int|char|bool|"
    r"[A-Za-z_][A-Za-z0-9_]*)[\s\*]+)+?)"
    r"(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*\((?P<params>[^;{}]*)\)\s*(?P<end>[;{])",
    re.DOTALL | re.MULTILINE,
)
STRUCT_RE = re.compile(r"^[ \t]*struct\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*\{")
FIELD_RE = re.compile(r"^[ \t]*(?P<ty>[A-Za-z_][A-Za-z0-9_\s\*\[\]]+)\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)(?:\[[^]]+\])?;")
MACRO_RE = re.compile(r"^[ \t]*#\s*define\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)(?:\([^)]*\))?\s*(?P<value>.*)$")
INCLUDE_RE = re.compile(r"^[ \t]*#\s*include\s+[<\"](?P<path>[^>\"]+)[>\"]")
CONTROL_NAMES = {"if", "for", "while", "switch", "return", "sizeof"}
INVALID_RETURN_PREFIXES = ("return", "else", "case", "if ", "for ", "while ", "switch ", "typedef", "#")

INDICATORS: dict[str, list[re.Pattern[str]]] = {
    "NULL_RETURN": [re.compile(r"\breturn\s+NULL\b")],
    "ERR_PTR_RETURN": [re.compile(r"\bERR_PTR\s*\("), re.compile(r"\breturn\s+ERR_CAST\b")],
    "IS_ERR_CHECK": [re.compile(r"\bIS_ERR\s*\("), re.compile(r"\bPTR_ERR\s*\(")],
    "ERROR_CODE": [re.compile(r"\breturn\s+-E[A-Z0-9_]+\b")],
    "REFCOUNT_GET": [re.compile(r"\b(?:kref_get|refcount_inc(?:_not_zero)?|get_device|[A-Za-z0-9_]+_get)\s*\(")],
    "REFCOUNT_PUT": [re.compile(r"\b(?:kref_put|refcount_dec|put_device|[A-Za-z0-9_]+_put)\s*\(")],
    "ALLOC": [
        re.compile(r"\b(?:[A-Za-z0-9_]*alloc[A-Za-z0-9_]*|[A-Za-z0-9_]*zalloc[A-Za-z0-9_]*|[A-Za-z0-9_]*create[A-Za-z0-9_]*)\s*\("),
        re.compile(r"\b(?:kmalloc|kzalloc|kcalloc|kvmalloc|vmalloc)[A-Za-z0-9_]*\s*\("),
    ],
    "FREE": [re.compile(r"\b(?:kfree[A-Za-z0-9_]*|vfree|[A-Za-z0-9_]+_free|[A-Za-z0-9_]+_destroy)\s*\(")],
    "MAY_SLEEP": [
        re.compile(r"\b(?:might_sleep|mutex_lock|wait_event[A-Za-z0-9_]*|schedule|down_read|down_write)\s*\("),
        re.compile(r"\bGFP_KERNEL\b"),
    ],
    "ATOMIC_CONTEXT": [re.compile(r"\b(?:spin_lock|raw_spin_lock|rcu_read_lock)\s*\("), re.compile(r"\bGFP_ATOMIC\b")],
}


def _paths(cfg: Config, roots: list[str]) -> list[Path]:
    files: list[Path] = []
    for root in roots:
        base = cfg.linux_tree / root
        if base.is_file():
            files.append(base)
        elif base.exists():
            files.extend(path for path in base.rglob("*") if path.suffix in {".h", ".c"})
    return sorted(set(files))


def _relative_to_tree(cfg: Config, path: Path) -> str:
    return str(path.resolve().relative_to(cfg.linux_tree.resolve()))


def _resolve_include(cfg: Config, including_file: Path, include: str) -> Path | None:
    candidates = []
    if include.startswith("."):
        candidates.append((including_file.parent / include).resolve())
    candidates.extend(
        [
            cfg.linux_tree / "include" / include,
            cfg.linux_tree / include,
            (including_file.parent / include).resolve(),
        ]
    )
    for candidate in candidates:
        if candidate.exists() and candidate.is_file() and cfg.linux_tree.resolve() in candidate.resolve().parents:
            return candidate.resolve()
    return None


def binding_closure_roots(cfg: Config, include_helpers: bool = True) -> list[str]:
    """Return C files exposed to Rust through bindings_helper.h and helpers.

    The intent is a bounded Rust-facing C surface, not a recursive preprocessor
    expansion of the whole kernel. We scan direct includes from the binding
    helper plus Rust helper sources.
    """

    helper = cfg.linux_tree / "rust/bindings/bindings_helper.h"
    roots: set[str] = set()
    if helper.exists():
        for raw in helper.read_text(encoding="utf-8", errors="replace").splitlines():
            if match := INCLUDE_RE.match(raw):
                resolved = _resolve_include(cfg, helper, match.group("path"))
                if resolved:
                    roots.add(_relative_to_tree(cfg, resolved))
    if include_helpers and (cfg.linux_tree / "rust/helpers").exists():
        roots.add("rust/helpers")
    return sorted(roots)


def _line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _split_top_level(value: str) -> list[str]:
    parts: list[str] = []
    depth = 0
    start = 0
    for idx, char in enumerate(value):
        if char in "([{":
            depth += 1
        elif char in ")]}" and depth:
            depth -= 1
        elif char == "," and depth == 0:
            parts.append(value[start:idx].strip())
            start = idx + 1
    tail = value[start:].strip()
    if tail and tail != "void":
        parts.append(tail)
    return parts


def _parse_params(params: str) -> list[str]:
    return [" ".join(part.split()) for part in _split_top_level(params)]


def _looks_like_function_match(match: re.Match[str]) -> bool:
    name = match.group("name")
    ret = " ".join(match.group("ret").split())
    params = match.group("params")
    matched = match.group(0)
    if name in CONTROL_NAMES:
        return False
    if not ret or ret.lower().startswith(INVALID_RETURN_PREFIXES):
        return False
    if "(*" in matched or ")(" in matched:
        return False
    if re.search(r"\)\s*(?:[A-Za-z_][A-Za-z0-9_]*|\*)", params):
        return False
    if "return " in params or "\\\\" in params:
        return False
    if name in {"bool", "void", "int", "char"} and "typedef" in ret:
        return False
    return True


def _is_comment_line(stripped: str) -> bool:
    return stripped.startswith(("//", "/*", "*"))


def _indicator_matches(indicator_type: str, raw: str) -> bool:
    code = raw.split("//", 1)[0]
    if indicator_type == "ERROR_CODE" and "ERR_PTR" in code:
        return False
    if indicator_type == "ATOMIC_CONTEXT" and re.search(r"\b(?:spin_lock_init|__spin_lock_init|__raw_spin_lock_init)\s*\(", code):
        return False
    return any(pattern.search(code) for pattern in INDICATORS[indicator_type])


def _parse_file(path: Path, version_id: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    functions: list[dict[str, Any]] = []
    structs: list[dict[str, Any]] = []
    macros: list[dict[str, Any]] = []
    indicators: list[dict[str, Any]] = []
    current_function: tuple[str, int] | None = None
    body_start_by_line: dict[int, str] = {}

    for match in FUNC_RE.finditer(text):
        name = match.group("name")
        if not _looks_like_function_match(match):
            continue
        start_line = _line_for_offset(text, match.start())
        row = {
            "version_id": version_id,
            "c_symbol": name,
            "return_type": " ".join(match.group("ret").split()),
            "params": json.dumps(_parse_params(match.group("params")), sort_keys=True),
            "header_file": str(path) if path.suffix == ".h" else "",
            "definition_file": str(path) if path.suffix == ".c" or match.group("end") == "{" else "",
            "line": start_line,
        }
        functions.append(row)
        if match.group("end") == "{":
            body_start_by_line[_line_for_offset(text, match.end() - 1)] = name

    for idx, raw in enumerate(lines, start=1):
        line = raw.strip()
        if not line or line.startswith("*"):
            continue
        if idx in body_start_by_line:
            current_function = (body_start_by_line[idx], 0)
        if match := FUNC_RE.match(raw):
            name = match.group("name")
            if _looks_like_function_match(match) and match.group("end") == "{":
                current_function = (name, 0)
        if match := MACRO_RE.match(raw):
            macros.append(
                {
                    "version_id": version_id,
                    "name": match.group("name"),
                    "value": match.group("value").strip(),
                    "source_file": str(path),
                    "line": idx,
                }
            )
        if match := STRUCT_RE.match(raw):
            name = match.group("name")
            fields: list[dict[str, str]] = []
            j = idx
            while j < len(lines) and "};" not in lines[j]:
                if field := FIELD_RE.match(lines[j]):
                    fields.append({"name": field.group("name"), "type": " ".join(field.group("ty").split())})
                j += 1
            structs.append(
                {
                    "version_id": version_id,
                    "c_type": name,
                    "fields": json.dumps(fields, sort_keys=True),
                    "size": None,
                    "align": None,
                    "header_file": str(path),
                    "line": idx,
                }
            )
        symbol = current_function[0] if current_function else "<file>"
        if current_function and not _is_comment_line(line):
            for indicator_type in INDICATORS:
                if _indicator_matches(indicator_type, raw):
                    indicators.append(
                        {
                            "version_id": version_id,
                            "c_symbol": symbol,
                            "indicator_type": indicator_type,
                            "evidence_file": str(path),
                            "evidence_line": idx,
                            "evidence_text": raw.strip()[:500],
                            "confidence": 0.7,
                        }
                    )
        if current_function:
            depth = current_function[1] + raw.count("{") - raw.count("}")
            current_function = (current_function[0], depth) if depth > 0 else None
    return functions, structs, macros, indicators


def extract_c_api(cfg: Config, roots: list[str] | None = None, version_id: str | None = None, max_files: int | None = None) -> dict[str, Any]:
    cfg.ensure_dirs()
    vid = version_id or default_version_id(cfg)
    selected_roots = roots or binding_closure_roots(cfg)
    files = _paths(cfg, selected_roots)
    if max_files:
        files = files[:max_files]
    all_functions: list[dict[str, Any]] = []
    all_structs: list[dict[str, Any]] = []
    all_macros: list[dict[str, Any]] = []
    all_indicators: list[dict[str, Any]] = []
    for path in files:
        functions, structs, macros, indicators = _parse_file(path, vid)
        all_functions.extend(functions)
        all_structs.extend(structs)
        all_macros.extend(macros)
        all_indicators.extend(indicators)
    conn = connect(cfg.database)
    initialize(conn)
    for table in ("c_functions", "c_structs", "c_macros", "c_behavior_indicators"):
        conn.execute(f"DELETE FROM {table} WHERE version_id=?", (vid,))
    conn.commit()
    upsert_many(conn, "c_functions", all_functions)
    upsert_many(conn, "c_structs", all_structs)
    upsert_many(conn, "c_macros", all_macros)
    upsert_many(conn, "c_behavior_indicators", all_indicators)
    return {
        "database": str(cfg.database),
        "version_id": vid,
        "roots": selected_roots,
        "root_strategy": "explicit" if roots else "bindings_closure",
        "files": len(files),
        "c_functions": len(all_functions),
        "c_structs": len(all_structs),
        "c_macros": len(all_macros),
        "c_behavior_indicators": len(all_indicators),
    }
