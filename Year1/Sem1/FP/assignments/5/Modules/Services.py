from Modules.Expense import Expense
from Modules.Exceptions import IllegalUndo
import copy

class Services:
    def __init__(self):
        self.__initialize_list()

    def add_expense(self, day, amount, category):
        """
        Function that adds a new expense to the current list, by calling the expense constructor with the given parameters
        :param day: The day of the expense
        :param amount: The amount of the expense
        :param category: The category of the expense
        """
        self.__expenses.append(Expense(day, amount, category))  # Call the constructor and append to the list
        self.__save_state()  # Flush changes to history

    def filter_expenses(self, threshold):
        for expense in self.__expenses[:]:
            if expense.amount <= threshold:
                self.__expenses.remove(expense)
        self.__save_state()

    def get_expenses(self):
        return self.__expenses

    def get_extended_expenses(self):
        max_length_day, max_length_amount, max_length_category = 3, 6, 8

        for expense in self.__expenses:
            if len(str(expense.day)) > max_length_day:
                max_length_day = len(str(expense.day))
            if len(str(expense.amount)) > max_length_amount:
                max_length_amount = len(str(expense.amount))
            if len(expense.category) > max_length_category:
                max_length_category = len(expense.category)

        return self.__expenses, max_length_day, max_length_amount, max_length_category

    def undo(self):
        # print('Calling undo')
        # print('History has {} elements'.format(len(self.__history)))

        if len(self.__history) == 1:
            raise IllegalUndo('Cannot undo any further')

        self.__history.pop()
        self.__expenses = copy.deepcopy(self.__history[-1])

    def __initialize_list(self):
        self.__expenses = [
            Expense(1, 10, 'coffee'),
            Expense(15, 55, 'clothes'),
            Expense(22, 114, 'equipment'),
            Expense(5, 25, 'food'),
            Expense(13, 18, 'food'),
            Expense(24, 127, 'clothes'),
            Expense(7, 112, 'clothes'),
            Expense(15, 1511, 'equipment'),
            Expense(1, 153, 'clothes'),
            Expense(2, 12, 'food'),
            Expense(5, 5, 'coffee'),
        ]
        self.__history = [copy.deepcopy(self.__expenses)]

    def __save_state(self):
        """
        Flush the current list of expenses to history
        """
        if self.__history[-1] != self.__expenses:
            self.__history.append(copy.deepcopy(self.__expenses))