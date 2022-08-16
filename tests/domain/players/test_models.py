import uuid

from src.domain.models.players import Player


def test_player_instance():
    """Test instance of player class."""

    id = uuid.uuid4()
    name = "test"
    player = Player(id, name)

    assert player.name == name
    assert player.id == id
