from __future__ import annotations

import sqlite3
from pathlib import Path


SCHEMA_VERSION = 1


def connect(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def initialize(conn: sqlite3.Connection) -> None:
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS metadata (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
        """
    )
    conn.execute(
        "INSERT OR REPLACE INTO metadata(key, value) VALUES ('schema_version', ?)",
        (str(SCHEMA_VERSION),),
    )
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS versions (
            version_id TEXT PRIMARY KEY,
            git_commit TEXT NOT NULL,
            tag TEXT,
            date TEXT,
            arch TEXT,
            config_hash TEXT,
            rustc_version TEXT,
            clang_version TEXT,
            bindgen_version TEXT
        );

        CREATE TABLE IF NOT EXISTS commits (
            commit_id TEXT PRIMARY KEY,
            parent_id TEXT,
            date TEXT,
            author TEXT,
            subject TEXT,
            message TEXT,
            changed_files TEXT NOT NULL,
            is_rust_related INTEGER NOT NULL,
            is_c_api_related INTEGER NOT NULL
        );

        CREATE TABLE IF NOT EXISTS binding_functions (
            version_id TEXT NOT NULL,
            rust_symbol TEXT NOT NULL,
            c_symbol TEXT NOT NULL,
            params TEXT NOT NULL,
            return_type TEXT,
            is_unsafe INTEGER NOT NULL,
            source_file TEXT NOT NULL,
            line INTEGER NOT NULL,
            PRIMARY KEY(version_id, rust_symbol, source_file, line)
        );

        CREATE TABLE IF NOT EXISTS binding_structs (
            version_id TEXT NOT NULL,
            rust_type TEXT NOT NULL,
            c_type TEXT NOT NULL,
            fields TEXT NOT NULL,
            size INTEGER,
            align INTEGER,
            source_file TEXT NOT NULL,
            line INTEGER NOT NULL,
            PRIMARY KEY(version_id, rust_type, source_file, line)
        );

        CREATE TABLE IF NOT EXISTS binding_consts (
            version_id TEXT NOT NULL,
            rust_name TEXT NOT NULL,
            c_name TEXT NOT NULL,
            value TEXT,
            source_file TEXT NOT NULL,
            line INTEGER NOT NULL,
            PRIMARY KEY(version_id, rust_name, source_file, line)
        );

        CREATE TABLE IF NOT EXISTS layout_facts (
            version_id TEXT NOT NULL,
            rust_type TEXT NOT NULL,
            field_name TEXT NOT NULL,
            size INTEGER,
            align INTEGER,
            offset INTEGER,
            source_file TEXT NOT NULL,
            line INTEGER NOT NULL,
            PRIMARY KEY(version_id, rust_type, field_name, source_file, line)
        );

        CREATE TABLE IF NOT EXISTS rust_binding_uses (
            version_id TEXT NOT NULL,
            rust_file TEXT NOT NULL,
            line INTEGER NOT NULL,
            binding_symbol TEXT NOT NULL,
            enclosing_unsafe_block INTEGER NOT NULL,
            enclosing_function TEXT,
            enclosing_impl TEXT,
            enclosing_type TEXT,
            PRIMARY KEY(version_id, rust_file, line, binding_symbol)
        );

        CREATE TABLE IF NOT EXISTS rust_safe_apis (
            version_id TEXT NOT NULL,
            rust_file TEXT NOT NULL,
            api_name TEXT NOT NULL,
            receiver_type TEXT,
            visibility TEXT,
            return_type TEXT,
            params TEXT NOT NULL,
            uses_bindings TEXT NOT NULL,
            line INTEGER NOT NULL,
            PRIMARY KEY(version_id, rust_file, api_name, line)
        );

        CREATE TABLE IF NOT EXISTS rust_safety_comments (
            version_id TEXT NOT NULL,
            rust_file TEXT NOT NULL,
            line INTEGER NOT NULL,
            text TEXT NOT NULL,
            nearby_binding_symbol TEXT,
            nearby_api TEXT,
            PRIMARY KEY(version_id, rust_file, line)
        );
        """
    )
    conn.commit()


def upsert_many(conn: sqlite3.Connection, table: str, rows: list[dict[str, object]]) -> None:
    if not rows:
        return
    columns = list(rows[0].keys())
    placeholders = ", ".join("?" for _ in columns)
    update = ", ".join(f"{column}=excluded.{column}" for column in columns)
    sql = (
        f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders}) "
        f"ON CONFLICT DO UPDATE SET {update}"
    )
    conn.executemany(sql, [tuple(row[column] for column in columns) for row in rows])
    conn.commit()
