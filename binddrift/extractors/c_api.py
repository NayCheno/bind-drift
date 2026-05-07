from __future__ import annotations

import json
import re
import shutil
import subprocess
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
TYPEDEF_TAG_RE = re.compile(
    r"\btypedef\s+(?P<kind>struct|union|enum)\s+(?P<tag>[A-Za-z_][A-Za-z0-9_]*)?\s*\{(?P<body>.*?)\}\s*"
    r"(?P<alias>[A-Za-z_][A-Za-z0-9_]*)\s*;",
    re.DOTALL,
)
TYPEDEF_SIMPLE_RE = re.compile(
    r"^[ \t]*typedef\s+(?P<target>[^;{}()]+?)\s+(?P<alias>[A-Za-z_][A-Za-z0-9_]*)\s*;",
    re.MULTILINE,
)
STRUCT_START_RE = re.compile(r"\bstruct\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*\{")
FUNCTION_POINTER_RE = re.compile(
    r"(?P<ret>.+?)\(\s*\*\s*(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*\)\s*\((?P<params>.*)\)\s*$",
    re.DOTALL,
)
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


def _normalize_ws(value: str) -> str:
    return " ".join(value.split())


def _strip_c_comments(text: str) -> str:
    text = re.sub(r"/\*.*?\*/", lambda match: "\n" * match.group(0).count("\n"), text, flags=re.DOTALL)
    return re.sub(r"//.*", "", text)


def _extract_type_aliases(text: str) -> dict[str, str]:
    aliases: dict[str, str] = {}
    scrubbed = _strip_c_comments(text)
    for match in TYPEDEF_TAG_RE.finditer(scrubbed):
        kind = match.group("kind")
        tag = match.group("tag")
        alias = match.group("alias")
        aliases[alias] = _normalize_ws(f"{kind} {tag or alias}")
    for match in TYPEDEF_SIMPLE_RE.finditer(scrubbed):
        target = _normalize_ws(match.group("target"))
        alias = match.group("alias")
        if "(*" in target or target.startswith(("struct", "union", "enum")) and "{" in target:
            continue
        aliases[alias] = target
    return aliases


def _normalize_aliases(value: str, aliases: dict[str, str]) -> str:
    normalized = value
    for alias, target in sorted(aliases.items(), key=lambda item: len(item[0]), reverse=True):
        normalized = re.sub(rf"\b{re.escape(alias)}\b", target, normalized)
    return _normalize_ws(normalized)


def _type_qual_type(node: dict[str, Any], aliases: dict[str, str], *, desugar: bool = True) -> str:
    type_info = node.get("type") or {}
    qual_type = type_info.get("desugaredQualType") if desugar else None
    qual_type = qual_type or type_info.get("qualType") or ""
    return _normalize_aliases(qual_type, aliases)


def _clang_return_type(qual_type: str, aliases: dict[str, str]) -> str:
    depth = 0
    for idx, char in enumerate(qual_type):
        if char == "(" and depth == 0:
            return _normalize_aliases(qual_type[:idx].strip(), aliases)
        if char in "(<[":
            depth += 1
        elif char in ")>]" and depth:
            depth -= 1
    return _normalize_aliases(qual_type, aliases)


def _find_matching_brace(text: str, open_idx: int) -> int | None:
    depth = 0
    idx = open_idx
    while idx < len(text):
        char = text[idx]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return idx
        idx += 1
    return None


def _split_c_members(body: str) -> list[str]:
    members: list[str] = []
    start = 0
    depth = 0
    for idx, char in enumerate(body):
        if char in "{([":
            depth += 1
        elif char in "})]" and depth:
            depth -= 1
        elif char == ";" and depth == 0:
            member = body[start:idx].strip()
            if member:
                members.append(member)
            start = idx + 1
    return members


def _anonymous_name(line_no: int, ordinal: int) -> str:
    return f"<anonymous@{line_no}:{ordinal}>"


def _parse_struct_member(member: str, aliases: dict[str, str], line_no: int, ordinal: int) -> dict[str, Any] | None:
    member = _normalize_ws(member)
    if not member or member.startswith(("#", "static_assert")):
        return None
    member = re.sub(r"\b(?:const|volatile)\b", lambda match: match.group(0), member)
    if function_pointer := FUNCTION_POINTER_RE.match(member):
        return {
            "name": function_pointer.group("name"),
            "type": _normalize_aliases(function_pointer.group("ret"), aliases),
            "kind": "function_pointer",
            "params": _parse_params(function_pointer.group("params")),
        }
    nested = re.match(
        r"(?P<kind>struct|union)\s+(?P<tag>[A-Za-z_][A-Za-z0-9_]*)?\s*\{(?P<body>.*)\}\s*(?P<name>[A-Za-z_][A-Za-z0-9_]*)?(?:\s*:\s*(?P<bits>\d+))?$",
        member,
        flags=re.DOTALL,
    )
    if nested:
        nested_body = nested.group("body")
        nested_fields = [
            field
            for inner_ordinal, raw_field in enumerate(_split_c_members(nested_body), start=1)
            if (field := _parse_struct_member(raw_field, aliases, line_no, inner_ordinal))
        ]
        return {
            "name": nested.group("name") or _anonymous_name(line_no, ordinal),
            "type": _normalize_ws(f"{nested.group('kind')} {nested.group('tag') or '<anonymous>'}"),
            "kind": "nested_record" if nested.group("name") else "anonymous_record",
            "fields": nested_fields,
            **({"bit_width": nested.group("bits")} if nested.group("bits") else {}),
        }
    bitfield = re.match(r"(?P<ty>.+?)\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*:\s*(?P<bits>[^:]+)$", member)
    if bitfield:
        return {
            "name": bitfield.group("name"),
            "type": _normalize_aliases(bitfield.group("ty"), aliases),
            "kind": "bitfield",
            "bit_width": bitfield.group("bits").strip(),
        }
    if "(" in member and ")" in member:
        return None
    field = re.match(r"(?P<ty>.+?)\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)(?P<array>(?:\s*\[[^]]*\])*)$", member)
    if not field:
        return None
    field_info: dict[str, Any] = {
        "name": field.group("name"),
        "type": _normalize_aliases(field.group("ty"), aliases),
        "kind": "field",
    }
    if array := field.group("array").strip():
        field_info["array"] = array
    return field_info


def _parse_struct_fields(body: str, aliases: dict[str, str], start_line: int) -> list[dict[str, Any]]:
    fields: list[dict[str, Any]] = []
    running_line = start_line
    for ordinal, member in enumerate(_split_c_members(body), start=1):
        if field := _parse_struct_member(member, aliases, running_line, ordinal):
            fields.append(field)
        running_line += member.count("\n")
    return fields


def _parse_structs(text: str, path: Path, version_id: str, aliases: dict[str, str]) -> list[dict[str, Any]]:
    scrubbed = _strip_c_comments(text)
    structs: list[dict[str, Any]] = []
    seen: set[tuple[str, int]] = set()
    for match in STRUCT_START_RE.finditer(scrubbed):
        if _brace_depth(scrubbed, match.start()) != 0:
            continue
        open_idx = scrubbed.find("{", match.start())
        close_idx = _find_matching_brace(scrubbed, open_idx)
        if close_idx is None:
            continue
        line = _line_for_offset(scrubbed, match.start())
        key = (match.group("name"), line)
        if key in seen:
            continue
        seen.add(key)
        body = scrubbed[open_idx + 1 : close_idx]
        structs.append(
            {
                "version_id": version_id,
                "c_type": match.group("name"),
                "fields": json.dumps(_parse_struct_fields(body, aliases, line + 1), sort_keys=True),
                "size": None,
                "align": None,
                "header_file": str(path),
                "line": line,
            }
        )
    return structs


def _brace_depth(text: str, offset: int) -> int:
    depth = 0
    for char in text[:offset]:
        if char == "{":
            depth += 1
        elif char == "}" and depth:
            depth -= 1
    return depth


def _loc_line(node: dict[str, Any]) -> int:
    loc = node.get("loc") or {}
    if line := loc.get("line"):
        return int(line)
    begin = (node.get("range") or {}).get("begin") or {}
    return int(begin.get("line") or 0)


def _loc_file(node: dict[str, Any]) -> str | None:
    loc = node.get("loc") or {}
    if loc.get("file"):
        return str(loc["file"])
    begin = (node.get("range") or {}).get("begin") or {}
    if begin.get("file"):
        return str(begin["file"])
    return None


def _range_begin_offset(node: dict[str, Any]) -> int | None:
    begin = (node.get("range") or {}).get("begin") or {}
    value = begin.get("offset")
    return int(value) if value is not None else None


def _bit_width(node: dict[str, Any]) -> str | None:
    for child in node.get("inner") or []:
        if child.get("kind") in {"ConstantExpr", "IntegerLiteral"} and child.get("value") is not None:
            return str(child["value"])
        if value := _bit_width(child):
            return value
    return None


def _clang_field_rows(record: dict[str, Any], aliases: dict[str, str], parent_line: int) -> list[dict[str, Any]]:
    fields: list[dict[str, Any]] = []
    pending_record: dict[str, Any] | None = None
    ordinal = 0
    for child in record.get("inner") or []:
        if child.get("kind") == "RecordDecl" and child.get("completeDefinition"):
            line = _loc_line(child) or parent_line
            pending_record = {
                "line": line,
                "begin": _range_begin_offset(child),
                "type": _normalize_ws(f"{child.get('tagUsed') or 'record'} {child.get('name') or '<anonymous>'}"),
                "fields": _clang_field_rows(child, aliases, line),
                "anonymous": not child.get("name"),
            }
            continue
        if child.get("kind") != "FieldDecl":
            continue
        ordinal += 1
        line = _loc_line(child) or parent_line
        field_name = child.get("name") or _anonymous_name(line, ordinal)
        qual_type = _type_qual_type(child, aliases)
        is_function_pointer = "(*)" in qual_type or re.search(r"\(\s*\*\s*\)", qual_type) is not None
        row: dict[str, Any] = {
            "name": field_name,
            "type": qual_type,
            "kind": "function_pointer" if is_function_pointer else "field",
        }
        if child.get("isBitfield"):
            row["kind"] = "bitfield"
            if width := _bit_width(child):
                row["bit_width"] = width
        if pending_record and (child.get("isImplicit") or _range_begin_offset(child) == pending_record.get("begin")):
            row["type"] = pending_record["type"]
            row["kind"] = "anonymous_record" if child.get("isImplicit") or not child.get("name") else "nested_record"
            row["fields"] = pending_record["fields"]
            pending_record = None
        fields.append(row)
    return fields


def _clang_args(path: Path, linux_tree: Path | None) -> list[str]:
    args = ["-x", "c", "-std=gnu11", "-fsyntax-only", "-fno-color-diagnostics", "-Xclang", "-ast-dump=json"]
    if linux_tree:
        args.extend(
            [
                f"-I{linux_tree}",
                f"-I{linux_tree / 'include'}",
                f"-I{linux_tree / 'arch/x86/include'}",
                f"-I{linux_tree / 'arch/x86/include/generated'}",
                "-D__KERNEL__",
                "-D__BINDDRIFT_CLANG_AST__",
            ]
        )
    args.append(str(path))
    return args


def _parse_clang_ast(path: Path, version_id: str, aliases: dict[str, str], linux_tree: Path | None = None) -> tuple[list[dict[str, Any]], list[dict[str, Any]], dict[str, str]] | None:
    clang = shutil.which("clang")
    if not clang:
        return None
    try:
        proc = subprocess.run(
            [clang, *_clang_args(path, linux_tree)],
            text=True,
            capture_output=True,
            timeout=20,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    if not proc.stdout.strip():
        return None
    try:
        ast = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return None
    if proc.returncode != 0 and "TranslationUnitDecl" not in proc.stdout[:2000]:
        return None
    merged_aliases = dict(aliases)
    for node in ast.get("inner") or []:
        if node.get("kind") != "TypedefDecl" or node.get("isImplicit"):
            continue
        if _loc_file(node) and Path(_loc_file(node)).resolve() != path.resolve():
            continue
        name = node.get("name")
        if name:
            merged_aliases[name] = _type_qual_type(node, aliases)

    functions: list[dict[str, Any]] = []
    structs: list[dict[str, Any]] = []
    for node in ast.get("inner") or []:
        loc_file = _loc_file(node)
        if loc_file and Path(loc_file).resolve() != path.resolve():
            continue
        if node.get("isImplicit"):
            continue
        line = _loc_line(node)
        if node.get("kind") == "FunctionDecl" and node.get("name") and line:
            has_body = any(child.get("kind") == "CompoundStmt" for child in node.get("inner") or [])
            params = [
                _normalize_ws(f"{_type_qual_type(param, merged_aliases)} {param.get('name') or ''}".strip())
                for param in node.get("inner") or []
                if param.get("kind") == "ParmVarDecl"
            ]
            functions.append(
                {
                    "version_id": version_id,
                    "c_symbol": node["name"],
                    "return_type": _clang_return_type((node.get("type") or {}).get("qualType") or "", merged_aliases),
                    "params": json.dumps(params, sort_keys=True),
                    "header_file": str(path) if path.suffix == ".h" else "",
                    "definition_file": str(path) if path.suffix == ".c" or has_body else "",
                    "line": line,
                }
            )
        elif node.get("kind") == "RecordDecl" and node.get("completeDefinition") and node.get("name") and line:
            structs.append(
                {
                    "version_id": version_id,
                    "c_type": node["name"],
                    "fields": json.dumps(_clang_field_rows(node, merged_aliases, line), sort_keys=True),
                    "size": None,
                    "align": None,
                    "header_file": str(path),
                    "line": line,
                }
            )
    if not functions and not structs and proc.returncode != 0:
        return None
    return functions, structs, merged_aliases


def _looks_like_function_match(match: re.Match[str]) -> bool:
    name = match.group("name")
    ret = " ".join(match.group("ret").split())
    params = match.group("params")
    matched = match.group(0)
    if name in CONTROL_NAMES:
        return False
    if not ret or ret.lower().startswith(INVALID_RETURN_PREFIXES):
        return False
    if re.search(rf"\(\s*\*\s*{re.escape(name)}\s*\)\s*\(", matched):
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


def _dedupe_rows(rows: list[dict[str, Any]], keys: tuple[str, ...]) -> list[dict[str, Any]]:
    seen: set[tuple[Any, ...]] = set()
    out: list[dict[str, Any]] = []
    for row in rows:
        key = tuple(row.get(name) for name in keys)
        if key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out


def _parse_file(path: Path, version_id: str, linux_tree: Path | None = None) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    aliases = _extract_type_aliases(text)
    clang_rows = _parse_clang_ast(path, version_id, aliases, linux_tree=linux_tree)
    if clang_rows:
        functions, structs, aliases = clang_rows
    else:
        functions = []
        structs = _parse_structs(text, path, version_id, aliases)
    macros: list[dict[str, Any]] = []
    indicators: list[dict[str, Any]] = []
    current_function: tuple[str, int] | None = None
    body_start_by_line: dict[int, str] = {}

    for match in FUNC_RE.finditer(text):
        name = match.group("name")
        if not _looks_like_function_match(match):
            continue
        start_line = _line_for_offset(text, match.start())
        if clang_rows and any(row["c_symbol"] == name and row["line"] == start_line for row in functions):
            if match.group("end") == "{":
                body_start_by_line[_line_for_offset(text, match.end() - 1)] = name
            continue
        row = {
            "version_id": version_id,
            "c_symbol": name,
            "return_type": _normalize_aliases(match.group("ret"), aliases),
            "params": json.dumps([_normalize_aliases(param, aliases) for param in _parse_params(match.group("params"))], sort_keys=True),
            "header_file": str(path) if path.suffix == ".h" else "",
            "definition_file": str(path) if path.suffix == ".c" or match.group("end") == "{" else "",
            "line": start_line,
        }
        functions.append(row)
        if match.group("end") == "{":
            body_start_by_line[_line_for_offset(text, match.end() - 1)] = name

    if clang_rows:
        fallback_structs = {
            row["c_type"]: row
            for row in _parse_structs(text, path, version_id, aliases)
            if row["c_type"] not in {existing["c_type"] for existing in structs}
        }
        structs.extend(fallback_structs.values())

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
    functions = _dedupe_rows(functions, ("version_id", "c_symbol", "header_file", "definition_file", "line"))
    structs = _dedupe_rows(structs, ("version_id", "c_type", "header_file", "line"))
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
        functions, structs, macros, indicators = _parse_file(path, vid, linux_tree=cfg.linux_tree)
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
