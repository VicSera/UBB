from Exceptions import ApplicationException


class ValidationError(ApplicationException):
    pass


class Validator:
    @staticmethod
    def __validate_name(reservation):
        if reservation.name == "":
            raise ValidationError("Name cannot be empty")

    @staticmethod
    def __validate_dates(reservation):
        if reservation.arrival > reservation.departure:
            raise ValidationError("Arrival date cannot be before departure date")

    @staticmethod
    def __validate_guests(reservation, room_type):
        if reservation.num_guests < 1 or reservation.num_guests > 4:
            raise ValidationError("Number of guests is incorrect (has to be between 1 and 4")
        if reservation.num_guests > room_type:
            raise ValidationError("Number of guests doesn\'t fit in the specified room type")

    @staticmethod
    def validate(reservation, room_type):
        Validator.__validate_dates(reservation)
        Validator.__validate_guests(reservation, room_type)
        Validator.__validate_name(reservation)
