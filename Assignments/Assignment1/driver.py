from Assignments.Assignment1.menu import Menu
from Assignments.Assignment1.troubleMaker import TroubleMaker
from Assignments.Assignment1.users import Users


def main():
    """
    driver class to test budget management system.
    :return: None
    """
    users = Users.load_test_user()  # calls hard coded users (that are stored in a list)
    m = Menu()  # calls menu
    for user in users:  # calls each users and store to our user lists.
        m.add_users(user)
        user.get_miscellaneous().set_user_type(TroubleMaker)
        user.get_eating_out().set_user_type(TroubleMaker)
        user.get_clothing_accessories().set_user_type(TroubleMaker)
        user.get_games_entertainment().set_user_type(TroubleMaker)

    m.log_in()  # goes to log in screen right away without having to register a new user.


if __name__ == '__main__':
    main()
