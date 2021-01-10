from Modules.Services import Services
import os

class UI:
    def __init__(self):
        self.__services = Services()

    def launch(self):
        """
        Launch the UI
        """
        UI.__clear_screen()
        options = {
            'Add an expense': self.__call_add_expense,
            'Show the list': self.__list_expenses,
            'Filter out expenses': self.__call_filter_expenses,
            'Undo': self.__services.undo
        }

        while True:
            function_to_call = UI.__choose(options=options)
            UI.__clear_screen()
            try:
                function_to_call()
            except Exception as exception:
                print(exception)


    def __list_expenses(self):
        expenses, day_length, amount_length, category_length = self.__services.get_extended_expenses()

        table_width = day_length + amount_length + category_length + 10

        print('+' + '-' * (table_width - 2) + '+')

        day_header = 'Day'.ljust(day_length)
        amount_header = 'Amount'.ljust(amount_length)
        category_header = 'Category'.ljust(category_length)
        print("| {} | {} | {} |".format(day_header, amount_header, category_header))

        print('+' + '-' * (table_width - 2) + '+')
        for expense in expenses:
            day = str(expense.day).ljust(day_length)
            amount = str(expense.amount).ljust(amount_length)
            category = str(expense.category).ljust(category_length)
            print("| {} | {} | {} |".format(day, amount, category))
        print('+' + '-' * (table_width - 2) + '+')

    @staticmethod
    def __choose(options=None, type=None, message=None):
        """
        Function that returns user input either from a list of options, or of a specified type
        :param options: The options the user can choose from
        :param type: The type of input requested (only if options != None)
        :param message: Message to display to the user (only if options != None)
        :return: Checked user input
        """
        if options is not None:
            valid_inputs = range(1, len(options) + 1)
            input_to_key = list(options.keys())

            for index, string in zip(valid_inputs, options):
                print("{}. {}".format(index, string))

            while True:
                try:
                    user_input = int(input('Choice: '))

                    if user_input in valid_inputs:
                        return options[input_to_key[user_input - 1]]  # compensate for 0 indexing
                    else:
                        UI.__warn_invalid_range()
                except ValueError:
                    UI.__warn_invalid_format()
                    continue
        elif type is not None:
            while True:
                try:
                    user_input = type(input('{}: '.format(message)))
                    return user_input
                except:
                    UI.__warn_invalid_format()

    def __call_add_expense(self):
        day = -1
        while day not in range(1, 31):
            day = UI.__choose(type=int, message='Day (0-30)')
        amount = UI.__choose(type=int, message='Amount')
        category = UI.__choose(type=str, message='Category')

        self.__services.add_expense(day, amount, category)
        UI.__clear_screen()

    def __call_filter_expenses(self):
        threshold = self.__choose(type=int, message='Threshold')

        self.__services.filter_expenses(threshold)
        UI.__clear_screen()

    @staticmethod
    def __warn_invalid_format():
        """
        Called whenever the user input is of an invalid format
        """
        print('Invalid input format')

    @staticmethod
    def __warn_invalid_range():
        """
        Called whenever the user input is out of a specified range
        """
        print('Input out of range')

    @staticmethod
    def __clear_screen():
        """
        Clear the console screen
        """
        os.system('clear')