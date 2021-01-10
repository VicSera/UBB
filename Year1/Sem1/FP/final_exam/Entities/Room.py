class Room:
    found_types = []

    def __init__(self, number, type):
        self.__number = number
        self.__type = type

    @staticmethod
    def from_line(number_str, type_str):
        try:
            room = Room(int(number_str), int(type_str))
            Room.found_types.append(room.type)
            return room
        except ValueError:
            raise Exception("Room file format was not respected. Exiting")

    def __str__(self):
        return "Room: {} Maximum number of guests: {}".format(self.number, self.type)

    @property
    def number(self):
        return self.__number

    @property
    def id(self):
        return self.__number

    @property
    def type(self):
        return self.__type