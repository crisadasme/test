from dataclasses import dataclass


@dataclass
class Player:
    """Player class represents an entity user."""

    id: str
    name: str
