"""
Module that implements string parsing
"""
import Modules.Operator as Operator
import os


def check_int_validity(string_to_be_checked):
    '''
    Function that checks whether a string can be converted to an integer
    :param string_to_be_checked: The string that will be checked
    :return: True if the string can be converted, False otherwise
    '''
    try:
        int(string_to_be_checked)
        return True
    except ValueError:
        return False


def check_str_validity(string_to_be_checked):
    '''
    Function that checks if a string is valid.
    :param string_to_be_checked: The string that will be checked
    :return: True if the string cannot be converted to an int, False otherwise
    '''
    try:
        int(string_to_be_checked)
        return False
    except ValueError:
        return True


def check_operator_validity(string_to_be_checked):
    '''
    Function that checks if a string can be converted to an operator
    :param string_to_be_checked: The string that will be checked
    :return: True if the string can be converted, False otherwise
    '''
    try:
        Operator.Operator(string_to_be_checked)
        return True
    except ValueError:
        return False


def parameters_are_valid(parameters, rule):
    '''
    Function that checks if the user-inputted parameters follow a certain rule set
    :param parameters: The parameters to check
    :param rule: The rules to check against
    :return: True if the parameters are valid, False otherwise
    '''

    checking_functions = {
        int: check_int_validity,
        str: check_str_validity,
        Operator.Operator: check_operator_validity
    }

    if len(parameters) != len(rule):
        return False

    for index, parameter in enumerate(parameters):
        if type(rule[index]) == str:
            if not rule[index] == parameter:
                return False
        elif not checking_functions[rule[index]](parameter):  # Invalid parameter type
            return False
    return True  # All parameters have a valid name and type


def choose(choices=None, special_message=None):
    """
    Have the user make a choice, and and don't stop until he gives a valid choice
    :param choices: The valid choices the user can make
    :return: The choice made by the user
    """
    while True:
        # os.system('clear')
        print(special_message)
        for index, value in enumerate(choices):
            print("{}. {}".format(str(index + 1), str(value)))

        user_input = input("--> ")
        if check_int_validity(user_input) is True:
            choice = int(user_input) - 1
            if choice in range(len(choices)):
                os.system('clear')
                return choices[choice]


def get_input_of_type(target_type, special_message=None):
    """
    Get a input of a certain type from the user
    :param target_type: The type that the input should be in
    :return: The input casted to the given type
    """

    type_checker = {
        int: check_int_validity,
        Operator.Operator: check_operator_validity,
        str: check_str_validity
    }

    while True:
        print(special_message)
        user_input = input("--> ")
        if type_checker[target_type](user_input) is True:
            return target_type(user_input)