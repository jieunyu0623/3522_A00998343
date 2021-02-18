from abc import ABC
from enum import Enum

from Assignments.Assignment1.transactions import Transactions


class BudgetStatus(Enum):
    """
    shows enum for locking and unlocking a budget category.
    """
    LOCKED = True
    UNLOCKED = False


class Budgets(ABC):
    """
    budget abstract class for four different type of categories.
    """

    def __init__(self, budget):
        """
        constructs a budget object with budget.
        :param budget: float
        """
        self._budget = budget
        self._amount_spent = 0
        self._amount_left = budget
        self._user_type = None
        self._status = BudgetStatus.UNLOCKED
        self._transaction = []

    @classmethod
    def budget_name(cls):
        """
        returns the budget category name.
        :return: class name
        """
        return cls.__name__

    def get_budget(self):
        """
        gets the budget amount.
        :return: float
        """
        return self._budget

    def get_status(self):
        """
        gets the budget status. (if the budget category is locked or not)
        :return: enum
        """
        return self._status

    def print_status(self):
        """
        prints the budget status.
        :return: String
        """
        if self._status == BudgetStatus.UNLOCKED:
            return "Unlocked"
        if self._status == BudgetStatus.LOCKED:
            return "Locked"

    def spend_money(self, amount):
        """
        subtract the amount passed from the amount left
        and increments the amount spent by the amount passed.
        :param amount: float
        :return: None
        """
        self._amount_spent += amount
        self._amount_left -= amount

    def add_transaction(self, transaction: Transactions):
        """
        adds a transaction to the transaction list.
        :param transaction: Transactions
        :return: None
        """
        self._transaction.append(transaction)

    def show_all_transactions(self):
        """
        prints all transactions in a category.
        :return: None
        """
        for transaction in self._transaction:
            print(f"\n{transaction}\n")

    def get_amount_spent(self):
        """
        gets the amount the user have spent.
        :return: float
        """
        return self._amount_spent

    def get_amount_left(self):
        """
        gets the amount left in the budget.
        :return: float
        """
        return self._amount_left

    def get_user_type(self):
        """
        gets user type.
        :return: UserType
        """
        return self._user_type

    def is_locked(self):
        """
        shows if the budget category is locked or not.
        :return: boolean
        """
        return self._status.value

    def lock_budget(self):
        """
        locks the budget category.
        :return: Enum
        """
        self._status = BudgetStatus.LOCKED

    def unlock_budget(self):
        """
        unlocks the budget category.
        :return: Enum
        """
        self._status = BudgetStatus.UNLOCKED

    def set_user_type(self, user_type):
        """
        sets the user type.
        :param user_type: UserType
        :return: None
        """
        self._user_type = user_type

    def __str__(self):
        """
        shows the string representation of budget information.
        :return: String
        """
        return f"****{self.budget_name()}****\n" \
               f"Status: {self.print_status()}\n" \
               f"Amount Spent: {self.get_amount_spent()}\n" \
               f"Amount Left: {self.get_amount_left()}\n" \
               f"Total Amount: {self.get_budget()}\n"
