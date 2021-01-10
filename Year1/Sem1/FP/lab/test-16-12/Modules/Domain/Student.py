from Modules.Domain.StudentValidator import ValidationError


class Student:
    def __init__(self, id, name, attendance_count, grade):
        self.__id = id
        self.__name = name
        self.__attendance_count = attendance_count
        self.__grade = grade

    def __str__(self):
        return '{}, {}, {}, {}'.format(self.__id, self.__name, self.__attendance_count, self.__grade)

    @staticmethod
    def from_file(id_string, name, attendance_count_string, grade_string):
        try:
            return Student(int(id_string), name, int(attendance_count_string), int(grade_string))
        except ValueError:
            raise ValidationError('File data is not in the right format')

    def save_format(self):
        return '{},{},{},{}\n'.format(self.__id, self.__name, self.__attendance_count, self.__grade)

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def attendance_count(self):
        return self.__attendance_count

    @attendance_count.setter
    def attendance_count(self, value):
        self.__attendance_count = value

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        self.__grade = value