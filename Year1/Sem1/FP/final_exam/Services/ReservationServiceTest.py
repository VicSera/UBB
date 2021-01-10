import unittest

from Entities.Room import Room
from Repository.FileRepository import FileRepository
from Repository.Repository import Repository
from Services.ReservationService import ReservationService, ServiceException
from Validator import Validator


class ReservationServiceTest(unittest.TestCase):
    def test__remove__invalid_id(self):
        repo = Repository()
        rooms = FileRepository("../Data/rooms.txt", Room)
        service = ReservationService(repo, rooms, Validator)

        self.assertRaises(ServiceException, service.remove, "1234")

    def test__add__empty_name(self):
        repo = Repository()
        rooms = FileRepository("../Data/rooms.txt", Room)
        service = ReservationService(repo, rooms, Validator)
        name = ""
        type = 1
        num_guests = 1
        arrival_day = 1
        arrival_month = 1
        departure_day = 1
        departure_month = 1
        self.assertRaises(ServiceException, service.add, name, type, num_guests, arrival_day, arrival_month, departure_day, departure_month)

    def test__add__num_guests_wrong(self):
        repo = Repository()
        rooms = FileRepository("../Data/rooms.txt", Room)
        service = ReservationService(repo, rooms, Validator)
        name = "Sera"
        type = 1
        num_guests = 5
        arrival_day = 1
        arrival_month = 1
        departure_day = 1
        departure_month = 1
        self.assertRaises(ServiceException, service.add, name, type, num_guests, arrival_day, arrival_month, departure_day, departure_month)

    def test__add__dates_wrong(self):
        repo = Repository()
        rooms = FileRepository("../Data/rooms.txt", Room)
        service = ReservationService(repo, rooms, Validator)
        name = "Sera"
        type = 1
        num_guests = 1
        arrival_day = 2
        arrival_month = 1
        departure_day = 1
        departure_month = 1
        self.assertRaises(ServiceException, service.add, name, type, num_guests, arrival_day, arrival_month, departure_day, departure_month)
