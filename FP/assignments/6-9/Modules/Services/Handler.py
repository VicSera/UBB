from Modules.Repositories.Repository import Repository


class HandlerError(Exception):
    pass


class HandlerTestObj:
    def __init__(self, id, value):
        self.__id = id
        self.__value = value

    def __eq__(self, other):
        return self.__value == other.value

    @property
    def id(self):
        return self.__id

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_val):
        self.__value = new_val


class Handler:
    def __init__(self, repository):
        self._repository = repository
        # print('Created blank handler')

    def add(self, *values):
        obj = HandlerTestObj(values[0], values[1])
        self._repository.add_element(obj)

    def get_all(self):
        values = []

        if self._repository.has_id:
            for id in self._repository.get_all_ids():
                values.append(self._repository.get_by_id(id))
        else:
            for index in range(self._repository.size):
                values.append(self._repository.access_index(index))

        return values

    def from_ids(self, ids):
        if self._repository.has_id:
            try:
                elements = [self._repository[id] for id in ids]
                return elements
            except KeyError:
                raise HandlerError('No elements found with the given ids')
        else:
            return []

    def remove(self, id):
        removed_element = self._repository.get_by_id(id)
        self._repository.remove_id(id)
        return removed_element

    def update_attribute(self, id, attribute, value):
        return self._repository.update_attribute(id, attribute, value)

    def id_exists(self, id):
        return self._repository.id_exists(id)

    def search(self, id=None, name=None):
        if id is not None:
            return [self._repository.get_by_id(id)]
        elif name is not None:
            return self._repository.search_name(name)