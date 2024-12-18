import unittest
from project.furniture import Furniture


class TestFurniture(unittest.TestCase):

    def test_valid_initialization(self):
        furniture = Furniture("Model123", 199.99, (100, 50, 30), True, 20.5)
        self.assertEqual(furniture.model, "Model123")
        self.assertEqual(furniture.price, 199.99)
        self.assertEqual(furniture.dimensions, (100, 50, 30))
        self.assertTrue(furniture.in_stock)
        self.assertEqual(furniture.weight, 20.5)

    def test_invalid_model(self):
        with self.assertRaises(ValueError) as context:
            Furniture("", 199.99, (100, 50, 30))
        self.assertEqual(str(context.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

        with self.assertRaises(ValueError):
            Furniture("A" * 51, 199.99, (100, 50, 30))

    def test_invalid_price(self):
        with self.assertRaises(ValueError) as context:
            Furniture("Model123", -1, (100, 50, 30))
        self.assertEqual(str(context.exception), "Price must be a non-negative number.")

    def test_invalid_dimensions(self):
        with self.assertRaises(ValueError) as context:
            Furniture("Model123", 199.99, (100, 50))
        self.assertEqual(str(context.exception), "Dimensions tuple must contain 3 integers.")

        with self.assertRaises(ValueError) as context:
            Furniture("Model123", 199.99, (100, 50, -30))
        self.assertEqual(str(context.exception), "Dimensions tuple must contain integers greater than zero.")

    def test_invalid_weight(self):
        with self.assertRaises(ValueError) as context:
            Furniture("Model123", 199.99, (100, 50, 30), True, -10)
        self.assertEqual(str(context.exception), "Weight must be greater than zero.")

    def test_get_available_status(self):
        furniture = Furniture("Model123", 199.99, (100, 50, 30), True)
        self.assertEqual(furniture.get_available_status(), "Model: Model123 is currently in stock.")

        furniture.in_stock = False
        self.assertEqual(furniture.get_available_status(), "Model: Model123 is currently unavailable.")

    def test_get_specifications(self):
        furniture = Furniture("Model123", 199.99, (100, 50, 30), weight=20.5)
        self.assertEqual(furniture.get_specifications(),
                         "Model: Model123 has the following dimensions: 100mm x 50mm x 30mm and weighs: 20.5")

        furniture_no_weight = Furniture("Model123", 199.99, (100, 50, 30))
        self.assertEqual(furniture_no_weight.get_specifications(),
                         "Model: Model123 has the following dimensions: 100mm x 50mm x 30mm and weighs: N/A")


if __name__ == "__main__":
    unittest.main()
