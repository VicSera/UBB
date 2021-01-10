from Entities.Reservation import Reservation
import datetime
import random

from Exceptions import ApplicationException
from Validator import ValidationError


class ServiceException(ApplicationException):
    pass


class ReservationService:
    def __init__(self, repository, rooms, validator):
        self.__repository = repository
        self.__rooms = rooms
        self.__validator = validator

    def add(self, name, type, num_guests, arrival_day, arrival_month, departure_day, departure_month):
        # Generate id
        id = self.generate_random_id()

        # Get arrival and departure date
        arrival = datetime.date(2020, arrival_month, arrival_day)
        departure = datetime.date(2020, departure_month, departure_day)

        # Find a suitable room
        found = False
        available_rooms = self.get_available_rooms(arrival_month, arrival_day, departure_month, departure_day)
        for room in available_rooms:
            print(room)
            if room.type == type:
                room_number = room.id
                found = True
                break
        if not found:
            raise ServiceException("No rooms of that type are available during the specified period")

        # Create reservation
        reservation = Reservation(
            id, room_number,
            name, num_guests,
            arrival, departure
        )

        # Validate the newly created reservation
        try:
            self.__validator.validate(reservation, type)
        except ValidationError as valid_error:
            raise ServiceException(valid_error)

        # TODO: validate reservation

        self.__repository.add(reservation)

    def get_all(self):
        # Return all the reservations
        return self.__repository.get_all()

    def remove(self, id):
        # Try to remove a reservation by id
        try:
            self.__repository.remove(id)
        except Exception as excp:
            raise ServiceException(excp)

    def get_daily_statistics(self):
        rooms_per_day = {
            "Monday": 0,
            "Tuesday": 0,
            "Wednesday": 0,
            "Thursday": 0,
            "Friday": 0,
            "Saturday": 0,
            "Sunday": 0
        }
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        date = datetime.date(2020, 1, 1)
        end = datetime.date(2021, 1, 1)
        one_day = datetime.timedelta(days=1)

        while date < end:
            reservations_for_date = self.count_rooms_reserved(date)
            order = date.weekday()  # 0 - 6
            rooms_per_day[days[order]] += reservations_for_date

            date += one_day

        statistics = []
        for key in rooms_per_day:
            statistics.append((key, rooms_per_day[key]))

        statistics.sort(key=lambda x: x[1], reverse=True)
        return statistics

    def count_rooms_reserved(self, day):
        counter = 0
        for reservation in self.__repository.get_all():
            if reservation.arrival < day and reservation.departure > day:
                counter += 1
        return counter

    def get_rooms(self):
        pass

    def get_monthly_statistics(self):
        reservations_per_month = {
            "January": 0,
            "February": 0,
            "March": 0,
            "April": 0,
            "May": 0,
            "June": 0,
            "July": 0,
            "August": 0,
            "September": 0,
            "October": 0,
            "November": 0,
            "December": 0
        }

        for order, month in enumerate(list(reservations_per_month.keys())):
            reservations_per_month[month] = self.get_reservation_nights(order + 1)

        statistics = []
        for key in reservations_per_month:
            statistics.append((key, reservations_per_month[key]))
        # print(statistics)

        statistics.sort(key=lambda x: x[1], reverse=True)
        # print(statistics)
        return statistics

    def get_reservation_nights(self, month):
        total = 0

        month_begin = datetime.date(2020, month, 1)
        if month == 12:
            month_end = datetime.date(2020, 12, 30)
        else:
            month_end = datetime.date(2020, month + 1, 1) - datetime.timedelta(days=1)

        for reservation in self.__repository.get_all():
            if reservation.arrival.month == month and reservation.departure.month == month:
                total += (reservation.departure - reservation.arrival).days + 1
            elif reservation.arrival.month == month: # only arrival is in the right month
                total += (month_end - reservation.arrival).days # add only the remaining time until the next month
            elif reservation.departure.month == month: # only departure is in the right month
                total += (reservation.departure - month_begin).days # add only the time spent in the given month
            # Here, both arrival and departure month are different, so we have 2 cases: total miss or enclave
            elif reservation.departure.month < month or reservation.arrival.month > month:
                continue
            elif reservation.arrival.month < month and reservation.departure.month > month:
                total += (month_end - month_begin).days

        return total

    def get_available_rooms(self, arrival_month, arrival_day, departure_month, departure_day):
        arrival = datetime.date(2020, arrival_month, arrival_day)
        departure = datetime.date(2020, departure_month, departure_day)

        return self.find_rooms(arrival, departure)

    def find_rooms(self, arrival, departure, type=None):
        available_rooms = []
        for room in self.__rooms.get_all():
            if type:
                if room.type != type:
                    continue
                if self.__check_room(room.id, arrival, departure):
                    return room.id
            else:
                if self.__check_room(room.id, arrival, departure):
                    available_rooms.append(room)

        if type == None and len(available_rooms) > 0:
            return available_rooms

        raise ServiceException("No rooms available for that period!")

    def __check_room(self, room_number, arrival, departure):
        for reservation in self.__repository.get_all():
            if reservation.room_number != room_number:
                continue
            if (reservation.arrival < arrival and reservation.departure > departure) or \
                (reservation.arrival > arrival and reservation.departure < departure) or \
                (reservation.arrival < arrival and reservation.departure > arrival) or \
                (reservation.arrival < departure and reservation.departure > departure):
                return False
        return True


    def generate_random_id(self):
        while True:
            id = ""
            for digit in range(4):
                id += str(random.randint(0, 9))

            if self.__repository.is_unique(id):
                return id