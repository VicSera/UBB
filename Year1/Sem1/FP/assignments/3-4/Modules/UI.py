"""
Module that implements the UI functions
"""

import Modules.Parser as Parser
import Modules.Expense as Expense
import Modules.Functions as Functions
import os
import copy

from Modules.Tests import test_all_functions


def menu_add(expenses):
    """
    Launch the menu that corresponds to the 'add' command
    :param expenses: The list of expenses to add elements to
    """
    add = Functions.add  # Reference the same function used in the command-based menu
    print("You have selected the 'add' option.")

    amount = Parser.get_input_of_type(int, "Please give an amount")
    category = Parser.get_input_of_type(str, "Please give a category")

    add(expenses, [amount, category])


def menu_insert(expenses):
    """
    Launch the menu that corresponds to the 'insert' command
    :param expenses: The list of expenses to insert new expenses into
    """
    add = Functions.insert  # Reference the same function used in the command-based menu
    print("You have selected the 'add' option.")

    while True:
        day = Parser.get_input_of_type(int, "Please give a valid day (1-30)")
        if day in range(1, 31):
            break
    amount = Parser.get_input_of_type(int, "Please give an amount")
    category = Parser.get_input_of_type(str, "Please give a category")

    add(expenses, [day, amount, category])



def menu_list(expenses):
    """
    Launch the menu that corresponds to the 'list' command
    :param expenses: The list of expenses to print out
    """
    printer = Functions.list_elements

    categories = ['All categories'] + Functions.get_all_categories(expenses)
    category = Parser.choose(categories, "Please choose a category:")

    if category is 'All categories':
        printer(expenses, [])
        return

    constraining_options = ['No constraints', 'Place a constraint']
    constraint_choice = Parser.choose(constraining_options, "Please choose a constraint:")

    if constraint_choice is 'No constraints':
        printer(expenses, [category])
        return

    operators = ['<', '>', '=']
    operator = Parser.choose(operators, "Please choose an operator: ")
    comparison_element = Parser.get_input_of_type(int, "Please choose a number to compare to: ")
    printer(expenses, [category, operator, comparison_element])


def menu_sort(expenses):
    """
    Launch the menu that corresponds to the 'sort' command
    :param expenses: The list of expenses to sort
    """

    options = ['Day', 'Category']
    criterion = Parser.choose(options, "Sort by:")

    if criterion is 'Day':
        valid_days = Functions.get_all_days(expenses)  # get all the unique entries for days
        day = Parser.get_input_of_type(int, "Please choose a day:")

        if day not in valid_days:
            print("There are no entries for day {}".format(str(day)))
            return

        Functions.sort_by(expenses, [day])
    elif criterion is 'Category':
        valid_categories = Functions.get_all_categories(expenses)  # get all the unique entries for categories
        category = Parser.choose(valid_categories, "Please pick a category:")

        Functions.sort_by(expenses, [category])


def menu_filter(expenses):
    """
    Launch the menu that corresponds to the 'filter' command
    :param expenses: The list of expenses to filter
    """

    categories = Functions.get_all_categories(expenses)
    category = Parser.choose(categories, "Please choose a category:")

    restrictions = [
        'No restrictions',
        'Add restriction'
    ]
    restriction = Parser.choose(restrictions, "Please choose any further restriction:")

    if restriction is 'No restrictions':
        Functions.filter(expenses, [category])
    elif restriction is 'Add restriction':
        operators = ['<', '>', '=']
        operator = Parser.choose(operators, "Please pick an operator:")
        value = Parser.get_input_of_type(int, "Please pick a value to compare to:")

        Functions.filter(expenses, [category, operator, value])


def menu_sum(expenses):
    """
    Launch the menu that corresponds to the 'sum' command
    :param expenses: The list of expenses to sum
    """

    categories = Functions.get_all_categories(expenses)
    category = Parser.choose(categories, "Please choose a category:")

    Functions.sum_category(expenses, [category])


def menu_max(expenses):
    """
    Launch the menu that corresponds to the 'maxday' command
    :param expenses: The list of expenses to look through
    """

    options = [
        "Get the day with the most expenses",
        "Get the maximum expense in a day"
    ]

    user_choice = Parser.choose(options, "Please choose what max you want:")

    if user_choice is options[0]:
        Functions.max_day(expenses, [])
    elif user_choice is options[1]:
        day = Parser.get_input_of_type(int, "Please pick a day:")
        Functions.max_per_day(expenses, [day])


def menu_undo():
    """
    Empty function, as the undo-ing is handled inside the main interface
    :return:
    """
    pass


def menu_exit(*empty_args):
    exit(0)


def menu_interface():
    """
    The main menu-based user interface
    """
    os.system('clear')

    expenses = Expense.initialize_list()
    expenses_history = [copy.deepcopy(expenses)]

    menu_options = [
        "Add an element to the list",
        "Insert an element to the list",
        "List elements",
        "Sort elements",
        "Filter out certain elements",
        "Get maximum",
        "Sum elements",
        "Undo",
        "Exit"
    ]

    functions = {
        menu_options[0]: menu_add,
        menu_options[1]: menu_insert,
        menu_options[2]: menu_list,
        menu_options[3]: menu_sort,
        menu_options[4]: menu_filter,
        menu_options[5]: menu_max,
        menu_options[6]: menu_sum,
        menu_options[7]: None,
        menu_options[8]: menu_exit
    }

    while True:
        function_to_call = functions[Parser.choose(menu_options, "Please choose one of the following options:")]
        os.system('clear')

        if function_to_call is None:
            expenses = Functions.undo(expenses_history)
            continue

        function_to_call(expenses)

        if expenses != expenses_history[-1]:
            expenses_history.append(copy.deepcopy(expenses))


def command_interface():
    """
    The main user interface.
    """
    os.system('clear')
    expenses = Expense.initialize_list()  # Initial list with sample values
    expenses_history = [copy.deepcopy(expenses)]

    options = {
        'add': Functions.add,
        'insert': Functions.insert,
        'remove': Functions.remove,
        'list': Functions.list_elements,
        'sum': Functions.sum_category,
        'max': Functions.max_per_day,
        'maxday': Functions.max_day,
        'sort': Functions.sort_by,
        'filter': Functions.filter,
        'undo': None,
        'exit': menu_exit
    }

    while True:
        print("\n         MAIN MENU          \n\n"
              "   Please input a command   \n\n")
        user_input = input("--> ")
        os.system('clear')
        operands = user_input.split()
        if operands[0] not in options.keys():
            print("Invalid command '" + str(operands[0]) + "'")
        elif operands[0] == 'undo':
            expenses = Functions.undo(expenses_history)  # treat undo separately because of the history change
        else:
            options[operands[0]](expenses, operands[1:])

            if expenses != expenses_history[-1]:  # only append if there was a change
                expenses_history.append(copy.deepcopy(expenses))  # append a copy of current expenses to the history


def get_menu_type():
    """
    Function that gets called first, to decide what type of menu the user desires
    :return: 1 or 2, corresponding to a command-based interface, or a menu-based one respectively
    """
    print("Please choose an interface type.\n"
          "1. Command-based\n"
          "2. Menu-based")
    while True:
        choice = Parser.get_input_of_type(int, "Choice: ")
        if choice in [1, 2]:
            return choice


def start_application():
    """
    Function that activates the appropriate interface, based on the user's decision
    :param choice: The user's choice
    """

    test_all_functions()

    os.system('clear')
    choice = get_menu_type()

    interfaces = {
        1: command_interface,
        2: menu_interface
    }

    interfaces[choice]()  # Call the corresponding interface function
