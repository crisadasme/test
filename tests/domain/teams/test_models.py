def test_team_instance(player, team):
    """Test instance of Team model class"""

    team.add_member(player)
    assert len(team.members) == 1

    team.remove_member(player)
    assert len(team.members) == 0
