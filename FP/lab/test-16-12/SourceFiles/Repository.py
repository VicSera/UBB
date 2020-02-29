class RepositoryException(Exception):
    pass


class Repository:
    def __init__(self):
        self._contents = {}

    def add(self, element):
        # add an element to the contents of the repository
        self._contents[element.id] = element

    def remove(self, id):
        # remove an element by id
        try:
            self._contents.pop(id)
        except KeyError:
            raise RepositoryException('ID not existent')

    def get(self, id):
        # get an element by id
        try:
            return self._contents[id]
        except KeyError:
            raise RepositoryException('ID not existent')

    def get_all_ids(self):
        # get a list of all ids
        return list(self._contents.keys())

    def get_all_students(self):
        # get a list of all students
        return list(self._contents.values())
