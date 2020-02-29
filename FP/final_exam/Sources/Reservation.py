import datetime

class Reservation:
    def __init__(self, id, room_number, name, num_guests, arrival, departure):
        self.__id = id
        self.__room_number = room_number
        self.__name = name
        self.__num_guests = num_guests
        self.__arrival = arrival
        self.__departure = departure

    def __str__(self):
        return "{} {} {} {} {}.{} {}.{}".format(
            self.id, self.room_number, self.name, self.num_guests, self.arrival.day, self.arrival.month,
            self.departure.day, self.departure.month
        )

    def save_format(self):
        return "{},{},{},{},{}.{},{}.{}\n".format(
            self.id, self.room_number, self.name, self.num_guests, self.arrival.day, self.arrival.month,
            self.departure.day, self.departure.month
        )

    @staticmethod
    def from_line(id, room_number_str, name, num_guests_str, arrival_str, departure_str):
        try:
            arrival = arrival_str.split('.')
            arrival[0] = int(arrival[0])
            arrival[1] = int(arrival[1])
            arrival = datetime.date(2020, arrival[1], arrival[0])
            departure = departure_str.split('.')
            departure[0] = int(departure[0])
            departure[1] = int(departure[1])
            departure = datetime.date(2020, departure[1], departure[0])
            reservation = Reservation(
                id, int(room_number_str),
                name, int(num_guests_str),
                arrival, departure
            )
            return reservation
        except ValueError:
            raise Exception("Reservation file format was not respected")


    @property
    def id(self):
        return self.__id

    @property
    def room_number(self):
        return self.__room_number

    @property
    def name(self):
        return self.__name

    @property
    def num_guests(self):
        return self.__num_guests

    @property
    def arrival(self):
        return self.__arrival

    @property
    def departure(self):
        return self.__departure