from sqlalchemy import Column, MetaData, String, Table
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import registry

from src.domain.models.players import Player

metadata = MetaData()
mapper_registry = registry(metadata=metadata)

player_table = Table(
    "player",
    metadata,
    Column("id", String, primary_key=True),
    Column("name", String(50)),
)


def start_mappers(engine: Engine) -> None:
    mapper_registry.map_imperatively(Player, player_table)
    metadata.create_all(engine)
