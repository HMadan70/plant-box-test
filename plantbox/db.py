"""The SQLite database. Tables are created from schema.sql when the app starts."""

import sqlite3
from pathlib import Path

from flask import current_app

SCHEMA = Path(__file__).with_name("schema.sql")


def init_db(path):
    with sqlite3.connect(path) as conn:
        conn.executescript(SCHEMA.read_text(encoding="utf-8"))


def connect():
    """A connection to the app's database. Use it as `with db.connect() as conn:`."""
    conn = sqlite3.connect(current_app.config["DATABASE"])
    conn.row_factory = sqlite3.Row  # rows work like dicts: row["name"]
    return conn
