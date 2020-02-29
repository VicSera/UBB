"""
Module that implements the test functions
"""
from Modules.Parser import *
from Modules.Operator import *


def test_check_int_validity_true():
    """
    Function that tests the validity of check_int_validity
    """
    int_true = "123"

    assert(check_int_validity(int_true) is True)


def test_check_int_validity_false():
    """
    Function that tests the validity of check_int_validity
    """
    int_false = "Hello"

    assert(check_int_validity(int_false) is False)



def test_check_str_validity_true():
    """
    Function that tests the functionality of check_str_validity
    """
    str_true = "Hello"

    assert(check_str_validity(str_true) is True)


def test_check_str_validity_false():
    """
    Function that tests the functionality of check_str_validity
    """
    str_false = "123"

    assert(check_str_validity(str_false) is False)



def test_check_operator_validity_true():
    """
    Function that checks the functionality of check_operator_validity
    """
    operator_true = '<'

    assert(check_operator_validity(operator_true) is True)


def test_check_operator_validity_false():
    """
    Function that checks the functionality of check_operator_validity
    """
    operator_false = '!s>'

    assert(check_operator_validity(operator_false) is False)


def test_parameters_are_valid_true():
    """
    Function that tests the functionality of parameters_are_valid
    :return:
    """
    parameters = [1, '<', 'hello']
    rule_true = [int, Operator, str]

    assert(parameters_are_valid(parameters, rule_true) is True)


def test_parameters_are_valid_false():
    """
    Function that tests the functionality of parameters_are_valid
    :return:
    """
    parameters = [1, '<', 'hello']
    rule_false = [str, Operator, int]

    assert(parameters_are_valid(parameters, rule_false) is False)



def test_all_functions():
    """
    Call all the test functions
    """
    test_parameters_are_valid_true()
    test_parameters_are_valid_false()
    test_check_int_validity_true()
    test_check_int_validity_false()
    test_check_operator_validity_true()
    test_check_operator_validity_false()
    test_check_str_validity_true()
    test_check_str_validity_false()