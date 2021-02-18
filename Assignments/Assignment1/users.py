from Assignments.Assignment1.clothingAccessories import ClothingAccessories
from Assignments.Assignment1.eatingOut import EatingOut
from Assignments.Assignment1.gamesEntertainment import GamesEntertainment
from Assignments.Assignment1.miscellaneous import Miscellaneous


class Users:
    """
    A class used to store user information.
    """

    def __init__(self, user_name, age, bank_account_number, bank_name, bank_balance, budgets):
        """
        constructs an user.
        :param user_name: String
        :param age: int
        :param bank_account_number: String
        :param bank_name: String
        :param bank_balance: float
        :param budgets: float
        """
        self._user_name = user_name
        self._age = age
        self._user_type = None
        self._bank_account_number = bank_account_number
        self._bank_name = bank_name
        self._bank_balance = bank_balance
        gn = GamesEntertainment(budgets)
        ca = ClothingAccessories(budgets)
        eo = EatingOut(budgets)
        m = Miscellaneous(budgets)
        self._budgets = [gn, ca, eo, m]

    def get_user_name(self):
        """
        gets user name.
        :return: String
        """
        return self._user_name

    def get_age(self):
        """
        gets user age.
        :return: int
        """
        return self._age

    def get_bank_account_number(self):
        """
        gets user bank account number.
        :return: String
        """
        return self._bank_account_number

    def get_bank_name(self):
        """
        gets user bank name.
        :return: String
        """
        return self._bank_name

    def get_bank_balance(self):
        """
        gets user bank balance.
        :return: float
        """
        return self._bank_balance

    def get_budgets(self):
        """
        gets user budgets.
        :return: float
        """
        return self._budgets

    def get_games_entertainment(self):
        """
        gets the budget category games and entertainment.
        :return: list
        """
        return self._budgets[0]

    def get_clothing_accessories(self):
        """
        gets the budget category clothing and accessories.
        :return: list
        """
        return self._budgets[1]

    def get_eating_out(self):
        """
        gets the budget category eating out.
        :return: list
        """
        return self._budgets[2]

    def get_miscellaneous(self):
        """
        gets the budget category miscellaneous.
        :return: list
        """
        return self._budgets[3]

    def print_budget_info(self):
        """
        prints all the info in each budget category.
        :return: None
        """
        for budget in self._budgets:
            print(budget)

    @staticmethod
    def load_test_user():
        """
        loads some users.
        :return: list
        """
        test_user1 = Users("Pam Beasley", 16, "1001001234", "TD Bank", 1640.35, 100)
        test_user2 = Users("Jim Halpert", 17, "1008271875", "RBC Bank", 2480.80, 150)
        test_user3 = Users("Angela Martin", 19, "1011039183", "BMO Bank", 4290.00, 200)
        test_users = [test_user1, test_user2, test_user3]
        return test_users
