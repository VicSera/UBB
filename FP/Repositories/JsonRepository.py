import json

from Modules.Exceptions import RepositoryException
from Modules.Repositories.Repository import Repository


class JsonRepository(Repository):
    def __init__(self, file_name, class_constructor, has_id=True):
        super().__init__(has_id)
        self.__file_name = file_name
        self.__class_constructor = class_constructor

        self.__load_data()

    def add_element(self, element):
        super().add_element(element)
        self.__flush_changes_to_file()

    def __load_data(self):
        try:
            with open(self.__file_name) as file:
                json_data = file.read()
                file_contents = json.loads(json_data)
                for object_data in file_contents:
                    if type(self._contents) is list:
                        self._contents.append(self.__class_constructor(*object_data.values()))
                    else:
                        self._contents[object_data['id']] = self.__class_constructor(*object_data.values())
        except FileNotFoundError as fnferror:
            raise RepositoryException(fnferror)
        except:
            pass

    def __flush_changes_to_file(self):
        try:
            dict_to_save = self.__convert_to_json()
            with open(self.__file_name, 'w') as file:
                converted_contents = json.dumps(dict_to_save)
                file.write(converted_contents)
        except FileNotFoundError as fnferror:
            raise RepositoryException(fnferror)

    def __convert_to_json(self):
        elements = self._contents
        if type(self._contents) is dict:
            elements = self._contents.values()
        list_of_dicts = []

        for element in elements:
            list_of_dicts.append(element.to_dict())
        return list_of_dicts

    def remove_id(self, id):
        return_value = super().remove_id(id)
        self.__flush_changes_to_file()
        return return_value

    def remove(self, element):
        return_value = super().remove(element)
        self.__flush_changes_to_file()
        return return_value

    def remove_by_attribute(self, attribute, value):
        return_value = super().remove_by_attribute(attribute, value)
        self.__flush_changes_to_file()
        return return_value

    def update_attribute(self, id, attribute, value):
        return_value = super().update_attribute(id, attribute, value)
        self.__flush_changes_to_file()
        return return_value