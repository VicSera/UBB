from Modules.Repositories.Repository import Repository, RepositoryException


class FileRepository(Repository):
    def __init__(self, file_name, contained_class, has_id=True):
        super().__init__(has_id)
        self.__file_name = file_name
        self.__contained_class = contained_class

        self.__load_data()

    def __load_data(self):
        try:
            with open(self.__file_name) as file:
                for line in file:
                    object = self.__contained_class.from_string(line.strip())
                    super().add_element(object)
        except FileNotFoundError as fnferror:
            raise RepositoryException(fnferror)
        except ValueError as verror:
            raise RepositoryException(verror)

    def add_element(self, element):
        super().add_element(element)
        try:
            with open(self.__file_name, 'a') as file:
                file.write(element.save_string())
        except FileNotFoundError as fnferror:
            raise RepositoryException(fnferror)

    def __flush_changes_to_file(self):
        try:
            if type(self._contents) is dict:
                elements = self._contents.values()
            else:
                elements = self._contents
            with open(self.__file_name, 'w') as file:
                for element in elements:
                    file.write(element.save_string())
        except FileNotFoundError as fnferror:
            raise RepositoryException(fnferror)

    def remove(self, element):
        return_value = super().remove(element)
        self.__flush_changes_to_file()
        return return_value

    def remove_by_attribute(self, attribute, value):
        return_value = super().remove_by_attribute(attribute, value)
        self.__flush_changes_to_file()
        return return_value

    def remove_id(self, id):
        return_value = super().remove_id(id)
        self.__flush_changes_to_file()
        return return_value

    def update_attribute(self, id, attribute, value):
        return_value = super().update_attribute(id, attribute, value)
        self.__flush_changes_to_file()
        return return_value