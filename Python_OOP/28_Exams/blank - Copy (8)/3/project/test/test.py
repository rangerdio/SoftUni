import unittest
from project.gallery import Gallery


class TestGallery(unittest.TestCase):

    def setUp(self):
        self.gallery = Gallery("KokosArtGallery", "ParisBG", 156.0, True)

    def test_gallery_initialization(self):
        self.assertEqual(self.gallery.gallery_name, "KokosArtGallery")
        self.assertEqual(self.gallery.city, "ParisBG")
        self.assertEqual(self.gallery.area_sq_m, 156.0)
        self.assertTrue(self.gallery.open_to_public)
        self.assertEqual(self.gallery.exhibitions, {})

    def test_gallery_name_validation(self):
        before_name = self.gallery.gallery_name
        with self.assertRaises(ValueError):
            self.gallery.gallery_name = "123@Art"
        self.assertEqual(self.gallery.gallery_name, before_name)

        with self.assertRaises(ValueError):
            self.gallery.gallery_name = " "

        self.gallery.gallery_name = "A"
        self.assertEqual(self.gallery.gallery_name, "A")

    def test_city_validation(self):
        before_city = self.gallery.city
        with self.assertRaises(ValueError):
            self.gallery.city = "@ParisBG"
        self.assertEqual(self.gallery.city, before_city)

        with self.assertRaises(ValueError):
            self.gallery.city = ""

        self.gallery.city = "B"
        self.assertEqual(self.gallery.city, "B")

    def test_area_sq_m_validation(self):
        before_area = self.gallery.area_sq_m
        with self.assertRaises(ValueError):
            self.gallery.area_sq_m = -100.0
        self.assertEqual(self.gallery.area_sq_m, before_area)

        with self.assertRaises(ValueError):
            self.gallery.area_sq_m = 0

        self.gallery.area_sq_m = 0.1
        self.assertEqual(self.gallery.area_sq_m, 0.1)

    def test_add_exhibition(self):
        before_count = len(self.gallery.exhibitions)
        result = self.gallery.add_exhibition("asd", 1986)
        self.assertEqual(result, 'Exhibition "asd" added for the year 1986.')
        self.assertIn("asd", self.gallery.exhibitions)
        self.assertEqual(len(self.gallery.exhibitions), before_count + 1)

        result = self.gallery.add_exhibition("asd", 1986)
        self.assertEqual(result, 'Exhibition "asd" already exists.')
        self.assertEqual(len(self.gallery.exhibitions), before_count + 1)

        result = self.gallery.add_exhibition("qwe", 3000)
        self.assertEqual(result, 'Exhibition "qwe" added for the year 3000.')
        self.assertIn("qwe", self.gallery.exhibitions)
        self.assertEqual(self.gallery.exhibitions["qwe"], 3000)

    def test_remove_exhibition(self):
        self.gallery.add_exhibition("asd", 1986)
        before_count = len(self.gallery.exhibitions)
        result = self.gallery.remove_exhibition("asd")
        self.assertEqual(result, 'Exhibition "asd" removed.')
        self.assertNotIn("asd", self.gallery.exhibitions)
        self.assertEqual(len(self.gallery.exhibitions), before_count - 1)

        result = self.gallery.remove_exhibition("asd")
        self.assertEqual(result, 'Exhibition "asd" not found.')
        self.assertEqual(len(self.gallery.exhibitions), before_count - 1)

    def test_list_exhibitions_empty(self):
        result = self.gallery.list_exhibitions()
        self.assertEqual(result, "")

        self.gallery.open_to_public = False
        result = self.gallery.list_exhibitions()
        self.assertEqual(result, "Gallery KokosArtGallery is currently closed for public! Check for updates later on.")

    def test_list_exhibitions_open(self):
        self.gallery.add_exhibition("asd", 2023)
        self.gallery.add_exhibition("qwe", 2024)
        result = self.gallery.list_exhibitions()
        self.assertEqual(result, "asd: 2023\nqwe: 2024")

    def test_multiple_exhibitions(self):
        before_count = len(self.gallery.exhibitions)
        self.gallery.add_exhibition("asd", 2023)
        self.gallery.add_exhibition("qwe", 2024)
        self.gallery.add_exhibition("zxc", 2025)
        self.assertEqual(len(self.gallery.exhibitions), before_count + 3)

        result = self.gallery.list_exhibitions()
        self.assertEqual(result, "asd: 2023\nqwe: 2024\nzxc: 2025")

    def test_toggle_open_status(self):
        self.gallery.open_to_public = False
        self.assertFalse(self.gallery.open_to_public)

        self.gallery.open_to_public = True
        self.assertTrue(self.gallery.open_to_public)

    def test_state_reset(self):
        self.gallery.add_exhibition("asd", 2023)
        self.gallery.add_exhibition("qwe", 2024)
        self.gallery.remove_exhibition("asd")
        self.gallery.remove_exhibition("qwe")
        self.assertEqual(len(self.gallery.exhibitions), 0)

    def test_exhibition_year_boundary(self):
        result = self.gallery.add_exhibition("min", 1)
        self.assertEqual(result, 'Exhibition "min" added for the year 1.')
        self.assertEqual(self.gallery.exhibitions["min"], 1)

        result = self.gallery.add_exhibition("max", 9999)
        self.assertEqual(result, 'Exhibition "max" added for the year 9999.')
        self.assertEqual(self.gallery.exhibitions["max"], 9999)

    def test_whitespace_exhibition_name(self):
        result = self.gallery.add_exhibition(" ", 2023)
        self.assertIn(" ", self.gallery.exhibitions)
        self.assertEqual(result, 'Exhibition " " added for the year 2023.')

    def test_case_sensitivity_exhibition_name(self):
        self.gallery.add_exhibition("ASD", 2023)
        result = self.gallery.add_exhibition("asd", 2024)
        self.assertIn("ASD", self.gallery.exhibitions)
        self.assertIn("asd", self.gallery.exhibitions)
        self.assertNotEqual(self.gallery.exhibitions["ASD"], self.gallery.exhibitions["asd"])

    def test_invalid_exhibition_year(self):
        result = self.gallery.add_exhibition("asd", -2023)
        self.assertIn("asd", self.gallery.exhibitions)
        self.assertEqual(self.gallery.exhibitions["asd"], -2023)

    def test_alternate_koko_gallery(self):
        alternate_gallery = Gallery("KokoGallery", "QweCity", 500.00, False)
        self.assertEqual(alternate_gallery.gallery_name, "KokoGallery")
        self.assertEqual(alternate_gallery.city, "QweCity")
        self.assertEqual(alternate_gallery.area_sq_m, 500.00)
        self.assertFalse(alternate_gallery.open_to_public)

        result = alternate_gallery.list_exhibitions()
        self.assertEqual(result, "Gallery KokoGallery is currently closed for public! Check for updates later on.")

        result = alternate_gallery.add_exhibition("asd", 2022)
        self.assertEqual(result, 'Exhibition "asd" added for the year 2022.')
        self.assertIn("asd", alternate_gallery.exhibitions)

        alternate_gallery.open_to_public = True
        result = alternate_gallery.list_exhibitions()
        self.assertEqual(result, "asd: 2022")


if __name__ == "__main__":
    unittest.main()
