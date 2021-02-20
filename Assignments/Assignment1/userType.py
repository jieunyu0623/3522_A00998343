import abc

from Assignments.Assignment1.users import Users


class UserType(abc.ABC):
    """
    UserType abstract class for three different user types.
    """

    def __init__(self):
        """
        constructs an user type object.
        """
        pass

    @abc.abstractmethod
    def lock_account(self, user: Users):
        """
        locks the budget category if the user exceeds a specified amount.
        :param user: Users
        :return: None
        """
        pass

    @abc.abstractmethod
    def warning_message(self, user: Users):
        """
        gives the user warning message if the user exceeds a stated amount.
        :param user: Users
        :return: None
        """
        pass

    @abc.abstractmethod
    def notification(self, user: Users):
        """
        gives the user notification if the user exceeds a set amount.
        :param user: Users
        :return: None
        """
        pass
