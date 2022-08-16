from dataclasses import dataclass, field
from typing import List, Optional

from .players import Player


@dataclass
class Team:
    """Team class represents a group of players"""

    id: str
    name: str
    members: Optional[List[Player]] = field(default_factory=lambda: [])

    def add_member(self, player: Player) -> None:
        self.members.append(player)

    def remove_member(self, player: Player) -> None:
        self.members.remove(player)
