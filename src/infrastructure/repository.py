from dataclasses import dataclass

from sqlalchemy.engine.base import Engine

from src.domain.models.players import Player
from src.infrastructure.postgres.session import session_scope


@dataclass
class PostgresPlayerRepository:
    """Player Repository implementation which used postgres"""

    engine: Engine

    def add(self, player: Player) -> None:
        """Add a player to repository."""

        with session_scope(self.engine) as session:
            session.add(player)
            session.commit()

    def get_by_id(self, id: str) -> Player:
        """Get a Player by its id."""

        with session_scope(self.engine) as session:
            result = session.query(Player).filter(Player.id == id).all()
            return result[0] if result else result

    def get_by_name(self, name: str) -> Player:
        """Get a Player by its name."""

        with session_scope(self.engine) as session:
            result = session.query(Player).filter(Player.name == name).all()
            return result
