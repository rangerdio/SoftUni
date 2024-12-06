from cat import Cat

from unittest import TestCase, main


class CatTests(TestCase):

    def setUp(self):
        self.my_cat = Cat("Mia")

    def test_init(self):
        self.assertEqual(self.my_cat.name, "Mia")
        self.assertFalse(self.my_cat.fed)
        self.assertFalse(self.my_cat.sleepy)
        self.assertEqual(self.my_cat.size, 0)

    def test_cat_eat(self):
        self.assertEqual(self.my_cat.name, "Mia")
        self.assertFalse(self.my_cat.fed)
        self.assertFalse(self.my_cat.sleepy)
        self.assertEqual(self.my_cat.size, 0)

        self.my_cat.eat()
        self.assertTrue(self.my_cat.fed)
        self.assertTrue(self.my_cat.sleepy)
        self.assertEqual(self.my_cat.size, 1)

        with self.assertRaises(Exception) as ex:
            self.my_cat.eat()
        self.assertEqual(str(ex.exception), 'Already fed.')
        self.assertTrue(self.my_cat.fed)
        self.assertTrue(self.my_cat.sleepy)
        self.assertEqual(self.my_cat.size, 1)

    def test_cat_sleep(self):
        self.assertFalse(self.my_cat.sleepy)

        with self.assertRaises(Exception) as ex:
            self.my_cat.sleep()
        self.assertEqual(str(ex.exception), 'Cannot sleep while hungry')

        self.my_cat.eat()
        self.assertTrue(self.my_cat.sleepy)
        self.my_cat.sleep()
        self.assertFalse(self.my_cat.sleepy)


if __name__ == '__main__':
    main()
