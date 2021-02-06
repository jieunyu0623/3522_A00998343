from datetime import datetime

from Labs.Lab4.clothingAccessories import ClothingAccessories
from Labs.Lab4.eatingOut import EatingOut
from Labs.Lab4.gamesEntertainment import GamesEntertainment
from Labs.Lab4.miscellaneous import Miscellaneous
from Labs.Lab4.transactions import Transactions


class Users:

    def __init__(self, user_name, age, bank_account_number, bank_name, bank_balance, budgets):
        self._user_name = user_name
        self._age = age
        self._bank_account_number = bank_account_number
        self._bank_name = bank_name
        self._bank_balance = bank_balance
        self._budgets = [GamesEntertainment(budgets), ClothingAccessories(budgets), EatingOut(budgets),
                         Miscellaneous(budgets)]

    def get_user_name(self):
        return self._user_name

    def get_age(self):
        return self._age

    def get_bank_account_number(self):
        return self._bank_account_number

    def get_bank_name(self):
        return self._bank_name

    def get_bank_balance(self):
        return self._bank_balance

    def get_budgets(self):
        return self._budgets

    @staticmethod
    def register_user():
        print("************User Registration************")
        name = input("Name: ")
        age = int(input("Age: "))
        bank_name = input("Bank Name: ")
        account_number = input("Bank Account Number: ")
        bank_balance = int(input("Account Balance: "))
        budgets = int(input("Budget: "))
        user = Users(name, age, account_number, bank_name, bank_balance, budgets)
        if user:
            print("The user is registered successfully!")
            return user
        else:
            print("User Registration failed! Please try again.")
            return

    @staticmethod
    def load_test_user():
        test_user = Users("Pam Beasley", 16, "1001001234", "TD Bank", 1640.35, 100)
        return test_user

    def user_menu(self):  # put this menu in a new class? but how do we access users that are already created?
        # user = Users.register_user()
        choice = None
        while choice != 4:
            print("***********Menu***********")
            print("1. View Budgets")
            print("2. Record a Transaction")
            print("3. View Transactions by Budget")
            print("4. Quit")
            print("View Bank Account Details")
            choice = int(input("Choose one: "))

            if choice == 1:
                print(self.get_budgets())

            if choice == 2:
                print("*****Record Transactions*****")
                amount = float(input("Amount: "))
                description = input("Location/Description: ")
                time_now = datetime.now().strftime("%Y-%m-%d %H:%M")
                print("Type of budget:")
                print("1. Games and Entertainment")
                print("2. Clothing and Accessories")
                print("3. Eating Out")
                print("4. Miscellaneous")
                budget_type = int(input("Select one: "))

                for num in range(4):
                    if budget_type == num + 1:
                        transaction = Transactions(time_now, amount, self.get_budgets()[num], description)
                        self.get_budgets()[num].add_transaction(transaction)
                        # print(self.get_budgets()[num].show_all_transactions())
                        self.get_budgets()[num].spend_money(transaction.get_dollar())
                        # print(self.get_budgets()[num].get_amount_left())
                        if transaction:
                            print("Transaction successfully recorded!")

            if choice == 3:
                print("1. Games and Entertainment")
                print("2. Clothing and Accessories")
                print("3. Eating Out")
                print("4. Miscellaneous")
                budget_choice = int(input("Choose one: "))

                for num in range(4):
                    if budget_choice == num + 1:
                        self.get_budgets()[num].show_all_transactions()

            if choice == 4:
                pass


def main():
    user = Users.load_test_user()
    user.user_menu()
    # print(user.get_budgets()[2].show_all_transactions())


if __name__ == '__main__':
    main()
