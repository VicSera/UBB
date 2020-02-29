"""
Determine a calendar date (as year, month, day) starting from two integer numbers
representing the year and the day number inside that year (e.g. day number 32 is February
1st). Take into account leap years.
"""


def is_number(number_to_check):
    """
    Check if a given value can be converted to an integer or not.

    Check if a given value can be converted to an integer or not. Return True if so, otherwise False.

    :param number_to_check: the number to be checked
    :return True if number_to_check is a number, False otherwise
    """
    try:
        int(number_to_check)
        return True
    except ValueError:
        return False


def get_input():
    """
    Obtain input from the user.

    Obtain input from the user. If the input values cannot be converted to an integer, request more input, until the given values are correct.
    The first valid input pair is converted to a pair of integers and returned.

    :return: a pair of integers representing a day and a year
    """
    print("Hello user.",
          "This program will display the calendar date corresponding to a given day of a year.")

    # get year input
    user_input_year = input("Please input a year: ")
    while not is_number(user_input_year):
        print("Wrong input type.")
        user_input_year = input("Please input a valid number: ")

    # get day input
    max_days = 365
    if is_leap_year(int(user_input_year)):
        max_days = 366

    user_input_day = max_days + 1
    while int(user_input_day) > max_days:
        user_input_day = input("Please input a valid day: ")
        while not is_number(user_input_day):
            print("Wrong input type.")
            user_input_day = input("Please input a valid day: ")

    return int(user_input_day), int(user_input_year)


def is_leap_year(year):
    """
    Check if a year is a leap year.

    Check if a year is a leap year. Leap years happen every 4 years.
    If the year is a multiple of 100, an exception is made, and the year is NOT a leap year.
    If the year is a multiple of 400, an exception is made, and the year is a leap year.

    :return: True if the year parameter is a leap year, False otherwise
    """
    if year % 400 == 0:  # multiple of 400 (leap year)
        return True
    elif year % 100 == 0:  # multiple of 100 (non-leap-year)
        return False
    elif year % 4 == 0:  # multiple of 4 (leap year)
        return True
    return False  # non-leap-year


def get_date(day, year):
    """
    Compute the calendar date described by a day and a year.

    Compute the calendar date described by a day and a year. Take into account leap years.

    :param day: user input for day
    :param year: user input for year
    :return: the calendar date corresponding to the day and year parameters
    """

    february_duration = 28
    if is_leap_year(year):  # Taking leap years into account
        february_duration = 29

    # List of all months
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    month_durations = {  # Map between each month and its duration
        "January": 31,
        "February": february_duration,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }

    for month in months:  # for each month in the year
        if day <= month_durations[month]:  # if day is within this month
            return month, day  # return month and day
        else:  # otherwise
            day -= month_durations[month]  # subtract from the days the number of days in the current month


if __name__ == "__main__":
    input_day, input_year = get_input()

    print(get_date(input_day, input_year))
