from Exceptions import ApplicationException


class ConsoleUI:
    def __init__(self, reservation_service):
        self.__reservation_service = reservation_service

        self.__launch()

    def __launch(self):
        options = [
            "Add a reservation",
            "List reservations",
            "Remove reservation",
            "List available rooms for a given period",
            "Monthly statistics",
            "Daily statistics"
        ]
        handlers = [
            self.__handle_add_reservation,
            self.__handle_list_reservations,
            self.__handle_remove_reservation,
            self.__handle_list_available_rooms,
            self.__handle_monthly_statistics,
            self.__handle_daily_statistics
        ]

        while True:
            try:
                choice = ConsoleUI.choose(options)
                handlers[choice]()
            except ApplicationException as excp:
                print(excp)

    def __handle_daily_statistics(self):
        statistics = self.__reservation_service.get_daily_statistics()
        for stat in statistics:
            print("{} - {} reservation(s)".format(stat[0], stat[1]))

    def __handle_monthly_statistics(self):
        statistics = self.__reservation_service.get_monthly_statistics()
        for stat in statistics:
            print("{} - {} reservation night(s)".format(stat[0], stat[1]))

    def __handle_list_available_rooms(self):
        arrival_day = ConsoleUI.get_input("Arrival day: ", int)
        arrival_month = ConsoleUI.get_input("Arrival month: ", int)
        departure_day = ConsoleUI.get_input("Departure day: ", int)
        departure_month = ConsoleUI.get_input("Departure month: ", int)

        rooms = self.__reservation_service.get_available_rooms(arrival_month, arrival_day, departure_month, departure_day)
        for room in rooms:
            print(room)

    def __handle_remove_reservation(self):
        id = ConsoleUI.get_input("ID: ", str)
        self.__reservation_service.remove(id)

    def __handle_add_reservation(self):
        name = ConsoleUI.get_input("Family name: ", str)
        room_type = ConsoleUI.get_input("Room type: ", int)
        num_guests = ConsoleUI.get_input("Number of guests: ", int)
        arrival_day = ConsoleUI.get_input("Arrival day: ", int)
        arrival_month = ConsoleUI.get_input("Arrival month: ", int)
        departure_day = ConsoleUI.get_input("Departure day: ", int)
        departure_month = ConsoleUI.get_input("Departure month: ", int)

        self.__reservation_service.add(
            name, room_type, num_guests, arrival_day, arrival_month,
            departure_day, departure_month
        )

    def __handle_list_reservations(self):
        reservations = self.__reservation_service.get_all()
        for reservation in reservations:
            print(reservation)

    @staticmethod
    def get_input(message, type):
        while True:
            try:
                return type(input(message))
            except ValueError:
                print("Invalid input. Please try again")

    @staticmethod
    def choose(options):
        for index, option in enumerate(options):
            print("{}. {}".format(index + 1, option))

        while True:
            try:
                choice = int(input("--> "))
                if choice < 1 or choice > len(options):
                    raise ValueError
                return choice - 1
            except ValueError:
                print('Input has to be a number between 1 and {}'.format(len(options)))