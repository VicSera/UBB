"""
12. Determine the age of a person, in number of days. Take into account leap years, as well as the
date of birth and current date (year, month, day).
"""

from datetime import date


def is_leap_year(year):
    """
    Check if a year is a leap year.

    Check if a year is a leap year. Leap years happen every 4 years.
    If the year is a multiple of 100, an exception is made, and the year is NOT a leap year.
    If the year is a multiple of 400, an exception is made, and the year is a leap year.

    :return: True if the year is a leap year, False otherwise
    """

    if year % 400 == 0:  # multiple of 400 (leap year)
        return True
    elif year % 100 == 0:  # multiple of 100 (non-leap-year)
        return False
    elif year % 4 == 0:  # multiple of 4 (leap year)
        return True
    return False  # non-leap-year


def is_valid(day, month, year):
    """
    Check if a date is valid.

    Check if a date is valid, taking into account leap years and lenght of each month
    :param day: day part of the date
    :param month: month part of the date
    :param year: year part of the date
    :return: True if the date is valid, False otherwise
    """

    days_in_month = [-1, 30, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # list of lengths of each month
    if is_leap_year(year):
        days_in_month[2] = 29  # adjust list for leap years
    if month not in range(1, 13):  # month not in 1..12
        return False
    if day not in range(1, days_in_month[month] + 1):  # day not in 1..n, where n is the number of days in that month
        return False
    return True


def get_input():
    """
    Get user input.

    Get user input - a date of birth.
    :return: a date structure consisting of day/month/year
    """

    # Get input
    input_day = int(input("Please input a day: "))
    input_month = int(input("Please input a month: "))
    input_year = int(input("Please input a year: "))

    # Check if it is valid, and continuously ask for more input as long as it is not valid
    while not is_valid(input_day, input_month, input_year):
        print("Invalid date entered. Please try again.")
        input_day = int(input("Please input a day: "))
        input_month = int(input("Please input a month: "))
        input_year = int(input("Please input a year: "))

    return date(input_year, input_month, input_day)


def get_days_since_new_year(some_date):
    """
    Compute the number of days that have passed since the beginning of the year a date is in
    :param some_date: date till which to start counting days
    :return: number of days from new year
    """
    days_in_month = [-1, 30, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # list of the lenghts of every month
    if is_leap_year(some_date.year):
        days_in_month[2] = 29  # adjust the list for leap years
    days_since_new_year = 0
    for month in range(1, some_date.month):
        days_since_new_year += days_in_month[month]  # add the days of each month in between
    days_since_new_year += some_date.day  # add the days passed in the current month

    return days_since_new_year


def get_days_till_new_year(some_date):
    """
    Compute the number of days to go till new year, starting from an arbitrary date.

    Compute the number of days to go till new year, starting from an arbitrary date.
    This function calls the get_days_since_new_year function,
    and subtracts the obtained value from 365 (or 366 in case of a leap year)
    :param some_date: date from which to start counting days
    :return: number of days till new year
    """

    days_till_my_date = get_days_since_new_year(some_date)
    if is_leap_year(some_date.year):
        return 366 - days_till_my_date
    else:
        return 365 - days_till_my_date


def get_diff_in_days(then, now):
    """
    Compute the number of days between two calendar dates.

    Compute the number of days between two calendar dates, taking into account leap years.
    First, get the number of days from 'then' to the end of that year.
    Second, get the total number of days in the full years between 'then' and 'now'
    Third, get the total number of days from the beginning of this year till 'now'
    :param then: first date
    :param now: last date
    :return: an integer representing the number of days between the two dates
    """

    if then.year == now.year:  # if the dates are both in the same year
        days_till_end_of_year = get_days_till_new_year(now)  # calculate the days in the interval [last_new_year, then)
        days_since_beginning_of_year = get_days_since_new_year(then)  # calculate the days in the interval [now, next_new_year)
        if is_leap_year(now.year):
            return 366 - days_since_beginning_of_year - days_till_end_of_year  # full year - [last_new_year, then) - [now, next_new_year)
        else:
            return 365 - days_since_beginning_of_year - days_till_end_of_year  # full year - [last_new_year, then) - [now, next_new_year)
    else:
        days_till_end_of_year = get_days_till_new_year(then)  # calculate the days from 'then' to the next new year
        days_since_beginning_of_year = get_days_since_new_year(now)  # calculate the days since the last new year
        days_in_between = 0  # the days in the whole years between 'then' and 'now'
        for year in range(then.year + 1, now.year):  # go through all the year strictly between the two dates
            if is_leap_year(year):
                days_in_between += 366  # add a whole leap year's worth of days
            else:
                days_in_between += 365  # add a whole year's worth of days

        return days_till_end_of_year + days_in_between + days_since_beginning_of_year  # sum them up


if __name__ == "__main__":
    current_date = date.today()  # current date
    print("Today:", current_date)  # print current date

    birth_date = get_input()  # date obtained from user input
    print(get_diff_in_days(birth_date, current_date))  # print result


