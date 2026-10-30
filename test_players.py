# test players_EDITED
import unittest
from players_EDITED import Player, Goalkeeper, Striker, Midfielder, Defender, Defender1, Defender2

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = Player("Sam", 10, 100, 100)

    def test_player_moves(self):
        self.player.move(10, 5)
        self.assertEqual(self.player.x, 50)
        self.assertEqual(self.player.y, 50)