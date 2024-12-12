from car_manager import Car

from unittest import TestCase, main


class CarTests(TestCase):
    def setUp(self):
        self.car = Car('Skoda', 'Octavia', 6, 60)

    def test_init(self):
        self.assertEqual(self.car.make, 'Skoda')
        self.assertEqual(self.car.model, 'Octavia')
        self.assertEqual(self.car.fuel_capacity, 60)
        self.assertEqual(self.car.fuel_consumption, 6)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_make_cannot_be_null_or_empty(self):
        with self.assertRaises(Exception) as exc:
            Car('', 'Octavia', 6, 60)
        self.assertEqual(str(exc.exception), 'Make cannot be null or empty!')

    def test_model_cannot_be_null_or_empty(self):
        with self.assertRaises(Exception) as exc:
            Car('Skoda', '', 6, 60)
        self.assertEqual(str(exc.exception), 'Model cannot be null or empty!')

    def test_fuel_consumption_zero_negative_exception(self):
        with self.assertRaises(Exception) as exc:
            Car('Skoda', 'Octavia', 0, 60)
        self.assertEqual(str(exc.exception), "Fuel consumption cannot be zero or negative!")

        with self.assertRaises(Exception) as exc:
            Car('Skoda', 'Octavia', -0.12, 60)
        self.assertEqual(str(exc.exception), "Fuel consumption cannot be zero or negative!")

    def test_fuel_capacity_zero_negative_exception(self):
        with self.assertRaises(Exception) as exc:
            Car('Skoda', 'Octavia', 6, 0)
        self.assertEqual(str(exc.exception), "Fuel capacity cannot be zero or negative!")

        with self.assertRaises(Exception) as exc:
            Car('Skoda', 'Octavia', 6, -0.12)
        self.assertEqual(str(exc.exception), "Fuel capacity cannot be zero or negative!")

    def test_fuel_amount_negative_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.fuel_amount = -5
        self.assertEqual(str(exc.exception), "Fuel amount cannot be negative!")

    def test_refuel_negative_and_positive_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.refuel(-5)
        self.assertEqual(str(exc.exception), "Fuel amount cannot be zero or negative!")

        self.assertEqual(self.car.fuel_amount, 0)
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount, 10)

    def test_drive_with_enough_and_not_enough_amount(self):
        self.assertEqual(self.car.fuel_amount, 0)
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount, 10)
        self.car.drive(100)
        self.assertEqual(self.car.fuel_amount, 4)

        self.car.refuel(6)
        self.assertEqual(self.car.fuel_amount, 10)
        with self.assertRaises(Exception) as exc:
            self.car.drive(200)
        self.assertEqual(str(exc.exception), "You don't have enough fuel to drive!")
        self.assertEqual(self.car.fuel_amount, 10)


if __name__ == '__main__':
    main()
