from Modules.UI.UI import UI
from Modules.Exceptions import RangeError
from Modules.Undo.UndoManager import UndoManager
from Modules.Undo.UndoHandlers import UndoHandler
import traceback


class MenuUI(UI):
    def __init__(self, discipline_handler, student_handler, grade_handler):
        super(MenuUI, self).__init__(discipline_handler, student_handler, grade_handler)  # initialize all the services and the repository

    def launch(self):
        options = [
            'Add',
            'List',
            'Remove',
            'Update',
            'Search',
            'Statistics',
            'Undo',
            'Redo'
        ]
        functions = [
            self.__add,
            self.__list,
            self.__remove,
            self.__update,
            self.__search,
            self.__statistics,
            UndoManager.undo,
            UndoManager.redo
        ]

        while True:
            user_option = MenuUI.get_user_choice(options)
            try:
                functions[user_option]()
            except Exception as error:
                print(error)
                traceback.print_exc()

    @staticmethod
    def get_user_choice(options):
        for index, option in enumerate(options):
            print('{}. {}'.format(index + 1, option))

        while True:
            try:
                user_input = int(input('--> '))
                if user_input - 1 not in range(len(options)):
                    raise RangeError
                return user_input - 1
            except ValueError:
                print('Invalid input')
            except RangeError:
                print('Input has to be a number between {} and {}'.format(1, len(options)))

    @staticmethod
    def get_input_of_type(type, prompt):
        while True:
            try:
                user_input = type(input(prompt))
                return user_input
            except ValueError:
                print('Invalid input')

    def __add(self):
        """
        Function that makes the user choose between adding a student, a discipline or a grade,
        and then calls the appropriate function
        """
        options = ['Add a student', 'Add a discipline', 'Add a grade']
        functions = [self.__add_student, self.__add_discipline, self.__add_grade]

        user_input = MenuUI.get_user_choice(options)
        functions[user_input]()

    def __remove(self):
        options = ['Remove a student', 'Remove a discipline']
        functions = [self.__remove_student, self.__remove_discipline]

        user_input = MenuUI.get_user_choice(options)
        functions[user_input]()

    @staticmethod
    def __print_values(values):
        for element in values:
            print(element)

    def __list(self):
        options = ['List students', 'List disciplines', 'List grades']
        repository_options = [self._student_handler, self._discipline_handler, self._grade_handler]

        user_input = MenuUI.get_user_choice(options)
        handler = repository_options[user_input]

        values = handler.get_all()
        MenuUI.__print_values(values)

    def __update(self):
        options = ['Update a student', 'Update a discipline']
        functions = [self.__update_student, self.__update_discipline]

        user_input = MenuUI.get_user_choice(options)
        functions[user_input]()

    def __search(self):
        repository_options = ['Search for a student', 'Search for a discipline']
        repository_choice = MenuUI.get_user_choice(repository_options)

        if repository_choice is 0:
            handler = self._student_handler
        else:
            handler = self._discipline_handler

        search_options = ['Search by ID', 'Search by name']

        search_choice = MenuUI.get_user_choice(search_options)

        if search_choice is 0:
            id_to_search = MenuUI.get_input_of_type(int, 'Please provide an ID: ')
            values = handler.search(id=id_to_search)
        elif search_choice is 1:
            name_to_search = MenuUI.get_input_of_type(str, 'Please provide a name: ')
            values = handler.search(name=name_to_search)

        MenuUI.__print_values(values)

    def __statistics(self):
        options = ['Failing students', 'Best students', 'Discipline hierarchy by average grade']
        functions = [self.__list_failing_students, self.__list_best_students, self.__discipline_hierarchy]

        choice = MenuUI.get_user_choice(options)
        functions[choice]()

    def __list_failing_students(self):
        failing_students = self._grade_handler.get_failing_students()
        failing_students = self._student_handler.from_ids(failing_students)

        if len(failing_students) is 0:
            print('No students are currently failing')
        else:
            MenuUI.__print_values(failing_students)

    def __list_best_students(self):
        best_students_with_average = self._grade_handler.get_best_students()

        for student, average in best_students_with_average:
            print('{} had average {}'.format(self._student_handler.search(student)[0], average))

    def __discipline_hierarchy(self):
        discipline_hierarchy = self._grade_handler.get_discipline_hierarchy()

        for discipline, average in discipline_hierarchy:
            print('{} had average {}'.format(self._discipline_handler.search(discipline)[0], average))

    def __add_student(self):
        """
        Function that gets called when the user chose to add a student.
        An ID and a name will be requested, processed by the handler, and then added to the repository
        """
        id = MenuUI.get_input_of_type(int, 'ID: ')
        name = MenuUI.get_input_of_type(str, 'Student name: ')

        student = self._student_handler.add(id, name)

        UndoManager.add_undo_operation(
            self._student_handler, UndoHandler.ADD_STUDENT, student
        )
        UndoManager.flush_operations()



    def __add_discipline(self):
        """
        Function that gets called when the user chose to add a discipline.
        An ID and a name will be requested, processed by the handler, and then added to the repository
        """
        id = MenuUI.get_input_of_type(int, 'ID: ')
        name = MenuUI.get_input_of_type(str, 'Discipline name: ')

        discipline = self._discipline_handler.add(id, name)

        UndoManager.add_undo_operation(
            self._discipline_handler, UndoHandler.ADD_DISCIPLNE, discipline
        )
        UndoManager.flush_operations()

    def __add_grade(self):
        """
        Function that gets called when the user chose to add a grade.
        A student ID, a discipline ID and a name will be requested, then
        processed by the handler, and then added to the repository
        """
        discipline_id = MenuUI.get_input_of_type(int, 'Discipline ID: ')
        student_id = MenuUI.get_input_of_type(int, 'Student ID: ')
        value = MenuUI.get_input_of_type(int, 'Grade value: ')

        if not self._student_handler.id_exists(student_id):  # check if the student actually exists
            raise Exception('Student ID does not exist')
        if not self._discipline_handler.id_exists(discipline_id):  # check if the discipline actually exists
            raise Exception('Discipline ID does not exist')

        grade = self._grade_handler.add(discipline_id, student_id, value)

        UndoManager.add_undo_operation(
            self._grade_handler, UndoHandler.ADD_GRADE, grade
        )
        UndoManager.flush_operations()

    def __remove_student(self):
        # remove student
        student_id = MenuUI.get_input_of_type(int, 'Student ID to remove: ')
        student = self._student_handler.remove(student_id)

        # remove his grades
        grades = self._grade_handler.remove_from_student(student_id)

        UndoManager.add_undo_operation(
            self._student_handler, UndoHandler.REMOVE_STUDENT,
            # student.id, student.name
            student
        )

        for grade in grades:
            UndoManager.add_undo_operation(
                self._grade_handler, UndoHandler.REMOVE_GRADE,
                grade
            )

        UndoManager.flush_operations()

    def __remove_discipline(self):
        # remove discipline
        discipline_id = MenuUI.get_input_of_type(int, 'Discipline ID to remove: ')
        discipline = self._discipline_handler.remove(discipline_id)

        # remove all grades at the given discipline
        grades = self._grade_handler.remove_from_discipline(discipline_id)

        UndoManager.add_undo_operation(
            self._discipline_handler, UndoHandler.REMOVE_DISCIPLINE,
            discipline
        )

        for grade in grades:
            UndoManager.add_undo_operation(
                self._grade_handler, UndoHandler.REMOVE_GRADE,
                grade
            )

        UndoManager.flush_operations()

    def __list_students(self):
        self._student_handler.list_all()

    def __list_disciplines(self):
        self._discipline_handler.list_all()

    def __list_grades(self):
        self._grade_handler.list_all()

    def __update_student(self):
        target_id = MenuUI.get_input_of_type(int, 'ID of student to update: ')
        new_name = MenuUI.get_input_of_type(str, 'New name: ')

        old_name = self._student_handler.update_attribute(target_id, 'name', new_name)

        UndoManager.add_undo_operation(self._student_handler, UndoHandler.UPDATE_STUDENT, target_id, 'name', old_name, new_name)
        UndoManager.flush_operations()

    def __update_discipline(self):
        target_id = MenuUI.get_input_of_type(int, 'ID of discipline to update: ')
        new_name = MenuUI.get_input_of_type(str, 'New name: ')

        old_name = self._discipline_handler.update_attribute(target_id, 'name', new_name)

        UndoManager.add_undo_operation(self._discipline_handler, UndoHandler.UPDATE_DISCIPLINE, target_id, 'name', old_name, new_name)
        UndoManager.flush_operations()

    def __search_student(self):
        options = ['Search by ID', 'Search by name']

        choice = MenuUI.get_user_choice(options)

        if choice is 0:
            id_to_search = MenuUI.get_input_of_type(int, 'Please provide an ID: ')
            self._student_handler.search(id=id_to_search)
        elif choice is 1:
            name_to_search = MenuUI.get_input_of_type(str, 'Please provide a name: ')
            self._student_handler.search(name=name_to_search)

    def __search_discipline(self):
        options = ['Search by ID', 'Search by name']

        choice = MenuUI.get_user_choice(options)

        if choice is 0:
            id_to_search = MenuUI.get_input_of_type(int, 'Please provide an ID: ')
            self._student_handler.search(id=id_to_search)
        elif choice is 1:
            name_to_search = MenuUI.get_input_of_type(str, 'Please provide a name: ')
            self._student_handler.search(name=name_to_search)