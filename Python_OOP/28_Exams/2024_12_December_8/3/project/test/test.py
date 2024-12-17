import unittest
from project.senior_student import SeniorStudent


class TestSeniorStudent(unittest.TestCase):
    def setUp(self):
        self.student = SeniorStudent("1234", "John Doe", 3.5)

    def test_init(self):
        self.assertEqual(self.student.student_id, "1234")
        self.assertEqual(self.student.name, "John Doe")
        self.assertEqual(self.student.student_gpa, 3.5)
        self.assertEqual(len(self.student.colleges), 0)

    def test_student_id_valid(self):
        self.student.student_id = "5678"
        self.assertEqual(self.student.student_id, "5678")

    def test_student_id_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.student.student_id = "123"
        self.assertEqual(str(context.exception), "Student ID must be at least 4 digits long!")

    def test_name_valid(self):
        self.student.name = "Jane Doe"
        self.assertEqual(self.student.name, "Jane Doe")

    def test_name_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.student.name = "   "
        self.assertEqual(str(context.exception), "Student name cannot be null or empty!")

    def test_student_gpa_valid(self):
        self.student.student_gpa = 2.5
        self.assertEqual(self.student.student_gpa, 2.5)

    def test_student_gpa_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.student.student_gpa = 1.0
        self.assertEqual(str(context.exception), "Student GPA must be more than 1.0!")

    def test_apply_to_college_success(self):
        result = self.student.apply_to_college(3.0, "Harvard")
        self.assertEqual(result, "John Doe successfully applied to Harvard.")
        self.assertIn("HARVARD", self.student.colleges)

    def test_apply_to_college_failure(self):
        result = self.student.apply_to_college(4.0, "MIT")
        self.assertEqual(result, "Application failed!")
        self.assertNotIn("MIT", self.student.colleges)

    def test_update_gpa_success(self):
        result = self.student.update_gpa(4.0)
        self.assertEqual(result, "Student GPA was successfully updated.")
        self.assertEqual(self.student.student_gpa, 4.0)

    def test_update_gpa_no_change(self):
        result = self.student.update_gpa(1.0)
        self.assertEqual(result, "The GPA has not been changed!")
        self.assertEqual(self.student.student_gpa, 3.5)

    def test_eq_same_gpa(self):
        other_student = SeniorStudent("5678", "Jane Smith", 3.5)
        self.assertTrue(self.student == other_student)

    def test_eq_different_gpa(self):
        other_student = SeniorStudent("5678", "Jane Smith", 3.0)
        self.assertFalse(self.student == other_student)


if __name__ == '__main__':
    unittest.main()
