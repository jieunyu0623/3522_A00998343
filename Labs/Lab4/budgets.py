from abc import ABC

from Labs.Lab4.budgetStatus import BudgetStatus
from Labs.Lab4.transactions import Transactions


class Budgets(ABC):

    def __init__(self, budget):
        self._budget = budget
        self._amount_spent = 0
        self._amount_left = budget
        self._status = BudgetStatus.UNLOCKED
        self._transaction = []

    def get_budget(self):
        return self._budget

    def spend_money(self, amount):
        self._amount_spent += amount
        self._amount_left -= amount

    def add_transaction(self, transaction: Transactions):
        self._transaction.append(transaction)

    def show_all_transactions(self):
        return self._transaction

    def get_amount_spent(self):
        return self._amount_spent

    def get_amount_left(self):
        return self._amount_left

    def get_budget_status(self):
        return self._status

    def __str__(self):
        return f"Status: {self._status}\n" \
               f"Amount Spent: {self.get_amount_spent()}\n" \
               f"Amount Left: {self.get_amount_left()}\n" \
               f"Total Amount: {self.get_budget()}\n"
