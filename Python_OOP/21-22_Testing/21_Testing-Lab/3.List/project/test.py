from extended_list import IntegerList

from unittest import TestCase, main


class IntegerListTests(TestCase):

    def setUp(self):
        self.nums_list = IntegerList(1, 2, 'as', [1, 1])

    def test_init(self):
        nums = IntegerList()
        self.assertEqual(nums._IntegerList__data, [])

        nums = IntegerList('koiko', 1.233, 33, [1, 2, 3], (1, 2, 3))
        self.assertEqual(nums._IntegerList__data, [33])

    def test_get_data(self):
        result = self.nums_list.get_data()
        self.assertEqual(result, [1, 2])

    def test_add_data_raise_error(self):
        self.nums_list.add(3)
        self.assertEqual(self.nums_list._IntegerList__data, [1, 2, 3])

        with self.assertRaises(ValueError) as err:
            self.nums_list.add('koiko')
        self.assertEqual(str(err.exception), "Element is not Integer")
        self.assertEqual(self.nums_list._IntegerList__data, [1, 2, 3])

    def test_add_with_integer(self):
        self.assertEqual(self.nums_list.get_data(), [1, 2])
        koko = self.nums_list.add(3)
        self.assertEqual(koko, [1, 2, 3])
        self.assertEqual(self.nums_list.get_data(), [1, 2, 3])

    def test_remove_index_raise_exception(self):
        self.assertEqual(len(self.nums_list.get_data()), 2)

        with self.assertRaises(IndexError) as err:
            self.nums_list.remove_index(2)
        self.assertEqual(str(err.exception), "Index is out of range")
        self.assertEqual(len(self.nums_list.get_data()), 2)

        with self.assertRaises(IndexError) as err:
            self.nums_list.remove_index(3)
        self.assertEqual(str(err.exception), "Index is out of range")
        self.assertEqual(len(self.nums_list.get_data()), 2)

    def test_remove_valid_index(self):
        value = self.nums_list.get_data()[1]
        self.assertEqual(value, 2)
        self.assertEqual(len(self.nums_list.get_data()), 2)

        ss = self.nums_list.remove_index(1)
        self.assertEqual(self.nums_list.get_data(), [1])
        self.assertEqual(ss, value)
        self.assertEqual(len(self.nums_list.get_data()), 1)

    def test_get_by_index_raise_error(self):
        self.assertEqual(len(self.nums_list.get_data()), 2)

        with self.assertRaises(IndexError) as err:
            self.nums_list.get(2)

        self.assertEqual(str(err.exception), "Index is out of range")

        with self.assertRaises(IndexError) as err:
            self.nums_list.get(3)

        self.assertEqual(str(err.exception), "Index is out of range")

        self.assertEqual(len(self.nums_list.get_data()), 2)

    def test_get_valid_index(self):
        value = self.nums_list.get_data()[0]
        self.assertEqual(value, 1)
        self.assertEqual(len(self.nums_list.get_data()), 2)

        ss = self.nums_list.get(0)
        self.assertEqual(ss, value)
        self.assertEqual(len(self.nums_list.get_data()), 2)

    def test_insert_index_raise_err(self):
        ...

    def test_get_biggest(self):
        self.assertEqual(self.nums_list.get_data(), [1, 2])
        self.assertEqual(self.nums_list.get_biggest(), 2)
        self.assertEqual(self.nums_list.get_data(), [1, 2])



if __name__ == '__main__':
    main()
