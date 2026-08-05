import os
import sqlite3
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


DATABASE_PATH = Path(
    os.getenv(
        "DATABASE_PATH",
        "./data/lulito.db"
    )
)


def get_connection() -> sqlite3.Connection:

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    connection.row_factory = sqlite3.Row

    connection.execute(
        "PRAGMA foreign_keys = ON"
    )

    return connection