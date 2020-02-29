"""
Assignment 1
Problem 5

Generate the largest prime number smaller than a given natural number n. If such a number
does not exist, a message should be displayed.
"""

from math import sqrt


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


def is_prime(number):
    """
    Check if a given integer is a prime number.

    Check if a given integer is a prime number, by iterating through all numbers up to its square root, and checking if they are divisors.

    :param number:
    :return Boolean value:
    """
    if number < 2:
        return False
    for divisor in range(2, int(sqrt(number) + 1)):
        if number % divisor == 0:
            return False
    return True


def get_first_prime_below(number):
    """
    Obtain the biggest prime number smaller than the given number.

    Obtain the biggest prime number smaller than the given number, by iterating through all the number below it, and returning the first prime number, or -1 if none are found.

    :param number:
    :return biggest prime number smaller than the given number or -1 if none are found:
    """
    for prime_trial in range(number - 1, 1, -1):
        if is_prime(prime_trial):
            return prime_trial
    return -1


def get_input():
    """
    Obtain input from the user.

    Obtain input from the user. If the input cannot be converted to an integer, request another input, until the value given is correct.
    The first valid input is converted to an integer and returned.

    :return: an integer corresponding to the first valid input from the user
    """
    print("Hello user.",
          "This program will display the largest prime number smaller than the number you are about to give.")

    user_input = input("Please input a number: ")
    while not is_number(user_input):
        print("Wrong input type.")
        user_input = input("Please input a number: ")

    return int(user_input)


if __name__ == '__main__':
    given_number = get_input()  # get input

    result = get_first_prime_below(given_number)  # find result
    if result != -1:
        print("The largest prime number smaller than ", given_number, " is ", result)
    else:
        print("No primes found below " + str(given_number))