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
