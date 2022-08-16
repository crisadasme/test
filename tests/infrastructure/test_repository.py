from src.domain.models.players import Player
from src.infrastructure.repository import PostgresPlayerRepository


def test_in_memory_repository(engine):
    """Test player repository using a in memory engine."""

    player1 = Player("1", "test")
    player2 = Player("2", "test")

    repo = PostgresPlayerRepository(engine)

    # adding player1 to repository
    repo.add(player1)
    fetched_player = repo.get_by_name(player1.name)
    assert len(fetched_player) == 1

    # adding player2 to repository
    repo.add(player2)
    fetched_player = repo.get_by_name(player2.name)
    assert len(fetched_player) == 2

    # retrieving player by its id
    fetched_player = repo.get_by_id(player1.id)
    assert fetched_player.id == player1.id
