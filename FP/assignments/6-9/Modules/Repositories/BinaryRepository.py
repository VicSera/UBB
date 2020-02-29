from Modules.Repositories.Repository import Repository, RepositoryException
import pickle


class BinaryRepository(Repository):
    def __init__(self, file_name, has_id=True):
        super().__init__(has_id)
        self.__file_name = file_name

        self.__load_data()

    def __load_data(self):
        try:
            with open(self.__file_name, 'rb') as file:
                self._contents = pickle.load(file)
        except:
            pass

    def add_element(self, element):
        super().add_element(element)
        self.__flush_changes_to_file()

    def __flush_changes_to_file(self):
        try:
            with open(self.__file_name, 'wb') as file:
                pickle.dump(self._contents, file)
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