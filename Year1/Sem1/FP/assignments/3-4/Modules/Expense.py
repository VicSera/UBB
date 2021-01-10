"""
Domain module for expenses
"""


def create(day, amount, category):
    expense = [day, amount, category]
    return expense


def get_day(expense):
    return expense[0]


def get_amount(expense):
    return expense[1]


def get_type(expense):
    return expense[2]


def initialize_list():
    """
    Function that returns a list with sample values
    :return: The newly created list with sample values
    """
    new_list = []

    new_list.append(create(1, 50, 'food'))
    new_list.append(create(2, 20, 'cleaning'))
    new_list.append(create(3, 27, 'taxi'))
    new_list.append(create(4, 34, 'flight'))
    new_list.append(create(5, 15, 'starbucks'))

    return new_list