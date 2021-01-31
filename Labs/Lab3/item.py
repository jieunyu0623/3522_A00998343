import abc


class Item(abc.ABC):
    """
    Item abstract class used for books, journals and dvds.
    """

    def __init__(self, call_num, title, num_copies, author):
        """
        Initialize an Item object.
        :param call_num: an int
        :param title: a string
        :param num_copies: a string
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        self._call_num = call_num
        self._title = title
        self._num_copies = num_copies
        self._author = author

    def get_title(self):
        """
        Returns the title of an Item.
        :return: a string
        """
        return self._title

    def get_author(self):
        """
        Returns the author of an Item.
        :return: a string
        """
        return self._author

    def get_num_copies(self):
        """
        Returns the number of copies that are available for this
        specific item.
        :return: an int
        """
        return self._num_copies

    @property
    def call_number(self):
        """
        Right, this here is another way of using properties.
        We use decorators. The @property decorator defines a property
        that only allows us to GET a value and not set one.

        I want to point out that I have not expected you to do this in
        your labs. I'm using this as an opportunity to introduce you to
        a new way of avoiding mechanical getters and setters.
        :return: _call_num
        """
        return self._call_num

    def increment_number_of_copies(self):
        """
        Increases the number of copies of an item by 1.
        """
        self._num_copies += 1

    def decrement_number_of_copies(self):
        """
        Decreases the number of copies of an item by 1.
        """
        self._num_copies -= 1

    def check_availability(self):
        """
        Returns True if the item is available and False otherwise.
        :return: A Boolean
        """
        if self._num_copies > 0:
            return True
        else:
            return False

    @abc.abstractmethod
    def __str__(self):
        pass

