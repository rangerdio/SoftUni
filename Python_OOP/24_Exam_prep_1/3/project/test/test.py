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
        # Check state before
        self.assertEqual(self.player.team, "Juventus")

        result = self.player.change_team("PSG")

        # Validate result and state after
        self.assertEqual(result, "Team successfully changed!")
        self.assertEqual(self.player.team, "PSG")

    def test_change_team_invalid(self):
        # Ensure no changes to state for invalid team
        result = self.player.change_team("Chelsea")
        self.assertEqual(result, "Invalid team name!")
        self.assertEqual(self.player.team, "Juventus")

    def test_add_new_achievement_first_time(self):
        # Check achievements length before
        self.assertEqual(len(self.player.achievements), 0)

        result = self.player.add_new_achievement("Golden Boot")

        # Validate result and achievements length after
        self.assertEqual(result, "Golden Boot has been successfully added to the achievements collection!")
        self.assertEqual(self.player.achievements["Golden Boot"], 1)
        self.assertEqual(len(self.player.achievements), 1)

    def test_add_new_achievement_increment(self):
        # Add initial achievement
        self.player.add_new_achievement("Golden Boot")

        # Check state before second addition
        self.assertEqual(self.player.achievements["Golden Boot"], 1)

        # Add the same achievement again
        self.player.add_new_achievement("Golden Boot")

        # Validate the updated count
        self.assertEqual(self.player.achievements["Golden Boot"], 2)
        self.assertEqual(len(self.player.achievements), 1)

    def test_lt_operator_player_with_more_goals(self):
        player2 = SoccerPlayer("Lionel Messi", 35, 800, "PSG")

        # Ensure correct comparison
        result = self.player < player2
        self.assertEqual(result, "Lionel Messi is a top goal scorer! S/he scored more than Cristiano Ronaldo.")

    def test_lt_operator_player_with_fewer_goals(self):
        player2 = SoccerPlayer("Neymar Jr", 29, 500, "PSG")

        # Ensure correct comparison
        result = self.player < player2
        self.assertEqual(result, "Cristiano Ronaldo is a better goal scorer than Neymar Jr.")

    def test_lt_operator_players_with_equal_goals(self):
        player2 = SoccerPlayer("Lionel Messi", 35, 700, "PSG")

        # Check comparison logic when goals are equal
        result = self.player < player2
        self.assertEqual(result, "Cristiano Ronaldo is a better goal scorer than Lionel Messi.")

    def test_multiple_team_changes(self):
        # Change team to PSG
        result1 = self.player.change_team("PSG")
        self.assertEqual(result1, "Team successfully changed!")
        self.assertEqual(self.player.team, "PSG")

        # Change team back to Juventus
        result2 = self.player.change_team("Juventus")
        self.assertEqual(result2, "Team successfully changed!")
        self.assertEqual(self.player.team, "Juventus")

    def test_invalid_and_valid_achievement_operations(self):
        # Add valid achievement
        result1 = self.player.add_new_achievement("Golden Boot")
        self.assertEqual(result1, "Golden Boot has been successfully added to the achievements collection!")
        self.assertEqual(self.player.achievements["Golden Boot"], 1)

        # Try adding the same achievement again
        result2 = self.player.add_new_achievement("Golden Boot")
        self.assertEqual(result2, "Golden Boot has been successfully added to the achievements collection!")
        self.assertEqual(self.player.achievements["Golden Boot"], 2)

    def test_initial_achievements_dictionary_empty(self):
        # Verify that achievements is an empty dictionary upon initialization
        self.assertEqual(len(self.player.achievements), 0)

    def test_multiple_achievements(self):
        # Add multiple achievements and validate length
        self.player.add_new_achievement("Golden Boot")
        self.player.add_new_achievement("Player of the Year")

        self.assertEqual(len(self.player.achievements), 2)
        self.assertIn("Golden Boot", self.player.achievements)
        self.assertIn("Player of the Year", self.player.achievements)


if __name__ == "__main__":
    unittest.main()
