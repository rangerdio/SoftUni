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
        with self.assertRaises(ValueError):
            self.gallery.gallery_name = "123@Art"

    def test_city_validation(self):
        with self.assertRaises(ValueError):
            self.gallery.city = "@ParisBG"

    def test_area_sq_m_validation(self):
        with self.assertRaises(ValueError):
            self.gallery.area_sq_m = -100.0

    def test_add_exhibition(self):
        result = self.gallery.add_exhibition("Impressionism", 2023)
        self.assertEqual(result, 'Exhibition "Impressionism" added for the year 2023.')
        self.assertIn("Impressionism", self.gallery.exhibitions)

        result = self.gallery.add_exhibition("Impressionism", 2023)
        self.assertEqual(result, 'Exhibition "Impressionism" already exists.')

    def test_remove_exhibition(self):
        self.gallery.add_exhibition("Impressionism", 2023)
        result = self.gallery.remove_exhibition("Impressionism")
        self.assertEqual(result, 'Exhibition "Impressionism" removed.')
        self.assertNotIn("Impressionism", self.gallery.exhibitions)

        result = self.gallery.remove_exhibition("NonExistent")
        self.assertEqual(result, 'Exhibition "NonExistent" not found.')

    def test_list_exhibitions_open(self):
        self.gallery.add_exhibition("Impressionism", 2023)
        self.gallery.add_exhibition("Modern Art", 2024)
        result = self.gallery.list_exhibitions()
        self.assertEqual(result, "Impressionism: 2023\nModern Art: 2024")

    def test_list_exhibitions_closed(self):
        self.gallery.open_to_public = False
        result = self.gallery.list_exhibitions()
        self.assertEqual(result, "Gallery KokosArtGallery is currently closed for public! Check for updates later on.")

if __name__ == "__main__":
    unittest.main()
