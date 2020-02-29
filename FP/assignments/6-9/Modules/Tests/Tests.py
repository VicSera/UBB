from Modules.Services.StudentHandler import StudentHandler, Student
from Modules.Services.DisciplineHandler import DisciplineHandler, Discipline
from Modules.Services.GradeHandler import GradeHandler, Grade
from Modules.Services.Handler import Handler, HandlerTestObj, HandlerError
from Modules.Undo.UndoManager import *
from Modules.Undo.UndoHandlers import *
from Modules.Repositories.Repository import *
import unittest


class StudentClassTest(unittest.TestCase):
    def test__name_property(self):
        student = Student(1, 'John')

        self.assertEqual('John', student.name)

    def test__str(self):
        student = Student(1, 'TestStudent')

        self.assertEqual('ID: 1 | Name: TestStudent', str(student))

class DisciplineClassTest(unittest.TestCase):
    def test__name_property(self):
        discipline = Discipline(1, 'TestDiscipline')

        self.assertEqual('TestDiscipline', discipline.name)

    def test__str(self):
        discipline = Discipline(1, 'TestDiscipline')

        self.assertEqual('ID: 1 | Name: TestDiscipline', str(discipline))

class GradeClassTest(unittest.TestCase):
    def test__grade_constructor(self):
        grade = Grade(1, 1, 10)

        self.assertEqual(1, grade.student_id)
        self.assertEqual(1, grade.discipline_id)
        self.assertEqual(10, grade.grade_value)

    def test__str(self):
        grade = Grade(1, 1, 10)

        self.assertEqual('Discipline ID: 1 | Student ID: 1 | Grade: 10', str(grade))

    def test_equ(self):
        grade_1 = Grade(1, 1, 9)
        grade_2 = Grade(1, 1, 10)
        grade_3 = Grade(1, 1, 10)

        self.assertEqual(grade_2, grade_3)
        self.assertNotEqual(grade_1, grade_2)

class DisciplineHandlerTest(unittest.TestCase):
    handler = DisciplineHandler()

    def test__add_discipline__existing_id__exception(self):
        id = 1
        some_name = 'OOP'

        self.assertRaises(RepositoryException, DisciplineHandlerTest.handler.add, id, some_name)

    def test__add_discipline__unique_id__no_exception(self):
        id = 6
        some_name = 'OOP'

        try:  # not expecting an exception
            DisciplineHandlerTest.handler.add(id, some_name)
        except:
            self.assertTrue(False)


class StudentHandlerTest(unittest.TestCase):
    handler = StudentHandler()

    def test__add_student__existing_id__exception(self):
        id = 1
        some_name = 'Victor'

        self.assertRaises(RepositoryException, StudentHandlerTest.handler.add, id, some_name)

    def test__add_student__unique_id__no_exception(self):
        id = 6
        some_name = 'Victor'

        try:  # not expecting an exception
            StudentHandlerTest.handler.add(id, some_name)
            self.assertTrue(False)
        except:
            pass


class GradeHandlerTest(unittest.TestCase):
    def test__add_grade(self):
        grade_handler = GradeHandler()
        grade_handler.add(1, 1, 10)
        grades = grade_handler.get_all()

        self.assertEqual(6, len(grades))
        self.assertEqual(Grade(1, 1, 10), grades[-1])

    def test__delete_from_student(self):
        grade_handler = GradeHandler()
        grade_handler.remove_from_student(1)

        self.assertEqual(4, len(grade_handler.get_all()))

    def test__delete_from_discipline(self):
        grade_handler = GradeHandler()
        grade_handler.remove_from_discipline(2)

        self.assertEqual(2, len(grade_handler.get_all()))

    def test__remove_grade(self):
        grade_handler = GradeHandler()
        grade_handler.add(1, 1, 1)
        grade_handler.remove_entity(Grade(1, 1, 1))

        self.assertEqual(5, len(grade_handler.get_all()))

    def test__failing_students__none(self):
        grade_handler = GradeHandler()

        self.assertEqual(0, len(grade_handler.get_failing_students()))

        grade_handler.add(1, 10, 4)

        self.assertEqual(1, len(grade_handler.get_failing_students()))

    def test__students_hierarchy(self):
        grade_handler = GradeHandler()
        expected_outcome = [1, 2, 3, 4]
        gpas = [10, 9, 8.5, 5]

        best_students = grade_handler.get_best_students()

        for index in range(len(best_students)):
            student = best_students[index][0]
            gpa = best_students[index][1]
            self.assertEqual(student, expected_outcome[index])
            self.assertEqual(gpa, gpas[index])

    def test__discipline_hierarchy(self):
        grade_handler = GradeHandler()
        expected_outcome = [1, 2]
        averages = [9.5, 22 / 3]

        best_disciplines = grade_handler.get_discipline_hierarchy()

        for index in range(len(best_disciplines)):
            discipline = best_disciplines[index][0]
            average = best_disciplines[index][1]

            self.assertEqual(expected_outcome[index], discipline)
            self.assertEqual(averages[index], average)


class HandlerTest(unittest.TestCase):
    def test__add(self):
        handler = Handler()

        handler.add(1, 1)

        self.assertEqual(1, len(handler.get_all()))

    def test__from_ids(self):
        handler = Handler()

        handler.add(1, 1)
        handler.add(2, 1)

        self.assertEqual(handler.get_all()[0], handler.get_all()[1])

        self.assertEqual(2, len(handler.from_ids([1, 2])))
        self.assertEqual(1, len(handler.from_ids([1])))
        self.assertRaises(HandlerError, handler.from_ids, [3])

    def test__obj_setter(self):
        object = HandlerTestObj(1, 1)
        object.value = 5

        self.assertEqual(5, object.value)

    def test__remove(self):
        handler = Handler()
        handler.add(1, 1)
        handler.add(2, 1)

        self.assertEqual(2, len(handler.get_all()))

        handler.remove(1)

        self.assertEqual(1, len(handler.get_all()))

        handler.remove(2)

        self.assertEqual(0, len(handler.get_all()))

    def test__id_exists(self):
        handler = Handler()
        handler.add(1, 1)

        self.assertTrue(handler.id_exists(1))
        self.assertFalse(handler.id_exists(2))

    def test__search(self):
        handler = Handler()
        handler.add(1, 1)
        handler.add(2, 1)
        handler.add(3, 2)

        self.assertEqual(1, len(handler.search(id=1)))


class UndoTester(unittest.TestCase):
    def test__undo__student(self):
        handler = StudentHandler()
        student = handler.add(6, 'TestUndo')

        UndoManager.add_undo_operation(handler, UndoHandler.ADD_STUDENT, student)
        UndoManager.flush_operations()

        UndoManager.undo()
        self.assertEqual(5, len(handler.get_all()))

        UndoManager.redo()
        self.assertEqual(6, len(handler.get_all()))

    def test__undo__grade(self):
        handler = GradeHandler()
        grade_to_remove = Grade(1, 1, 10)
        handler.remove_entity(grade_to_remove)

        UndoManager.add_undo_operation(handler, UndoHandler.REMOVE_GRADE, grade_to_remove)
        UndoManager.flush_operations()

        self.assertEqual(4, len(handler.get_all()))

        UndoManager.undo()

        self.assertEqual(5, len(handler.get_all()))

        UndoManager.redo()

        self.assertEqual(4, len(handler.get_all()))

    def test__undo_update(self):
        handler = StudentHandler()
        old_name = 'Victor'
        new_name = 'Changed'
        handler.update_attribute(1, 'name', new_name)

        UndoManager.add_undo_operation(handler, UndoHandler.UPDATE_STUDENT, 1, 'name', old_name, new_name)
        UndoManager.flush_operations()

        UndoManager.undo()
        self.assertEqual(old_name, handler.search(id=1)[0].name)


class RepositoryTest(unittest.TestCase):
    def test__remove__non_existent_id(self):
        repository = Repository(has_id=True)
        self.assertRaises(RepositoryException, repository.remove_id, 1)

    def test__remove_id__no_id_repo(self):
        repository__no_id = Repository(has_id=False)
        self.assertRaises(RepositoryException, repository__no_id.remove_id, 1)

    def test__access_index__with_id_repo(self):
        repository = Repository(has_id=True)
        self.assertRaises(RepositoryException, repository.access_index, 1)

    def test__get_all_ids(self):
        repository__no_id = Repository(has_id=False)
        self.assertRaises(RepositoryException, repository__no_id.get_all_ids)

    def test__get_by_id(self):
        repository = Repository(has_id=True)
        repository__no_id = Repository(has_id=False)
        self.assertRaises(RepositoryException, repository.get_by_id, 1)
        self.assertRaises(RepositoryException, repository__no_id.get_by_id, 1)

    def test__add(self):
        new_elem = 5 # no id
        repository = Repository(has_id=True)

        self.assertRaises(RepositoryException, repository.add_element, new_elem)

    def test__update(self):
        new_elem = HandlerTestObj(1, 1)
        repository = Repository(has_id=True)

        repository.add_element(new_elem)

        self.assertEqual(1, repository.size)

        repository.update_attribute(1, 'value', 2)
        self.assertEqual(HandlerTestObj(1, 2), repository.get_by_id(1))

    def test__search(self):
        repository = Repository(has_id=True)

        student_1 = Student(10, 'Victor')
        student_2 = Student(11, 'John')
        student_3 = Student(11, 'John No Good')

        repository.add_element(student_1)
        repository.add_element(student_2)
        self.assertRaises(RepositoryException, repository.add_element, student_3)

        search_1 = repository.search_name('Victor')
        self.assertEqual(student_1, search_1[0])
        self.assertEqual(1, len(search_1))

        self.assertRaises(RepositoryException, repository.search_name, 'NameThatDoesn\'tExist')

        repository.add_element(HandlerTestObj(3, 123))
        self.assertRaises(RepositoryException, repository.search_name, 'ThisWillCrash')

        repository = Repository(has_id=False)
        repository.add_element(Grade(1, 1, 1))
        self.assertRaises(RepositoryException, repository.search_name, 'ThisWillCrash')


if __name__ == '__main__':
    unittest.main()