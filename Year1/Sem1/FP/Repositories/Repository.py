from Modules.Exceptions import RepositoryException


class Repository:
    def __init__(self, has_id=True):
        if has_id:
            self._contents = {}  # store as dict for quicker access
        else:
            self._contents = []  # store as list since there is no unique id
        self.__has_id = has_id


    def add_element(self, element):
        """
        Function that lets a handler add an element to a repository
        This works differently for repositories with ID (Student, Discipline), or without ID (Grade)
        :param element: The element to be added
        """
        if self.__has_id:  # Student or Discipline
            if hasattr(element, 'id'):
                if element.id in self._contents.keys():
                    raise RepositoryException('ID not unique')
                self._contents[element.id] = element
            else:
                raise RepositoryException('Element should have an ID')
        else:  # Grade
            if hasattr(element, 'id'):  # Grade shouldn't have an (unique) ID
                raise RepositoryException('Adding an element with ID to a list. Repository is meant for objects without unique IDs')
            self._contents.append(element)

    def get_by_id(self, id):
        """
        Function that returns an element with the corresponding ID
        :param id: The ID of the element to return
        :return: The element found
        """
        if self.__has_id:
            if id not in self._contents.keys():
                raise RepositoryException('No element has id {}'.format(id))
            return self._contents[id]
        else:
            raise RepositoryException('Trying to access by ID when there are no ids stored in this repository')

    def get_all_ids(self):
        """
        Function that returns all possible IDs that can be accessed
        :return:
        """
        if self.__has_id:
            return list(self._contents.keys())
        else:
            raise RepositoryException('Trying to get all IDs but this repository doesn\'t keep a dictionary')

    def access_index(self, index):
        """
        Function that accesses the repository at a given index (twin to get_by_id)
        :param index: The index to return
        """
        if self.__has_id:
            raise RepositoryException('Trying to access an index in a dictionary repository')
        else:
            return self._contents[index]

    def __getitem__(self, item):
        return self._contents[item]

    def remove_id(self, id):
        """
        Function that removes an element with a certain ID
        :param id: The ID to remove
        """
        if self.__has_id:
            try:
                to_be_deleted =  self._contents[id]
                del self._contents[id]
                return to_be_deleted
            except KeyError:
                raise RepositoryException('ID doesn\'t exist')
        else:
            raise RepositoryException('Trying to delete by ID when there is none in the repository')

    def update_attribute(self, id, attribute, value):
        """
        For the element with the given ID, change its given attribute to a given value
        :param id: The ID of the element
        :param attribute: The attribute to look for
        :param value: The new value to assign
        """
        if self.__has_id:
            try:
                old_value =  getattr(self._contents[id], attribute)
                setattr(self._contents[id], attribute, value)
                return old_value
            except KeyError:
                print('The given ID does not exist')
        else:
            raise RepositoryException('This repository has no ID feature')

    def id_exists(self, id):
        """
        Check if a certain ID exists in the repository
        :param id: The ID to look for
        """
        if self.__has_id:
            if id in self._contents.keys():
                return True
            return False
        else:
            raise RepositoryException('Checking if an ID exists in an ID-less repository')

    def remove_by_attribute(self, attribute, value):
        """
        Remove any element that has a given attribute with a certain value
        :param attribute: The attribute to check
        :param value: The value to check against
        """
        deleted = []

        for element in self._contents[:]:
            if getattr(element, attribute) == value:
                deleted.append(element)
                self._contents.remove(element)

        return deleted

    def remove(self, element):
        self._contents.remove(element)

    def search_name(self, target_name):
        matches = []

        if self.__has_id:
            elements = self._contents.values()
        else:
            elements = self._contents

        for element in elements:
            try:
                if target_name.lower() in element.name.lower():
                    matches.append(element)
            except AttributeError:
                print('Element {} has no attribute \'name\''.format(element))

        if len(matches) is 0:
            raise RepositoryException('No matches found for name {}'.format(target_name))

        return matches

    @property
    def size(self):
        return len(self._contents)

    @property
    def has_id(self):
        return self.__has_id

    # def get_contents(self):
    #     return self.__contents