from Assignments.Assignment1.budgets import Budgets


class ClothingAccessories(Budgets):
    """
    child class of the Budget class.
    A budget category ClothingAccessories.
    """

    def __init__(self, budget):
        """
        passes the budget amount to the super class constructor.
        :param budget: float
        """
        super().__init__(budget)
