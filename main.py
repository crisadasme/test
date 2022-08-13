"""Create a new League"""
from datetime import datetime
from typing import Any, List, Protocol
from dataclasses import dataclass


class Player(Protocol):
    """Player is the entity representation of a user."""
    name: str


class Team(Protocol):
    """Team is an group of players"""
    name: str
    members: List[Player]


class League(Protocol):
    """League represents a long term competition"""
    name: str
    teams: List[Team]
    created_at: datetime
    updated_at: datetime


@dataclass
class NewmetaLeague:
    name: str
    teams: List[Team]
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()

@dataclass
class NewmetaTeam:
    name: str
    members: List[Player]

@dataclass
class NewmetaPlayer:
    name: str


def new_player(name: str) -> Player:
    """Returns a new instance of a Player class"""
    return NewmetaPlayer(name)

def new_team(name: str, members: List[Player]) -> Team:
    """Returns a new instance of a Team"""
    return NewmetaTeam(name=name, members=members)

def new_league(name: str, teams: List[Team]) -> League:
    """Returns a new league instance"""
    return NewmetaLeague(name, teams)


def main() -> None:
    members = [new_player(name) for name in ["diork", "seyren", "valken"]]
    print(members)

    teams = [new_team(name, members) for name in ["afk", "gg", "liquid"]]

    league = new_league(name="Newmeta League", teams=teams)
    print(league.name)
    print(league.teams)
    print(league.created_at)
    print(league.updated_at)
    
if __name__ == "__main__":
    main()
