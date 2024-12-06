from worker import Worker

from unittest import TestCase, main


class WorkerTests(TestCase):

    def test_init(self):
        w = Worker('Ivan', 1000, 100)

        self.assertEqual(w.name, 'Ivan')
        self.assertEqual(w.salary, 1000)
        self.assertEqual(w.energy, 100)
        self.assertEqual(w.money, 0)

    def test_energy_after_rest_method(self):
        w = Worker('Ivan', 1000, 100)
        w.rest()
        self.assertEqual(w.energy, 101)

    def test_work_with_negative(self):
        w = Worker('Ivan', 1000, 1)
        w.work()
        self.assertEqual(w.money, 1000)
        self.assertEqual(w.energy, 0)

        with self.assertRaises(Exception) as ex:
            w.work()
        self.assertEqual(str(ex.exception), 'Not enough energy.')

        self.assertEqual(w.money, 1000)
        self.assertEqual(w.energy, 0)

    def test_get_info(self):
        w = Worker('Ivan', 1000, 100)
        w.work()
        self.assertEqual(w.get_info(), 'Ivan has saved 1000 money.')


if __name__ == '__main__':
    main()
