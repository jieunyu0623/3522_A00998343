from Labs.Lab4.userType import UserType
from Assignments.Assignment1.users import Users


class TroubleMaker(UserType):
    """
    TroubleMaker class using the abstract class UserType.
    A user type TroubleMaker.
    """

    def __init__(self):
        """
        constructs an user type by using the super class constructor.
        """
        super().__init__()

    def lock_account(self, user: Users):
        """
        locks the budget category if the user exceeds 120% of the amount assigned
        to the budget.
        :param user: Users
        :return: None
        """
        for budget in user.get_budgets():
            if budget.get_amount_spent() > budget.get_budget() * 1.2:
                budget.lock_budget()

    def warning_message(self, user: Users):
        """
        gives the user warning message if the user exceeds 75% of the amount
        assigned to the budget.
        :param user: Users
        :return: None
        """
        for budget in user.get_budgets():
            if (0.75 * budget.get_budget()) < budget.get_amount_spent() < budget.get_budget():
                print("\nYou have spent more than 75 % of the budget!\n")

    def notification(self, user: Users):
        """
        gives the user notification if the user exceeds the budget amount.
        :param user: Users
        :return: None
        """
        for budget in user.get_budgets():
            if budget.get_budget() * 1.2 > budget.get_amount_spent() > budget.get_budget():
                print("\nYou have exceeded the budget. It is recommended to stop your spending.\n")
