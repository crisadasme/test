from uuid import uuid4

import pytest

from src.domain.models.players import Player
from src.domain.models.teams import Team
from src.infrastructure.postgres.engines import engine_factory
from src.infrastructure.postgres.orm import start_mappers


@pytest.fixture
def engine() -> Player:
    """Fixture which returns a in memory engine."""
    engine = engine_factory("in_memory")
    start_mappers(engine)
    return engine


@pytest.fixture
def player() -> Player:
    """Fixture which returns a instanced Player."""
    return Player(uuid4(), "test")


@pytest.fixture
def team() -> Team:
    """Fixture which returns a instanced Team."""
    return Team(uuid4(), "test")
