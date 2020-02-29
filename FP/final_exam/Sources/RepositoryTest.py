import unittest

from Repository.Repository import Repository, RepositoryException


class TestClass:
    def __init__(self, id):
        self.__id = id

    @property
    def id(self):
        return self.__id

class RepositoryTest(unittest.TestCase):
    def test__repo__add(self):
        repo = Repository()
        repo.add(TestClass(1))

        self.assertEqual(1, repo.get(1).id)

    def test__repo__get(self):
        repo = Repository()

        self.assertRaises(RepositoryException, repo.get, 1)

    def test__repo__remove(self):
        repo = Repository()
        repo.add(TestClass(1))
        repo.remove(1)

        self.assertRaises(RepositoryException, repo.get, 1)