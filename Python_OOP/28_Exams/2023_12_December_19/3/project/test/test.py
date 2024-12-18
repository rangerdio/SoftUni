import unittest
from project.climbing_robot import ClimbingRobot

class TestClimbingRobot(unittest.TestCase):

    def setUp(self):
        self.robot = ClimbingRobot("Mountain", "Advanced", 100, 50)

    def test_initialization(self):
        self.assertEqual(self.robot.category, "Mountain")
        self.assertEqual(self.robot.part_type, "Advanced")
        self.assertEqual(self.robot.capacity, 100)
        self.assertEqual(self.robot.memory, 50)
        self.assertEqual(len(self.robot.installed_software), 0)

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            ClimbingRobot("Invalid", "Advanced", 100, 50)

    def test_get_used_capacity(self):
        self.robot.installed_software.append({"name": "Software1", "capacity_consumption": 30, "memory_consumption": 10})
        self.assertEqual(self.robot.get_used_capacity(), 30)

    def test_get_available_capacity(self):
        self.robot.installed_software.append({"name": "Software1", "capacity_consumption": 30, "memory_consumption": 10})
        self.assertEqual(self.robot.get_available_capacity(), 70)

    def test_get_used_memory(self):
        self.robot.installed_software.append({"name": "Software1", "capacity_consumption": 30, "memory_consumption": 10})
        self.assertEqual(self.robot.get_used_memory(), 10)

    def test_get_available_memory(self):
        self.robot.installed_software.append({"name": "Software1", "capacity_consumption": 30, "memory_consumption": 10})
        self.assertEqual(self.robot.get_available_memory(), 40)

    def test_install_software_success(self):
        software = {"name": "Software1", "capacity_consumption": 30, "memory_consumption": 10}
        result = self.robot.install_software(software)
        self.assertIn(software, self.robot.installed_software)
        self.assertEqual(result, "Software 'Software1' successfully installed on Mountain part.")

    def test_install_software_failure(self):
        software = {"name": "Software1", "capacity_consumption": 120, "memory_consumption": 60}
        result = self.robot.install_software(software)
        self.assertNotIn(software, self.robot.installed_software)
        self.assertEqual(result, "Software 'Software1' cannot be installed on Mountain part.")

if __name__ == "__main__":
    unittest.main()
