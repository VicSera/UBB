from Exceptions import ApplicationException


class RepositoryException(ApplicationException):
    pass


class Repository:
    def __init__(self):
        self.__contents = {}

    def get(self, id):
        try:
            return self.__contents[id]
        except KeyError:
            raise RepositoryException

    def add(self, object):
        try:
            self.__contents[object.id] = object
        except AttributeError:
            raise RepositoryException

    def remove(self, id):
        try:
            self.__contents.pop(id)
        except KeyError:
            raise RepositoryException("The given ID does not exist")

    def get_all(self):
        return self.__contents.values()

    def is_unique(self, id):
        return id not in self.__contents.keys()
