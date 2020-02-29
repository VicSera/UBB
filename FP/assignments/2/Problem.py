'''
Implement a menu-driven console application that provides the following functionalities:
1. Read a list of complex numbers (in z = a + bi form) from the console.
2. Display the entire list of numbers on the console.
3. Display on the console the longest sequence that observes a given property. Each student will
receive 2 of the properties from the list provided below.
4. Exit the application.
The source code will include:
a. Specifications for the functions related to point 3 above.
b. 10 suitable complex numbers already available at program startup.
Sequence Properties
The sequence (consists of):
1. Numbers with a strictly increasing real part.
2. Contains at most 3 distinct values.
3. Numbers having the same modulus.
4. Numbers having increasing modulus.
5. Real numbers.
6. Distinct numbers.
7. The difference between the modulus of consecutive numbers is a prime number.
8. The modulus of all elements is in the [0, 10] range.
9. Consecutive number pairs have equal sum. (e.g. 1+3i, 1-i, 1+3i, 1-i)
10. Sum of its elements is 10+10i
11. Real part is in the form of a mountain (first the values increase, then they decrease). (e.g. 1-i, 2+6i,
4-67i, 90+3i, 80-7i, 76+i, 43-12i, 3)
12. Both real and imaginary parts can be written using the same base 10 digits (e.g. 1+3i, 31i, 33+i, 111,
11-313i)
MY ASSIGNMENTS: 1 AND 2
'''


class InvalidFunction (Exception):
    pass


def get_real(complex_number):
    '''
    Getter for the real part of a complex number
    :param complex_number: the source complex number
    :return: Re(complex_number), or the real part of the complex number
    '''
    return complex_number[0]


def get_imaginary(complex_number):
    '''
    Getter for the imaginary part of a complex number
    :param complex_number: the source complex number
    :return: Im(complex_number), or the imaginary part of the complex number
    '''
    return complex_number[1]


def set_real(complex_number, real):
    '''
    Setter for the real part of a complex number
    :param complex_number: the target complex number
    :param real: the target value to set
    '''
    complex_number[0] = real


def set_imaginary(complex_number, imaginary):
    '''
    Setter for the imaginary part of a complex number
    :param complex_number: the target complex number
    :param imaginary: the target value to set
    '''
    complex_number[1] = imaginary


def is_number(number):
    '''
    Check if a given value can be converted to a float or not.
    Check if a given value can be converted to a float or not. Return True if so, otherwise False.
    :param number: The value to be checked
    :return: True if the number can be converted to a float, False otherwise
    '''
    try:
        float(number)  # if it can be converted to a float
        return True  # return true
    except ValueError:  # otherwise, if the conversion throws an error
        return False  # return false


def turn_to_complex_number(complex_number_string):
    '''
    Check if a string can be converted to a complex number.
    Check if a string can be converted to a complex number.
    If so, return the real and imaginary parts, otherwise, raise an exception
    The string has to have the format (#1) +/- (#2)i
    :param complex_number_string: the string to be converted
    :return: a pair consisting of a real and an imaginary part
    '''

    separators = '+-'  # possible separators that are to be recognized

    # initialisations for the used values
    starting_point = 0
    real_part = ''
    imaginary_part = ''
    found_separator = False  # to know which value to change (real if !found, imaginary if found)
    separator = ''  # to know if the imaginary part is negative or not
    real_is_negative = False  # keep in mind the sign of the real part

    if complex_number_string[0] == '-':
        real_is_negative = True  # keep in mind that the real part is negative
        starting_point = 1  # skip the '-' when parsing the string

    for character in complex_number_string[starting_point:]:  # parse each character, starting from 'starting_point'
        if character in separators:  # if found a separator
            if found_separator:  # if the string already contains a reparator
                raise ValueError  # then the string is invalid
            separator = character
            found_separator = True  # mark the separator as found
        elif is_number(character) or character == '.':  # append the current number/dot to the corresponding value
            if not found_separator:  # if !found separator, we're on the left side
                real_part += character
            else:  # otherwise, we're on the right side
                imaginary_part += character
        elif character == 'i':  # i marks the end of a number
            real_sign = 1  # suppose real part is positive
            imag_sign = 1  # suppose imag part is positive
            if real_is_negative:
                real_sign = -1  # if the first character was a '-', change real sign
            if separator == '-':  # if the separator was a '-', change imag sign
                imag_sign = -1
            return real_sign * float(real_part), imag_sign * float(imaginary_part)  # return the pair with the corresponding signs

    raise ValueError


def test_turn_to_complex_number():
    """
    Function that tests the functionality of the turn_to_complex_number function
    """
    test_string = "1.5-2.7i"
    try:
        number = turn_to_complex_number(test_string)  # Compute the value of the string
        if get_real(number) != 1.5 or get_imaginary(number) != -2.7:  # Compare the result to the expected result
            raise InvalidFunction  # If values mismatch, raise an InvalidFunction exception
    except ValueError:  # If the function doesn't recognise the format, even though it is correct
        raise InvalidFunction  # Raise an InvalidFunction exception


def ui_add_numbers(number_list):
    '''
    Add numbers to the list.
    Add numbers to the list, but check each input to make sure
    :param number_list:
    :return:
    '''
    print("You have selected the option to add values to the list.",
          "Press enter after each number, or just x to stop adding numbers")
    while True:
        user_input = input()
        if user_input == 'x':
            print("Going back to the menu")
            break
        else:
            try:
                complex_num = [0., 0.]
                real, imaginary = turn_to_complex_number(user_input)
                set_real(complex_num, real)
                set_imaginary(complex_num, imaginary)
                number_list.append(complex_num)
            except:
                print("Invalid complex number format")


def ui_display_numbers(number_list):
    '''
    Print a list of format [[r1, i1], [r2, i2], ...]
    :param number_list: the list of numbers to display
    '''

    for complex_number in number_list:
        if complex_number[1] < 0:
            print(complex_number[0], "-", -complex_number[1], "i")
        else:
            print(complex_number[0], "+", complex_number[1], "i")


def seq_increasing_real_part(number_list):
    '''
    Generate the largest sequence that contains numbers with strictly increasing real parts
    :param number_list: the values to use
    :return: a slice of number_list that corresponds to the largest sequence that follows that rule
    '''
    max_index_begin, max_index_end = 0, 0  # store the bounds of the best sequence
    current_index_begin = 0  # the beginning of the current sequence

    for index in range(1, len(number_list)):  # parse all elements but the first one
        if get_real(number_list[index]) > get_real(number_list[index - 1]):  # if the last element had a smaller real part
            sequence_length = index - current_index_begin
            if sequence_length > max_index_end - max_index_begin:  # check if the current sequence is bigger than the previous maximum
                max_index_begin = current_index_begin  # update max_indexes accordingly
                max_index_end = index
        else:  # the start of a new sequence
            current_index_begin = index  # new sequence starts from the first element that broke the order rule

    return number_list[max_index_begin:max_index_end + 1]  # return the maximal slice


def test_seq_increasing_real_part():
    """
    Function that tests the functionality of the seq_increasing_real_part function
    """
    number_list = [  # list for testing the function
        [1.2, -5.0],
        [3.2, 5.1],
        [-5.5, 10.2],
        [-17.2, -21.2],
        [-72.1, 22.0],  # Beginning of the expected sequence
        [11.4, -7.7],
        [17.3, 7.6],
        [21.2, 2.124],  # End of the expected sequence
        [1.3, -12.5],
        [-8.2, 4.121],
    ]

    sequence = seq_increasing_real_part(number_list)  # Call the function
    if sequence != number_list[4:8]:  # Compare the result to the expected result
        raise InvalidFunction  # Raise an InvalidFunction exception in case of a mismatch


def num_distinct_values(list):
    '''
    Count how many distinct values there are in a list
    :param list: the list to parse
    :return: number of distinct values
    '''

    found_values = []  # empty list initially
    for value in list:
        if value not in found_values:  # only add values that have not yet been found
            found_values.append(value)

    return len(found_values)  # final length should be the number of distinct values


def test_num_distinct_values():
    """
    Functions that test the functionality of num_distinct_values
    """

    generic_list = [1, 1, 2, 3, 1, 4, 5, 5, 7, 7, 7, 7]
    expected_result = 6

    if num_distinct_values(generic_list) != expected_result:
        raise InvalidFunction


def seq_at_most_3_diff_values(number_list):
    '''
    Generate the largest sequence that contains no more than 3 unique values
    :param number_list: the values to use
    :return: a slice of number_list that corresponds to the longest sequence that follows that rule
    '''
    max_index_begin, max_index_end = 0, 0  # these store the bounds of the best sequence
    current_index_begin = 0  # current sequence beginning

    for index in range(1, len(number_list)):
        current_sequence = number_list[current_index_begin:index]  # the slice corresponding to the current sequence
        distinct_values = num_distinct_values(current_sequence)  # count the number of unique elements already in the sequence
        if distinct_values < 3 or (distinct_values == 3 and number_list[index] in current_sequence):  # if the current sequence has 2 or fewer unique values OR it already has 3, but the current one is already in the sequence
            if index - current_index_begin > max_index_end - max_index_begin:  # if the new sequence size is bigger than the previous maximum
                max_index_begin = current_index_begin  # update the beginning and end values
                max_index_end = index
        else:  # in this case, we need to start building another sequence
            last_starting_value = number_list[current_index_begin]  # this variable holds the value of the previous first element in the sequence
            while number_list[current_index_begin] == last_starting_value:  # while loop that takes care of consecutive elements that need to be skipped when changing starting point
                current_index_begin += 1  # increment starting index

    return number_list[max_index_begin:max_index_end + 1]  # return the maximal slice


def test_seq_at_most_3_diff_values():
    """
    Function that tests the functionality of the seq_at_most_3_diff_values function
    """
    number_list = [  # list for testing the function
        [1, 1],
        [1, 1],
        [2, 1],  # Beginning of the expected sequence
        [3, 1],
        [3, 1],
        [4, 4],
        [4, 4],
        [4, 4],  # End of the expected sequence
        [5, 5]
    ]

    expected_sequence = number_list[2:8]
    if seq_at_most_3_diff_values(number_list) != expected_sequence:
        raise InvalidFunction


def sequence_menu(number_list):
    '''
    The menu corresponding to the 3rd option in the main menu
    From here, the user can select one out of 2 rules for generating a sequence
    :param number_list: the number list to use
    '''
    options = {
        1 : seq_increasing_real_part,
        2 : seq_at_most_3_diff_values
    }

    while True:
        option = input("Choose:\n"
                       "1. Longest sequence with strictly increasing real part\n"
                       "2. Longest sequence with max 3 distinct values\n"
                       "x. Exit\n"
                       "Option: ")
        if option == 'x':
            break
        sequence = options[int(option)](number_list)
        print(sequence)


def launch_menu():
    number_list = [  # just some random initial values
        [1.0, -5.0],
        [-3.2, -2.1],
        [6.5, 10.6],
        [-12.2, 21.2],
        [7.8, -22.0],
        [18.1, -7.7],
        [6.3, 5.6],
        [-2.6, 2.1],
        [1.3, -12.2],
        [-8.2, -4.2],
    ]
    options = {  # the main menu options
        1 : ui_add_numbers,
        2 : ui_display_numbers,
        3 : sequence_menu
    }

    while True:
        option = input("Please choose:\n"
                       "1. Add numbers\n"
                       "2. Display numbers\n"
                       "3. Sequences\n"
                       "x. Exit\n"
                       "Choice: ")
        if option == 'x':
            break
        options[int(option)](number_list)  # call the function corresponding to the user option


def test_all_functions():
    """
    Function that calls all the test functions
    :return:
    """
    try:
        test_turn_to_complex_number()
        test_seq_increasing_real_part()
        test_num_distinct_values()
        test_seq_at_most_3_diff_values()
    except InvalidFunction:
        raise Exception("Functions are not valid")


if __name__ == '__main__':
    test_all_functions()
    launch_menu()