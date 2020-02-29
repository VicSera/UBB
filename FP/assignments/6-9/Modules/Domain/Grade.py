class Grade:
    def __init__(self, discipline_id, student_id, grade_value):
        self.__discipline_id = discipline_id
        self.__student_id = student_id
        self.__grade_value = grade_value

    def __str__(self):
        return 'Discipline ID: {} | Student ID: {} | Grade: {}'.format(self.__discipline_id, self.__student_id, self.__grade_value)

    def __eq__(self, other):
        return (self.__discipline_id == other.discipline_id
                and self.__student_id == other.student_id
                and self.__grade_value == other.grade_value)

    def save_string(self):
        return '{},{},{}\n'.format(self.__discipline_id, self.__student_id, self.__grade_value)

    def to_dict(self):
        grade_dict = {
            'discipline_id': self.__discipline_id,
            'student_id': self.__student_id,
            'grade_value': self.__grade_value
        }
        return grade_dict

    @staticmethod
    def from_string(data_string):
        arguments = data_string.split(',')
        return Grade(int(arguments[0]), int(arguments[1]), int(arguments[2]))

    @property
    def student_id(self):
        return self.__student_id

    @property
    def discipline_id(self):
        return self.__discipline_id

    @property
    def grade_value(self):
        return self.__grade_value

    @grade_value.setter
    def grade_value(self, value):
        self.__grade_value = value