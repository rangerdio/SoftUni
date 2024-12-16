import unittest
from project.soccer_player import SoccerPlayer


class TestSoccerPlayer(unittest.TestCase):
    def setUp(self):
        self.player = SoccerPlayer("Cristiano Ronaldo", 36, 700, "Juventus")

    def test_init(self):
        self.assertEqual(self.player.name, "Cristiano Ronaldo")
        self.assertEqual(self.player.age, 36)
        self.assertEqual(self.player.goals, 700)
        self.assertEqual(self.player.team, "Juventus")
        self.assertEqual(self.player.achievements, {})

    def test_change_team_valid(self):
        result = self.player.change_team("PSG")
        self.assertEqual(result, "Team successfully changed!")
        self.assertEqual(self.player.team, "PSG")

    def test_change_team_invalid(self):
        result = self.player.change_team("Chelsea")
        self.assertEqual(result, "Invalid team name!")

    def test_add_new_achievement_first_time(self):
        result = self.player.add_new_achievement("Golden Boot")
        self.assertEqual(result, "Golden Boot has been successfully added to the achievements collection!")
        self.assertIn("Golden Boot", self.player.achievements)
        self.assertEqual(self.player.achievements["Golden Boot"], 1)

    def test_add_new_achievement_increment(self):
        self.player.add_new_achievement("Golden Boot")
        self.player.add_new_achievement("Golden Boot")
        self.assertEqual(self.player.achievements["Golden Boot"], 2)

    def test_lt_operator_player_with_more_goals(self):
        player2 = SoccerPlayer("Lionel Messi", 35, 800, "PSG")
        result = self.player < player2
        self.assertEqual(result, "Lionel Messi is a top goal scorer! S/he scored more than Cristiano Ronaldo.")

    def test_lt_operator_player_with_fewer_goals(self):
        player2 = SoccerPlayer("Neymar Jr", 29, 500, "PSG")
        result = self.player < player2
        self.assertEqual(result, "Cristiano Ronaldo is a better goal scorer than Neymar Jr.")


if __name__ == "__main__":
    unittest.main()
