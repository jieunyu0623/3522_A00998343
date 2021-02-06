from datetime import datetime

from transactions import Transactions
from users import Users


class Menu:

    @staticmethod
    def user_menu():
        """user = Users.register_user()
        print("***********Menu***********")
        print("1. View Budgets")
        print("2. Record a Transaction")
        print("3. View Transactions by Budget")
        print("View Bank Account Details")
        choice = int(input("Choose one: "))

        if choice == 1:
            print(user.get_budgets())

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
                    transaction = Transactions(time_now, amount, user.get_budgets()[num], description)
                    user.get_budgets()[num].add_transaction(transaction)
                    user.get_budgets()[num].spend_money(transaction.get_dollar())
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
                    user.get_budgets()[num].show_all_transactions()"""
