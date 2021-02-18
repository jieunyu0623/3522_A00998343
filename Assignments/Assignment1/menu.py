from datetime import datetime

from Assignments.Assignment1.angel import Angel
from Assignments.Assignment1.rebel import Rebel
from Assignments.Assignment1.transactions import Transactions
from Assignments.Assignment1.troubleMaker import TroubleMaker
from users import Users


class UserNotFoundException(Exception):
    def __init__(self):
        print("user not found!")


class Menu:

    def __init__(self):
        self.users = []

    def print_users(self):
        for user in self.users:
            print(user)

    def add_users(self, user: Users):
        self.users.append(user)

    def delete_users(self, user: Users):
        self.users.remove(user)

    def log_in(self):
        if not self.users:
            print("There are no users! Please register a new user.")
            return self.main_menu()

        i = 1
        for user in self.users:
            print(f"{i} - {user.get_user_name()}\n")
            i += 1
        print(f"{i} - Back to main menu")
        choice = int(input("Please Choose one: "))
        if choice == i:
            return self.main_menu()

        if self.users[choice - 1]:
            user = self.users[choice - 1]
            return self.user_menu(user)
        else:
            raise UserNotFoundException()

    def register_user(self):
        print("************User Registration************")
        name = input("Name: ")
        age = int(input("Age: "))
        bank_name = input("Bank Name: ")
        account_number = input("Bank Account Number: ")
        bank_balance = float(input("Account Balance: "))
        budgets = float(input("Budget: "))
        print("1. Rebel")
        print("2. TroubleMaker")
        print("3. Angel")

        user_type = int(input("Choose User Type: "))
        if user_type == 1:
            user_type = Rebel
        if user_type == 2:
            user_type = TroubleMaker
        if user_type == 3:
            user_type = Angel

        user = Users(name, age, account_number, bank_name, bank_balance, budgets)
        user.get_miscellaneous().set_user_type(user_type)
        user.get_eating_out().set_user_type(user_type)
        user.get_games_entertainment().set_user_type(user_type)
        user.get_clothing_accessories().set_user_type(user_type)

        if user:
            print("The user is registered successfully!")
            self.add_users(user)
            return self.main_menu()
        else:
            print("User Registration failed! Please try again.")

    def main_menu(self):

        print("1. Register a new user")
        print("2. Login")
        print("3. Exit")
        choice = int(input("Please choose one: "))
        if choice == 1:
            self.register_user()
        elif choice == 2:
            self.log_in()
        else:
            print("Thank you for using the budget management system!")
            return

    def user_menu(self, user: Users):  # how do we move this to menu?
        choice = None
        while choice != 5:
            print("***********Menu***********")
            print("1. View Budgets")
            print("2. Record a Transaction")
            print("3. View Transactions by Budget")
            print("4. View Bank Account Details")
            print("5. Back to Main Menu")
            choice = int(input("Choose one: "))

            if choice == 1:
                user.print_budget_info()

            if choice == 2:

                count = 0

                if user.get_budgets()[0].get_user_type() == Rebel:
                    for budget in user.get_budgets():
                        if budget.is_locked():
                            count += 1

                    if count >= 2:
                        print("Your account is locked! You can't spend any more money.")
                        return self.user_menu(user)

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
                        if user.get_budgets()[num].is_locked():
                            print("Your account is locked! You can't spend any more money.")
                            return self.user_menu(user)
                        transaction = Transactions(time_now, amount, description)
                        user.get_budgets()[num].add_transaction(transaction)
                        # print(self.get_budgets()[num].show_all_transactions())
                        user.get_budgets()[num].spend_money(transaction.get_dollar())
                        # print(self.get_budgets()[num].get_amount_left())
                        if transaction:
                            print("Transaction successfully recorded!")

                        if user.get_budgets()[num].get_user_type() == TroubleMaker:
                            t = TroubleMaker()
                            t.warning_message(user)
                            t.notification(user)
                            t.lock_account(user)

                        if user.get_budgets()[num].get_user_type() == Angel:
                            a = Angel()
                            a.lock_account(user)
                            a.notification(user)
                            a.warning_message(user)

                        if user.get_budgets()[num].get_user_type() == Rebel:
                            r = Rebel()
                            r.warning_message(user)
                            r.notification(user)
                            r.lock_account(user)

            if choice == 3:
                print("1. Games and Entertainment")
                print("2. Clothing and Accessories")
                print("3. Eating Out")
                print("4. Miscellaneous")
                budget_choice = int(input("Choose one: "))

                for num in range(4):
                    if budget_choice == num + 1:
                        user.get_budgets()[num].show_all_transactions()

            if choice == 4:
                print("\n**** Bank Information ****")
                print(f"Bank Name: {user.get_bank_name()}")
                print(f"Bank Account Number: {user.get_bank_account_number()}")
                print(f"Bank Balance: {user.get_bank_balance()}\n")

            if choice == 5:
                self.main_menu()


def main():
    m = Menu()
    # m.main_menu()
    m.print_users()


if __name__ == '__main__':
    main()
