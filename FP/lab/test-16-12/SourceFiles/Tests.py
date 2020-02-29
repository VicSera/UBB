import unittest

from Modules.Domain.Student import Student
from Modules.Domain.StudentValidator import ValidationError
from Modules.Repositories.Repository import Repository
from Modules.Services.StudentService import StudentService


class StudentServiceTest(unittest.TestCase):
    def test_add_student__unique_id__exception(self):
        repository = Repository()
        student_service = StudentService(repository)

        student_service.add_student(1, 'Vic Sera', 10, 10)
        self.assertRaises(ValidationError, student_service.add_student, 1, 'This Will Crash', 10, 10)

    def test_add_student__name_without_2_words__exception(self):
        repository = Repository()
        student_service = StudentService(repository)

        self.assertRaises(ValidationError, student_service.add_student, 1, 'Crash', 10, 10)

    def test_add_student__valid_name__no_exception(self):
        repository = Repository()
        student_service = StudentService(repository)

        student_service.add_student(1, 'Qwe Rty', 10, 10)
        self.assertEqual(1, len(repository.get_all_students()))

    def test_add_student__name_too_short__exception(self):
        repository = Repository()
        student_service = StudentService(repository)

        self.assertRaises(ValidationError, student_service.add_student, 1, 'Li Shen', 10, 10)

    def test_add_student__attendances_negative__exception(self):
        repository = Repository()
        student_service = StudentService(repository)

        self.assertRaises(ValidationError, student_service.add_student, 1, 'Qwe Rty', -10, 10)

    def test_add_student__grade_not_between_1_10__exception(self):
        repository = Repository()
        student_service = StudentService(repository)

        self.assertRaises(ValidationError, student_service.add_student, 1, 'Qwe, Rty', 10, 11)


if __name__ == '__main__':
    unittest.main()