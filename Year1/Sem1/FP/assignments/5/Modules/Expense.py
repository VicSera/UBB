class Expense:
    def __init__(self, day, amount, category):
        self.__day = day
        self.__amount = amount
        self.__category = category

    def __str__(self):
        return "Expense({}, {}, {})".format(self.__day, self.__amount, self.__category)

    def __eq__(self, other):
        return self.__day == other.day and \
            self.__amount == other.amount and \
            self.__category == other.category

    @property
    def day(self):
        return self.__day

    @property
    def amount(self):
        return self.__amount

    @property
    def category(self):
        return self.__category