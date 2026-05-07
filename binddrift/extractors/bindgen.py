from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from binddrift.config import Config
from binddrift.db import connect, initialize, upsert_many
from binddrift.kernel import default_version_id


EXTERN_FUNCTION_RE = re.compile(
    r"pub\s+fn\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*\((?P<params>.*?)\)\s*(?:->\s*(?P<ret>[^;]+))?;",
    re.DOTALL,
)
STRUCT_RE = re.compile(r"pub\s+struct\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*\{")
FIELD_RE = re.compile(r"pub\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*):\s*(?P<ty>[^,]+),?")
CONST_RE = re.compile(
    r"pub\s+const\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*):\s*(?P<ty>[^=]+)=\s*(?P<value>[^;]+);",
    re.DOTALL,
)
MEM_PATH = r"::(?:core|std)::mem"
PTR_PATH = r"::(?:core|std)::ptr"
LAYOUT_SIZE_RE = re.compile(rf"assert_eq!\s*\(\s*{MEM_PATH}::size_of::<(?P<ty>[^>]+)>\s*\(\s*\)\s*,\s*(?P<size>\d+)usize", re.DOTALL)
LAYOUT_ALIGN_RE = re.compile(rf"assert_eq!\s*\(\s*{MEM_PATH}::align_of::<(?P<ty>[^>]+)>\s*\(\s*\)\s*,\s*(?P<align>\d+)usize", re.DOTALL)
LAYOUT_OFFSET_RE = re.compile(
    r"assert_eq!\s*\(\s*unsafe\s*\{\s*&\s*\(\s*\*\s*\(\s*0\s+as\s+\*const\s+(?P<ty>[^)]+)\s*\)\s*\)\s*\.(?P<field>[A-Za-z_][A-Za-z0-9_]*)"
    r"\s+as\s+\*const\s+_\s+as\s+usize\s*\}\s*,\s*(?P<offset>\d+)usize",
    re.DOTALL,
)
LAYOUT_OFFSET_NULL_RE = re.compile(
    rf"assert_eq!\s*\(\s*unsafe\s*\{{\s*&\s*\(\s*\*\s*\(\s*{PTR_PATH}::null::<(?P<ty>[^>]+)>\s*\(\s*\)\s*\)\s*\)\s*\.(?P<field>[A-Za-z_][A-Za-z0-9_]*)"
    r"\s+as\s+\*const\s+_\s+as\s+usize\s*\}\s*,\s*(?P<offset>\d+)usize",
    re.DOTALL,
)
LAYOUT_OFFSET_ADDR_OF_RE = re.compile(
    rf"assert_eq!\s*\(\s*(?:unsafe\s*\{{\s*)?(?:{PTR_PATH}::)?addr_of!\s*\(\s*\(\*(?P<ptr>[A-Za-z_][A-Za-z0-9_]*)\)\.(?P<field>[A-Za-z_][A-Za-z0-9_]*)\s*\)"
    r"\s+as\s+usize\s+-\s*(?P=ptr)\s+as\s+usize\s*(?:\})?\s*,\s*(?P<offset>\d+)usize",
    re.DOTALL,
)
LAYOUT_SIZE_CONST_RE = re.compile(rf"const\s+_\s*:\s*\[\s*\(\)\s*;\s*(?P<size>\d+)usize\s*\]\s*=\s*\[\s*\(\)\s*;\s*{MEM_PATH}::size_of::<(?P<ty>[^>]+)>\s*\(\s*\)\s*\]", re.DOTALL)
LAYOUT_ALIGN_CONST_RE = re.compile(rf"const\s+_\s*:\s*\[\s*\(\)\s*;\s*(?P<align>\d+)usize\s*\]\s*=\s*\[\s*\(\)\s*;\s*{MEM_PATH}::align_of::<(?P<ty>[^>]+)>\s*\(\s*\)\s*\]", re.DOTALL)
LAYOUT_OFFSET_OF_ASSERT_RE = re.compile(rf"assert_eq!\s*\(\s*{MEM_PATH}::offset_of!\s*\(\s*(?P<ty>[A-Za-z_][A-Za-z0-9_]*)\s*,\s*(?P<field>[A-Za-z_][A-Za-z0-9_]*)\s*\)\s*,\s*(?P<offset>\d+)usize", re.DOTALL)
LAYOUT_OFFSET_OF_CONST_RE = re.compile(rf"const\s+_\s*:\s*\[\s*\(\)\s*;\s*(?P<offset>\d+)usize\s*\]\s*=\s*\[\s*\(\)\s*;\s*{MEM_PATH}::offset_of!\s*\(\s*(?P<ty>[A-Za-z_][A-Za-z0-9_]*)\s*,\s*(?P<field>[A-Za-z_][A-Za-z0-9_]*)\s*\)\s*\]", re.DOTALL)
LAYOUT_SIZE_INDEX_RE = re.compile(rf"\[[^\]]*Size of[^\]]*\]\s*\[\s*{MEM_PATH}::size_of::<(?P<ty>[^>]+)>\s*\(\s*\)\s*-\s*(?P<size>\d+)usize\s*\]", re.DOTALL)
LAYOUT_ALIGN_INDEX_RE = re.compile(rf"\[[^\]]*Alignment of[^\]]*\]\s*\[\s*{MEM_PATH}::align_of::<(?P<ty>[^>]+)>\s*\(\s*\)\s*-\s*(?P<align>\d+)usize\s*\]", re.DOTALL)
LAYOUT_OFFSET_OF_INDEX_RE = re.compile(rf"\[[^\]]*Offset of[^\]]*\]\s*\[\s*{MEM_PATH}::offset_of!\s*\(\s*(?P<ty>[A-Za-z_][A-Za-z0-9_]*)\s*,\s*(?P<field>[A-Za-z_][A-Za-z0-9_]*)\s*\)\s*-\s*(?P<offset>\d+)usize\s*\]", re.DOTALL)


@dataclass
class BindingFacts:
    functions: list[dict[str, Any]]
    structs: list[dict[str, Any]]
    consts: list[dict[str, Any]]
    layouts: list[dict[str, Any]]
    missing_files: list[str]


def _line_for_offset(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def _split_top_level(value: str) -> list[str]:
    parts: list[str] = []
    start = 0
    depth = 0
    pairs = {"(": ")", "<": ">", "[": "]"}
    closers = set(pairs.values())
    for idx, char in enumerate(value):
        if char in pairs:
            depth += 1
        elif char in closers and depth:
            depth -= 1
        elif char == "," and depth == 0:
            parts.append(value[start:idx].strip())
            start = idx + 1
    tail = value[start:].strip()
    if tail:
        parts.append(tail)
    return parts


def _parse_params(params: str) -> list[dict[str, str]]:
    out = []
    for raw in _split_top_level(" ".join(params.split())):
        if ":" in raw:
            name, ty = raw.split(":", 1)
            out.append({"name": name.strip(), "type": ty.strip()})
        else:
            out.append({"name": "", "type": raw})
    return out


def _tree_sitter_parser() -> Any | None:
    try:
        from tree_sitter import Language, Parser
        import tree_sitter_rust
    except Exception:
        return None
    parser = Parser()
    try:
        parser.language = Language(tree_sitter_rust.language())
    except Exception:
        return None
    return parser


def _node_text(node: Any) -> str:
    return node.text.decode("utf-8", errors="replace") if getattr(node, "text", None) is not None else ""


def _line(node: Any) -> int:
    return int(node.start_point.row) + 1


def _child_by_type(node: Any, node_type: str) -> Any | None:
    for child in node.children:
        if child.type == node_type:
            return child
    return None


def _iter_nodes(node: Any) -> list[Any]:
    out: list[Any] = []
    stack = [node]
    while stack:
        current = stack.pop()
        out.append(current)
        stack.extend(reversed(current.children))
    return out


def _parse_ts_params(parameters: Any | None) -> list[dict[str, str]]:
    if parameters is None:
        return []
    out: list[dict[str, str]] = []
    for child in parameters.children:
        if child.type != "parameter":
            if child.type == "variadic_parameter":
                out.append({"name": "", "type": "..."})
            continue
        name = child.child_by_field_name("pattern")
        ty = child.child_by_field_name("type")
        out.append({"name": _node_text(name).strip() if name is not None else "", "type": _node_text(ty).strip() if ty is not None else _node_text(child).strip()})
    return out


def _visibility(node: Any) -> str:
    if visibility := _child_by_type(node, "visibility_modifier"):
        return _node_text(visibility).strip()
    return "private"


def _repr_c_lines(root: Any) -> set[int]:
    lines: set[int] = set()
    pending_attrs: list[str] = []
    for child in root.children:
        if child.type == "attribute_item":
            text = _node_text(child).replace(" ", "")
            pending_attrs.append(text)
            continue
        if child.type == "struct_item":
            if any(text.startswith("#[repr(") and ("repr(C" in text or "repr(c" in text) for text in pending_attrs):
                lines.add(_line(child))
            pending_attrs = []
            continue
        if child.type not in {",", ";"}:
            pending_attrs = []
    return lines


def _parse_tree_sitter_file(path: Path, version_id: str, text: str) -> BindingFacts | None:
    parser = _tree_sitter_parser()
    if parser is None:
        return None
    tree = parser.parse(text.encode("utf-8", errors="replace"))
    root = tree.root_node
    if root.has_error:
        return None
    functions: list[dict[str, Any]] = []
    structs: list[dict[str, Any]] = []
    consts: list[dict[str, Any]] = []
    repr_c_lines = _repr_c_lines(root)
    for node in _iter_nodes(root):
        if node.type == "function_signature_item":
            name = node.child_by_field_name("name")
            if name is None or _child_by_type(node, "visibility_modifier") is None:
                continue
            return_type = node.child_by_field_name("return_type")
            functions.append(
                {
                    "version_id": version_id,
                    "rust_symbol": _node_text(name),
                    "c_symbol": _node_text(name),
                    "params": json.dumps(_parse_ts_params(node.child_by_field_name("parameters")), sort_keys=True),
                    "return_type": _node_text(return_type).strip() if return_type is not None else "()",
                    "is_unsafe": 1,
                    "source_file": str(path),
                    "line": _line(node),
                }
            )
        elif node.type == "struct_item" and _child_by_type(node, "visibility_modifier") is not None and _line(node) in repr_c_lines:
            name = node.child_by_field_name("name") or _child_by_type(node, "type_identifier")
            if name is None:
                continue
            fields: list[dict[str, str]] = []
            body = node.child_by_field_name("body") or _child_by_type(node, "field_declaration_list")
            if body is not None:
                for field in body.children:
                    if field.type != "field_declaration":
                        continue
                    field_name = field.child_by_field_name("name") or _child_by_type(field, "field_identifier")
                    field_type = field.child_by_field_name("type")
                    if field_name is not None and field_type is not None:
                        fields.append({"name": _node_text(field_name), "type": _node_text(field_type).strip(), "visibility": _visibility(field)})
            structs.append(
                {
                    "version_id": version_id,
                    "rust_type": _node_text(name),
                    "c_type": _node_text(name),
                    "fields": json.dumps(fields, sort_keys=True),
                    "size": None,
                    "align": None,
                    "source_file": str(path),
                    "line": _line(node),
                    "visibility": _visibility(node),
                }
            )
        elif node.type == "const_item" and _child_by_type(node, "visibility_modifier") is not None:
            name = node.child_by_field_name("name")
            value = node.child_by_field_name("value")
            if name is None:
                continue
            consts.append(
                {
                    "version_id": version_id,
                    "rust_name": _node_text(name),
                    "c_name": _node_text(name),
                    "value": " ".join((_node_text(value) if value is not None else "").split()),
                    "source_file": str(path),
                    "line": _line(node),
                }
            )
    return BindingFacts(functions, structs, consts, _parse_layouts(text, path, version_id), [])


def _layout_types_from_text(text: str) -> dict[str, str]:
    ptr_types: dict[str, str] = {}
    uninit_types: dict[str, str] = {}
    for match in re.finditer(rf"\bconst\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*:\s*{MEM_PATH}::MaybeUninit<(?P<ty>[^>]+)>", text):
        uninit_types[match.group("name")] = match.group("ty").strip()
    for match in re.finditer(rf"\blet\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*=\s*{MEM_PATH}::MaybeUninit::<(?P<ty>[^>]+)>::uninit\(\)\s*;", text):
        uninit_types[match.group("name")] = match.group("ty").strip()
    for match in re.finditer(rf"\blet\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*=\s*{PTR_PATH}::null::<(?P<ty>[^>]+)>\(\)\s*;", text):
        ptr_types[match.group("name")] = match.group("ty").strip()
    for match in re.finditer(r"\blet\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?P<ty>[A-Za-z_][A-Za-z0-9_]*)::UNINIT\.as_ptr\(\)\s*;", text):
        ptr_types[match.group("name")] = match.group("ty").strip()
    for match in re.finditer(r"\blet\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*=\s*(?P<src>[A-Za-z_][A-Za-z0-9_]*)\.as_ptr\(\)\s*;", text):
        if ty := uninit_types.get(match.group("src")):
            ptr_types[match.group("name")] = ty
    for match in re.finditer(r"\blet\s+(?P<name>[A-Za-z_][A-Za-z0-9_]*)\s*:\s*\*const\s+(?P<ty>[A-Za-z_][A-Za-z0-9_]*)\b", text):
        ptr_types[match.group("name")] = match.group("ty").strip()
    return ptr_types


def _db_struct_rows(structs: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [{key: value for key, value in row.items() if key != "visibility"} for row in structs]


def _parse_layouts(text: str, path: Path, version_id: str) -> list[dict[str, Any]]:
    layouts: list[dict[str, Any]] = []
    ptr_types = _layout_types_from_text(text)
    seen: set[tuple[str, str, int | None, int | None, int | None]] = set()

    def add(row: dict[str, Any]) -> None:
        key = (row["rust_type"], row["field_name"], row["size"], row["align"], row["offset"])
        if key in seen:
            return
        seen.add(key)
        layouts.append(row)

    for pattern in (LAYOUT_SIZE_RE, LAYOUT_SIZE_CONST_RE, LAYOUT_SIZE_INDEX_RE):
        for match in pattern.finditer(text):
            add(
                {
                    "version_id": version_id,
                    "rust_type": match.group("ty").strip(),
                    "field_name": "",
                    "size": int(match.group("size")),
                    "align": None,
                    "offset": None,
                    "source_file": str(path),
                    "line": _line_for_offset(text, match.start()),
                }
            )
    for pattern in (LAYOUT_ALIGN_RE, LAYOUT_ALIGN_CONST_RE, LAYOUT_ALIGN_INDEX_RE):
        for match in pattern.finditer(text):
            add(
                {
                    "version_id": version_id,
                    "rust_type": match.group("ty").strip(),
                    "field_name": "",
                    "size": None,
                    "align": int(match.group("align")),
                    "offset": None,
                    "source_file": str(path),
                    "line": _line_for_offset(text, match.start()),
                }
            )
    for pattern in (LAYOUT_OFFSET_RE, LAYOUT_OFFSET_NULL_RE):
        for match in pattern.finditer(text):
            add(
                {
                    "version_id": version_id,
                    "rust_type": match.group("ty").strip(),
                    "field_name": match.group("field"),
                    "size": None,
                    "align": None,
                    "offset": int(match.group("offset")),
                    "source_file": str(path),
                    "line": _line_for_offset(text, match.start()),
                }
            )
    for match in LAYOUT_OFFSET_ADDR_OF_RE.finditer(text):
        add(
            {
                "version_id": version_id,
                "rust_type": ptr_types.get(match.group("ptr"), ""),
                "field_name": match.group("field"),
                "size": None,
                "align": None,
                "offset": int(match.group("offset")),
                "source_file": str(path),
                "line": _line_for_offset(text, match.start()),
            }
        )
    for pattern in (LAYOUT_OFFSET_OF_ASSERT_RE, LAYOUT_OFFSET_OF_CONST_RE, LAYOUT_OFFSET_OF_INDEX_RE):
        for match in pattern.finditer(text):
            add(
                {
                    "version_id": version_id,
                    "rust_type": match.group("ty").strip(),
                    "field_name": match.group("field"),
                    "size": None,
                    "align": None,
                    "offset": int(match.group("offset")),
                    "source_file": str(path),
                    "line": _line_for_offset(text, match.start()),
                }
            )
    return sorted(layouts, key=lambda row: (row["line"], row["rust_type"], row["field_name"], row["size"] or row["align"] or row["offset"] or 0))


def _parse_file(path: Path, version_id: str) -> BindingFacts:
    text = path.read_text(encoding="utf-8", errors="replace")
    if parsed := _parse_tree_sitter_file(path, version_id, text):
        return parsed
    lines = text.splitlines()
    functions: list[dict[str, Any]] = []
    structs: list[dict[str, Any]] = []
    consts: list[dict[str, Any]] = []
    layouts: list[dict[str, Any]] = []
    for match in EXTERN_FUNCTION_RE.finditer(text):
        name = match.group("name")
        functions.append(
            {
                "version_id": version_id,
                "rust_symbol": name,
                "c_symbol": name,
                "params": json.dumps(_parse_params(match.group("params")), sort_keys=True),
                "return_type": " ".join((match.group("ret") or "()").split()),
                "is_unsafe": 1,
                "source_file": str(path),
                "line": _line_for_offset(text, match.start()),
            }
        )
    for match in CONST_RE.finditer(text):
        name = match.group("name")
        consts.append(
            {
                "version_id": version_id,
                "rust_name": name,
                "c_name": name,
                "value": " ".join(match.group("value").split()),
                "source_file": str(path),
                "line": _line_for_offset(text, match.start()),
            }
        )
    i = 0
    while i < len(lines):
        line = lines[i]
        if match := STRUCT_RE.search(line):
            name = match.group("name")
            fields: list[dict[str, str]] = []
            j = i + 1
            depth = line.count("{") - line.count("}")
            while j < len(lines) and depth > 0:
                if field := FIELD_RE.search(lines[j].strip()):
                    fields.append({"name": field.group("name"), "type": field.group("ty").strip()})
                depth += lines[j].count("{") - lines[j].count("}")
                j += 1
            structs.append(
                {
                    "version_id": version_id,
                    "rust_type": name,
                    "c_type": name,
                    "fields": json.dumps(fields, sort_keys=True),
                    "size": None,
                    "align": None,
                    "source_file": str(path),
                    "line": i + 1,
                }
            )
            i = j
        i += 1
    layouts = _parse_layouts(text, path, version_id)
    return BindingFacts(functions, structs, consts, layouts, [])


def extract_bindings(cfg: Config, objtree: Path | None = None, version_id: str | None = None) -> dict[str, Any]:
    cfg.ensure_dirs()
    vid = version_id or default_version_id(cfg)
    obj = objtree or cfg.build_root / vid
    files = [
        obj / "rust/bindings/bindings_generated.rs",
        obj / "rust/bindings/bindings_helpers_generated.rs",
    ]
    facts = BindingFacts([], [], [], [], [])
    for path in files:
        if not path.exists():
            facts.missing_files.append(str(path))
            continue
        parsed = _parse_file(path, vid)
        facts.functions.extend(parsed.functions)
        facts.structs.extend(parsed.structs)
        facts.consts.extend(parsed.consts)
        facts.layouts.extend(parsed.layouts)
    conn = connect(cfg.database)
    initialize(conn)
    upsert_many(conn, "binding_functions", facts.functions)
    upsert_many(conn, "binding_structs", _db_struct_rows(facts.structs))
    upsert_many(conn, "binding_consts", facts.consts)
    upsert_many(conn, "layout_facts", facts.layouts)
    upsert_many(
        conn,
        "extraction_errors",
        [
            {
                "version_id": vid,
                "stage": "bindings",
                "source": path,
                "message": "generated binding file is missing",
                "severity": "warning",
            }
            for path in facts.missing_files
        ],
    )
    return {
        "database": str(cfg.database),
        "version_id": vid,
        "objtree": str(obj),
        "binding_functions": len(facts.functions),
        "binding_structs": len(facts.structs),
        "binding_consts": len(facts.consts),
        "layout_facts": len(facts.layouts),
        "missing_files": facts.missing_files,
    }
