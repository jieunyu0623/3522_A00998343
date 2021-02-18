from Assignments.Assignment1.budgets import Budgets


class Miscellaneous(Budgets):
    """
    child class of the Budget class.
    A budget category Miscellaneous.
    """

    def __init__(self, budget):
        """
        passes the budget amount to the super class constructor.
        :param budget: float
        """
        super().__init__(budget)