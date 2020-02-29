from Modules.Domain.Student import Student
from Modules.Repositories.Repository import Repository, RepositoryException


class FileRepository(Repository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name

        self.__load_data()

    def __load_data(self):
        # initialize the repository with the data from the file
        try:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    arguments = line.strip().split(',')
                    student = Student.from_file(*arguments)
                    super().add(student)
        except FileNotFoundError:
            raise RepositoryException('File not found')

    def __save_to_file(self):
        # save the current state of the repository contents to the file
        try:
            with open(self.__file_name, 'w') as file:
                contents = self._contents.values()
                for element in contents:
                    file.write(element.save_format())
        except FileNotFoundError:
            raise RepositoryException('Could not find specified file to write data')

    def add(self, element):
        # call the parent-class add and save changes
        super().add(element)
        self.__save_to_file()

    def remove(self, id):
        # call the parent-class remove and save changes
        super().remove(id)
        self.__save_to_file()