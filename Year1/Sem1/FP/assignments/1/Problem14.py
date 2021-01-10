"""
Assignment 1
Problem 14

Sequence: 1 2 3 2 2 5 2 2 3 3 3 7 2 2 3 3 3 2 2 5 5 5 5 5
"""

from math import sqrt


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(sqrt(number)) + 1):
        if number % divisor == 0:
            return False
    return True


def get_nth_element(n):
    flag = False
    current_index = 1
    if n == 1:
        return 1
    current_num_to_factorize = 1
    while True:
        current_num_to_factorize += 1
        if is_prime(current_num_to_factorize):
            current_index += 1
            if current_index == n:
                return current_num_to_factorize
        else:
            current_divisor = 2
            copy_to_factorize = current_num_to_factorize
            while copy_to_factorize > 1:
                while copy_to_factorize % current_divisor == 0:
                    copy_to_factorize //= current_divisor
                    flag = True
                if flag:
                    current_index += current_divisor
                flag = False
                if current_index >= n:
                    return current_divisor
                current_divisor += 1


if __name__ == '__main__':
    input_number = int(input("What is the position you desire? "))
    print(get_nth_element(input_number))