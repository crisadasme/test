from dataclasses import dataclass
from typing import List, Optional

from .teams import Team


@dataclass
class League:
    """
    League class represents a group of team
    which plays over a period for a championship.
    """

    name: str
    participants: Optional[List[Team]]

    def start(self) -> None:
        print(f"Initializing: {self.name} league.")
        print(f"Total Participants: {len(self.participants)} teams.")


@dataclass
class Tournament:
    """
    Tournament class represents which a series of
    Teams compete to achieve the victory.
    """

    name: str
    participants: Optional[List[Team]]

    def start(self) -> None:
        print(f"Initializing: {self.name} tournament.")
        print(f"Total Participants: {len(self.participants)} teams.")
