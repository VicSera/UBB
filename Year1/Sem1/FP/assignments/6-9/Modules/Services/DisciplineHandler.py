from Modules.Services.Handler import Handler
from Modules.Domain.Discipline import Discipline


class DisciplineHandler(Handler):
    def __init__(self, repository):
        super(DisciplineHandler, self).__init__(repository)
        # self.__initialize_repository()

    def add(self, id, name):
        new_discipline = Discipline(id, name)
        self._repository.add_element(new_discipline)
        return new_discipline

    def __initialize_repository(self):
        """
        Adding the initial values to the disciplines repository
        """
        self._repository.add_element(Discipline(1, 'Algebra'))
        self._repository.add_element(Discipline(2, 'FP'))
        self._repository.add_element(Discipline(3, 'Analysis'))
        self._repository.add_element(Discipline(4, 'CSA'))
        self._repository.add_element(Discipline(5, 'Computer Logic'))