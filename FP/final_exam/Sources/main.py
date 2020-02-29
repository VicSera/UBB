from Entities.Reservation import Reservation
from Entities.Room import Room
from Exceptions import ApplicationException
from Repository.FileRepository import FileRepository
from Services.ReservationService import ReservationService
from UI.ConsoleUI import ConsoleUI
from Validator import Validator

rooms = FileRepository("Data/rooms.txt", Room)

# TODO: move validation
if len(set(Room.found_types)) != 3:
    raise ApplicationException("Not all room types are present")

reservations = FileRepository("Data/reservations.txt", Reservation)
reservation_service = ReservationService(reservations, rooms, Validator)

ui = ConsoleUI(reservation_service)