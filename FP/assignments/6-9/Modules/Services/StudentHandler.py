from Modules.Services.Handler import Handler
from Modules.Domain.Student import Student


class StudentHandler(Handler):
    def __init__(self, repository):
        super(StudentHandler, self).__init__(repository)
        # self.__initialize_repository()

    def add(self, id, name):
        new_student = Student(id, name)
        self._repository.add_element(new_student)
        return new_student

    def __initialize_repository(self):
        """
        Adding the initial values to the students repository
        """
        self._repository.add_element(Student(1, 'Victor'))
        self._repository.add_element(Student(2, 'John'))
        self._repository.add_element(Student(3, 'Dan'))
        self._repository.add_element(Student(4, 'Matthew'))
        self._repository.add_element(Student(5, 'Ben'))