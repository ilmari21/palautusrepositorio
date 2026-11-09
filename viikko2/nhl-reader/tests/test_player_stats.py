import unittest

from src.player import Player
from src.player_stats import PlayerStats


class PlayerReaderStub:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


def create_player(name, nationality, team, goals, assists):
    return Player({
        "name": name,
        "nationality": nationality,
        "team": team,
        "goals": goals,
        "assists": assists,
        "games": 10,
    })


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        players = [
            create_player("Finn", "FIN", "DAL", 10, 20),
            create_player("Canadian", "CAN", "DAL", 5, 20),
            create_player("Swede", "SWE", "BOS", 15, 5),
            create_player("Finnish teammate", "FIN", "BOS", 5, 5),
        ]
        self.stats = PlayerStats(PlayerReaderStub(players))

    def test_top_scorers_by_nationality_returns_players_sorted_by_points(self):
        players = self.stats.top_scorers_by_nationality("FIN")

        self.assertEqual(["Finn", "Finnish teammate"], [player.name for player in players])
        self.assertEqual([30, 10], [player.points for player in players])

    def test_top_scorers_by_team_returns_players_sorted_by_points(self):
        players = self.stats.top_scorers_by_team("DAL")

        self.assertEqual(["Finn", "Canadian"], [player.name for player in players])
        self.assertEqual([30, 25], [player.points for player in players])

    def test_top_scorers_by_team_returns_empty_list_for_unknown_team(self):
        players = self.stats.top_scorers_by_team("N/A")

        self.assertEqual([], players)


if __name__ == "__main__":
    unittest.main()
