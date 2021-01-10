class Discipline:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def __str__(self):
        return 'ID: {} | Name: {}'.format(self.__id, self.__name)

    def save_string(self):
        return '{},{}\n'.format(self.__id, self.__name)

    def to_dict(self):
        discipline_dict = {
            'id': self.__id,
            'name': self.__name
        }
        return discipline_dict

    @staticmethod
    def from_string(data_string):
        arguments = data_string.split(',')
        return Discipline(int(arguments[0]), arguments[1])

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value