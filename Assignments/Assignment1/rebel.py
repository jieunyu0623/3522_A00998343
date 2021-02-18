from Labs.Lab4.userType import UserType
from Assignments.Assignment1.users import Users


class Rebel(UserType):
    """
    Rebel class using the abstract class UserType.
    A user type Rebel.
    """

    def __init__(self):
        """
        constructs an user type by using the super class constructor.
        """
        super().__init__()

    def lock_account(self, user: Users):
        """
        locks the budget category if the user exceeds the amount assigned
        to the budget.
        if more than 2 budget categories exceed the budget, lock all the budget
        categories.
        :param user: Users
        :return: None
        """
        count = 0
        for budget in user.get_budgets():
            if budget.get_amount_spent() > budget.get_budget():
                count += 1
                budget.lock_budget()

        if count >= 2:
            user.get_miscellaneous().lock_budget()
            user.get_eating_out().lock_budget()
            user.get_clothing_accessories().lock_budget()
            user.get_games_entertainment().lock_budget()

    def warning_message(self, user: Users):
        """
        gives the user warning message if the user exceeds 50% of the amount
        assigned to the budget.
        :param user: Users
        :return: None
        """
        for budget in user.get_budgets():
            if budget.get_budget() > budget.get_amount_spent() > (0.50 * budget.get_budget()):
                print("\nWARNING: you have spent more than HALF of your budget! It is strongly "
                      "recommended to cut off your spending.\n")

    def notification(self, user: Users):
        """
        gives the user notification if the user exceeds the budget amount.
        :param user: Users
        :return: None
        """
        for budget in user.get_budgets():
            if budget.get_amount_spent() > budget.get_budget():
                print("\nYou have exceeded the budget limit. DO YOU WANT TO BE A HOBO? "
                      "STOP SPENDING MONEY AND GET A JOB!\n")
