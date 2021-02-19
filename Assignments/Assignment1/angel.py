from Labs.Lab4.userType import UserType
from Assignments.Assignment1.users import Users


class Angel(UserType):
    """
    Angel class using the abstract class UserType.
    A user type Angel.
    """

    def __init__(self):
        """
        constructs an user type by using the super class constructor.
        """
        super().__init__()

    def lock_account(self, user: Users):
        """
        no need to lock account for the user type Angel.
        :param user: Users
        :return: None
        """
        pass

    def warning_message(self, user: Users):
        """
        gives the user warning message if the user exceeds 90% of the amount assigned
        to the budget.
        :param user: Users
        :return: None
        """
        for budget in user.get_budgets():
            if budget.get_budget() > budget.get_amount_spent() > (0.90 * budget.get_budget()):
                print("\nYou have spent more than 90 % of your budget!\n")

    def notification(self, user: Users):
        """
        gives the user notification if the user exceeds the budget amount.
        :param user: Users
        :return: None
        """
        for budget in user.get_budgets():
            if budget.get_amount_spent() > budget.get_budget():
                print("\nYou have exceeded the budget.\n")
