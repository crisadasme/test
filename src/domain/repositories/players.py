from typing import Protocol

from domain.models.players import Player


class PlayerRepository(Protocol):
    """Repository interface."""

    def add(player: Player) -> None:
        """Add a player to repository."""
        ...

    def get_by_id(id: str) -> Player:
        """Get a player by its id."""
        ...

    def get_by_name(name: str) -> Player:
        """Get a player by its name."""
        ...
