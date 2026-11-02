import unittest
from statistics_service import SortBy, StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),  #  4+12 = 16
            Player("Lemieux", "PIT", 45, 54), # 45+54 = 99
            Player("Kurri",   "EDM", 37, 53), # 37+53 = 90
            Player("Yzerman", "DET", 42, 56), # 42+56 = 98
            Player("Gretzky", "EDM", 35, 89)  # 35+89 = 124
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_finds_player(self):
        player = self.stats.search("Gretzky")

        self.assertEqual(player.name, "Gretzky")

    def test_search_returns_none_if_player_is_not_found(self):
        player = self.stats.search("Selanne")

        self.assertIsNone(player)

    def test_team_returns_players_from_team(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)
        self.assertEqual(
            [player.name for player in players],
            ["Semenko", "Kurri", "Gretzky"]
        )

    def test_top_returns_requested_number_of_players_in_order(self):
        players = self.stats.top(3)

        self.assertEqual(len(players), 3)
        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Lemieux", "Yzerman"]
        )

    def test_top_can_sort_by_goals(self):
        players = self.stats.top(3, SortBy.GOALS)

        self.assertEqual(
            [player.name for player in players],
            ["Lemieux", "Yzerman", "Kurri"]
        )

    def test_top_can_sort_by_assists(self):
        players = self.stats.top(3, SortBy.ASSISTS)

        self.assertEqual(
            [player.name for player in players],
            ["Gretzky", "Yzerman", "Lemieux"]
        )
