"""
Module that implements the underlying functions called by the UI
"""
import Modules.Parser as Parser
import Modules.Expense as Expense
import Modules.Operator as Operator

import copy
from datetime import datetime


def add(expenses, parameters):
    '''
    Function that handles adding expenses to the expenses list, checking for the day of the month automatically
    :param expenses: The list to modify
    :param parameters: The list of parameters the user inputted for the 'add' command
    The parameters are in the following format:
    add <sum> <category>
    '''

    # Rule for checking parameter validity
    rule = [int, str]  # Parameters have to be an int and a str in this exact order

    if not Parser.parameters_are_valid(parameters, rule):
        print("Invalid parameters for adding function.")
        print("Usage: add <sum> <category>")
        return

    expense = Expense.create(int(datetime.now().day), int(parameters[0]), parameters[1])

    expenses.append(expense)


def insert(expenses, parameters):
    '''
    Function that inserts a new expense into the list, but this time all three details of an expense have to be specified
    :param expenses: The list of expenses
    :param parameters: The list of parameters
    '''

    # Rule for checking parameter validity
    rule = [int, int, str]  # Parameters have to be in day/amount/category format

    if not Parser.parameters_are_valid(parameters, rule) or int(parameters[0]) not in range(1, 31):
        print("Invalid parameters for inserting function.")
        print("Usage: insert <day> <sum> <category>")
        return

    expense = Expense.create(int(parameters[0]), int(parameters[1]), parameters[2])

    expenses.append(expense)


def remove(expenses, parameters):
    '''
    Function that handles the remove feature in the menu
    Possible parameter structure:
    remove <day>
    remove <start day> to <end day>
    remove <category>
    :param expenses: Expense list to change
    :param parameters: Parameters for the remove feature
    :return:
    '''

    rules = [
        [int],
        [int, 'to', int],
        [str]
    ]

    rule_used = -1

    for rule_index in range(len(rules)):  # Figure out which of the three rules the command follows
        if Parser.parameters_are_valid(parameters, rules[rule_index]):  # Found the corresponding set of rules
            rule_used = rule_index
            break

    if rule_used == -1:  # No rule matched up with the given parameters
        print("Usage:\n"
              "remove <day>\n"
              "remove <start day> to <end day>\n"
              "remove <category>")
    if rule_used == 0:  # First case
        for expense in expenses[:]:
            if Expense.get_day(expense) == int(parameters[0]):
                expenses.remove(expense)
    elif rule_used == 1:  # Second case
        for expense in expenses[:]:
            if int(parameters[0]) <= Expense.get_day(expense) <= int(parameters[2]):
                expenses.remove(expense)
    elif rule_used == 2:  # Third case
        for expense in expenses[:]:
            if Expense.get_type(expense) == parameters[0]:
                expenses.remove(expense)


def print_row(to_print=None):
    """
    Function that prints a row in the table of expenses
    :param expense: The expense that should be represented in the row
    """
    if to_print is None:
        row = '+' + '-' * (3 + 10 + 15 + 8) + '+'
        print(row)
    elif type(to_print) is str and to_print is 'Header':
        paddings = [3, 10, 15]
        categories = ['Day', 'Amount', 'Category']

        row = '| '
        for element in range(len(categories)):
            value = categories[element]
            padding = paddings[element] - len(value)
            row += value + (' ' * padding) + ' | '
        print(row)
    elif type(to_print) is list:
        paddings = [3, 10, 15]

        row = '| '
        for attribute in range(len(to_print)):
            value = str(to_print[attribute])
            padding = paddings[attribute] - len(value)
            row += value + (' ' * padding) + ' | '
        print(row)


def list_elements(expenses, parameters):
    '''
    Function that handles listing expenses
    Possible parameters:
    list
    list <category>
    list <category> [ < | = | > ] <value>
    :param expenses: Expense list to be listed out
    :param parameters: Parameters used by the listing feature
    '''

    rules = [
        [],
        [str],
        [str, Operator.Operator, int]
    ]

    rule_used = -1

    for rule_index, rule in enumerate(rules):
        if Parser.parameters_are_valid(parameters, rule):
            rule_used = rule_index
            break

    if rule_used == -1:
        print('Usage:\n',
              'list\n',
              'list <category>\n'
              'list <category> [ < | = | > ] <value>')
    else:
        print_row(to_print=None)
        print_row(to_print='Header')
        print_row(to_print=None)
        if rule_used == 0:  # First case
            for expense in expenses:
                print_row(to_print=expense)
        elif rule_used == 1:  # Second case
            for expense in expenses:
                if Expense.get_type(expense) == parameters[0]:
                    print_row(to_print=expense)
        elif rule_used == 2:  # Third case
            for expense in expenses:
                type_match = Expense.get_type(expense) == parameters[0]
                operator_rule_followed = Operator.operator_map[parameters[1]](Expense.get_amount(expense), int(parameters[2]))
                if operator_rule_followed and type_match:
                    print_row(to_print=expense)
        print_row(to_print=None)


def get_all_categories(expenses):
    """
    Function that returns a list of all unique categories found in the expense list
    :param expenses: The list to parse
    :return: A list containing the unique categories
    """
    unique_list = []
    for expense in expenses:
        if Expense.get_type(expense) not in unique_list:
            unique_list.append(Expense.get_type(expense))

    return unique_list


def get_all_days(expenses):
    """
    Get a list containing all the days of the months which have entries in the expense list
    :param expenses: The expense list to look through
    :return: The described list
    """

    days = []

    for expense in expenses:
        day = Expense.get_day(expense)
        if day not in days:
            days.append(day)

    return days


def get_all_expenses(expenses, day=None, amount=None, category=None):
    """
    Get a list of all expenses that have a fixed day, amount or category
    :param day: The day restriction
    :param amount: The amount restriction
    :param category: The category restriction
    :return: The resulting list
    """

    expenses_to_keep = []

    if day is not None:
        for expense in expenses:
            if Expense.get_day(expense) == day:
                expenses_to_keep.append(expense)
    elif amount is not None:
        for expense in expenses:
            if Expense.get_amount(expense) == amount:
                expenses_to_keep.append(expense)
    elif category is not None:
        for expense in expenses:
            if Expense.get_type(expense) == category:
                expenses_to_keep.append(expense)

    return expenses_to_keep


def sum_category(expenses, parameters):
    """
    Function that handles the 'sum' functionality
    Usage: sum <category>
    :param expenses: The expense list
    :param parameters: The list of parameters used for summing
    :return: The sum corresponding to the elements described by the parameters
    """

    rule = [str]
    usage = "sum <category>"

    if Parser.parameters_are_valid(parameters, rule):
        target_category = parameters[0]
        if target_category not in get_all_categories(expenses):
            print("Category {} not found.".format(target_category))
            return

        total = 0
        for expense in expenses:
            if Expense.get_type(expense) == target_category:
                total += Expense.get_amount(expense)
        print(total)
    else:
        print(usage)


def max_per_day(expenses, parameters):
    """
    Function that returns a list of expenses that have the day equal to a given day
    :param expenses: The list to look through
    :param day: The target day
    :return: The list of corresponding days
    """

    usage = "max <day>"

    rule = [int]

    if Parser.parameters_are_valid(parameters, rule) is False:
        print(usage)
        return

    day = int(parameters[0])

    if day not in range(1, 31):
        print(usage)
        return

    max_expense = 0

    for expense in expenses:
        if Expense.get_day(expense) == day:
            amount = Expense.get_amount(expense)
            if amount > max_expense:
                max_expense = amount

    print(max_expense)


def max_day(expenses, parameters):
    """
    Function that gets the day with the biggest expenses
    :param expenses:
    :param parameters:
    :return:
    """

    rule = []

    if Parser.parameters_are_valid(parameters, rule) is False:
        print("Usage: maxday")
        return

    max_day = -1
    sum_exp_per_day = {}

    for expense in expenses:
        day = Expense.get_day(expense)
        amount = Expense.get_amount(expense)
        if day not in sum_exp_per_day.keys():
            sum_exp_per_day[day] = amount
            if max_day is -1:
                max_day = day
            if sum_exp_per_day[max_day] < amount:
                max_day = day
        else:
            sum_exp_per_day[day] += amount
            if sum_exp_per_day[max_day] < sum_exp_per_day[day]:
                max_day = day

    print(max_day)


def sort_by(expenses, parameters):
    """
    Sort the expenses in a given day in ascending order
    :param expenses: The expense list to look through
    :param parameters: The parameters for sorting
    """

    usage = "sort <day>\nsort <category>"

    rules = [[int], [str]]
    if Parser.parameters_are_valid(parameters, rules[0]) is True:  # sort <day>
        all_day_entries = get_all_days(expenses)
        target_day = int(parameters[0])

        if target_day not in all_day_entries:
            print("No entry for day {}". format(parameters[0]))
            return

        expenses_in_target_day = get_all_expenses(expenses, day=target_day)
        criterion = lambda e: Expense.get_amount(e)
        expenses_in_target_day.sort(key=criterion)
        list_elements(expenses_in_target_day, [])
    elif Parser.parameters_are_valid(parameters, rules[1]) is True:  # sort <category>
        all_category_entries = get_all_categories(expenses)
        target_category = parameters[0]

        if target_category not in all_category_entries:
            print("No entry for category {}".format(target_category))
            return

        expenses_in_target_category = get_all_expenses(expenses, category=target_category)
        criterion = lambda e: Expense.get_amount(e)
        expenses_in_target_category.sort(key=criterion)
        list_elements(expenses_in_target_category, [])
    else:  # invalid arguments
        print(usage)
        return


def filter(expenses, parameters):
    """
    Function that handles the 'filter' functionality
    :param expenses: The expense list to filter
    :param parameters: The parameters for filtering
    """

    rules = [
        [str],  # filter <category>
        [str, Operator.Operator, int]  # filter <category>  < / > / =  <value>
    ]

    all_categories = get_all_categories(expenses)

    if Parser.parameters_are_valid(parameters, rules[0]) is True:
        category_to_keep = parameters[0]

        for category in all_categories:
            if category != category_to_keep:
                remove(expenses, [category])
    elif Parser.parameters_are_valid(parameters, rules[1]) is True:
        category_to_keep = parameters[0]
        operator = parameters[1]
        value = int(parameters[2])

        for category in all_categories:
            if category != category_to_keep:
                remove(expenses, [category])
        for expense in expenses[:]:
            if Operator.operator_map[operator](Expense.get_amount(expense), value) is False:
                expenses.remove(expense)


def undo(expenses_history):
    """
    Handle the undoing functionality
    :param expenses: The current expenses
    :param expenses_history: The history of expenses
    """
    if len(expenses_history) is 1:
        print("Cannot undo any further")
        return copy.deepcopy(expenses_history[0])

    expenses_history.pop()
    return copy.deepcopy(expenses_history[-1])