from Modules.Services import Services
from Modules.Expense import Expense

def add_expense_match__not_break():
    services = Services()
    services.add_expense(1, 1, 'test')
    expense = Expense(1, 1, 'test')

    assert services.get_expenses()[-1] == expense


def add_expense_mismatch__break():
    services = Services()
    services.add_expense(1, 1, 'test')
    expense = Expense(1, 1, 'break')

    assert services.get_expenses()[-1] != expense


def test_all():
    add_expense_mismatch__break()
    add_expense_match__not_break()