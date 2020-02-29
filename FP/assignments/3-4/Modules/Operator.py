"""
Module that implements the operator functionality
"""


operator_map = {
        '>': lambda x, y: x > y,
        '<': lambda x, y: x < y,
        '=': lambda x, y: x == y
    }


def Operator(string_to_check):
    """
    Check if the given string is an operator or not
    :param string_to_check: The string to be checked
    """
    if string_to_check in ['>', '<', '=']:
        pass
    else:
        raise ValueError