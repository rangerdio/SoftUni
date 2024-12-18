import unittest
from project.restaurant import Restaurant

class TestRestaurant(unittest.TestCase):

    def setUp(self):
        self.restaurant = Restaurant("Fine Dine", 3)

    def test_initialization(self):
        self.assertEqual(self.restaurant.name, "Fine Dine")
        self.assertEqual(self.restaurant.capacity, 3)
        self.assertEqual(self.restaurant.waiters, [])

    def test_name_setter_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.restaurant.name = "  "
        self.assertEqual(str(context.exception), "Invalid name!")

    def test_capacity_setter_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.restaurant.capacity = -1
        self.assertEqual(str(context.exception), "Invalid capacity!")

    def test_add_waiter_success(self):
        result = self.restaurant.add_waiter("John")
        self.assertEqual(result, "The waiter John has been added.")
        self.assertIn({"name": "John"}, self.restaurant.waiters)

    def test_add_waiter_duplicate(self):
        self.restaurant.add_waiter("John")
        result = self.restaurant.add_waiter("John")
        self.assertEqual(result, "The waiter John already exists!")

    def test_add_waiter_no_capacity(self):
        self.restaurant.add_waiter("John")
        self.restaurant.add_waiter("Alice")
        self.restaurant.add_waiter("Bob")
        result = self.restaurant.add_waiter("Charlie")
        self.assertEqual(result, "No more places!")

    def test_remove_waiter_success(self):
        self.restaurant.add_waiter("John")
        result = self.restaurant.remove_waiter("John")
        self.assertEqual(result, "The waiter John has been removed.")
        self.assertNotIn({"name": "John"}, self.restaurant.waiters)

    def test_remove_waiter_not_found(self):
        result = self.restaurant.remove_waiter("John")
        self.assertEqual(result, "No waiter found with the name John.")

    def test_get_total_earnings(self):
        self.restaurant.add_waiter("John")
        self.restaurant.waiters[0]["total_earnings"] = 200
        self.restaurant.add_waiter("Alice")
        self.restaurant.waiters[1]["total_earnings"] = 300
        total = self.restaurant.get_total_earnings()
        self.assertEqual(total, 500)

    def test_get_waiters_with_earnings_filter(self):
        self.restaurant.add_waiter("John")
        self.restaurant.waiters[0]["total_earnings"] = 200
        self.restaurant.add_waiter("Alice")
        self.restaurant.waiters[1]["total_earnings"] = 300
        self.restaurant.add_waiter("Bob")
        self.restaurant.waiters[2]["total_earnings"] = 150

        filtered_waiters = self.restaurant.get_waiters(min_earnings=200)
        self.assertEqual(len(filtered_waiters), 2)
        self.assertIn({"name": "John", "total_earnings": 200}, filtered_waiters)
        self.assertIn({"name": "Alice", "total_earnings": 300}, filtered_waiters)

if __name__ == "__main__":
    unittest.main()