from typing import Any

from sqlalchemy import create_engine

DB_USER = "admin"
DB_PASSWORD = "1234"
DB_NAME = "postgres"
DB_HOST = "127.0.0.1"

PSQL_CONNECTION = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

ENGINE_FACTORY = {
    "postgres": create_engine(PSQL_CONNECTION),
    "in_memory": create_engine("sqlite://", echo=True),
}


def engine_factory(engine: str) -> Any:
    """Returns a sqlalchemy engine based on input."""
    try:
        return ENGINE_FACTORY[engine]
    except KeyError:
        print("wrong factory option.")
