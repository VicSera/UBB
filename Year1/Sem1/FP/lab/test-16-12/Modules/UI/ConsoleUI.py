import traceback


class ConsoleUI:
    def __init__(self, student_service):
        self.__student_service = student_service

        self.__launch()

    def __launch(self):
        options = [
            'Add a student',
            'Give bonus',
            'Display all',
            'Display filtered'
        ]
        functions = [
            self.__add_student,
            self.__give_bonus,
            self.__display_all,
            self.__display_filtered
        ]

        while True:
            try:
                user_choice = ConsoleUI.choose(options)
                functions[user_choice]()
            except Exception as exception:
                print(exception)
                # traceback.print_exc()

    def __add_student(self):
        # get arguments for adding a student
        id = ConsoleUI.get_input(int, 'ID: ')
        name = ConsoleUI.get_input(str, 'Name: ')
        attendance_count = ConsoleUI.get_input(int, 'Attendance count: ')
        grade = ConsoleUI.get_input(int, 'Grade: ')

        self.__student_service.add_student(id, name, attendance_count, grade)

    def __give_bonus(self):
        # get arguments for adding a bonus
        minimum_attendances = ConsoleUI.get_input(int, 'Minimum attendances: ')
        bonus = ConsoleUI.get_input(int, 'Bonus: ')

        self.__student_service.give_bonus(minimum_attendances, bonus)

    def __display_all(self):
        # display all students
        students = self.__student_service.get_all_students()

        for student in students:
            print(student)

    def __display_filtered(self):
        # display filtered students
        target_string = ConsoleUI.get_input(str, 'Give a string: ')

        students = self.__student_service.get_all_with_name(target_string)
        for student in students:
            print(student)

    @staticmethod
    def get_input(type, message):
        # get input of the given type
        while True:
            try:
                user_input = type(input(message))
                return user_input
            except:
                continue

    @staticmethod
    def choose(options):
        # make the user choose between the given options, returning the index of the chosen one
        for index, option in enumerate(options):
            print('{}. {}'.format(index + 1, option))

        while True:
            try:
                user_choice = int(input('--> '))
                if user_choice in range(1, len(options) + 1):
                    return user_choice - 1
            except:
                continue