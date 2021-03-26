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

    @property
    def get_title(self):
        """
        Returns the title of an Item.
        :return: a string
        """
        return self._title

    @property
    def get_author(self):
        """
        Returns the author of an Item.
        :return: a string
        """
        return self._author

    @property
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

# ================BOOK======================================================


class Book(Item):
    """
    Represents a single book in a library which is identified through
    its call number.
    """

    def __init__(self, call_num, title, num_copies, author):
        """
        Constructs a book item.
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        super().__init__(call_num, title, num_copies, author)

    @property
    def get_author(self):
        """
        gets the author of the book.
        :return: self._author
        """
        return self._author

    def __str__(self):
        """
        string representation of the Book item.
        :return: string representation
        """
        return f"---- Book: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self.get_num_copies()}\n" \
               f"Author: {self.get_author()}\n"


# ========================DVD=======================================================


class Dvd(Item):
    """
    Represents a single dvd in a library which is identified through
    its call number.
    """

    def __init__(self, call_num, title, num_copies, author, release_date, region_code):
        """
        Constructs a dvd item.
        :param call_num:
        :param title:
        :param num_copies:
        :param author:
        :param release_date:
        :param region_code:
        """
        self._release_date = release_date
        self._region_code = region_code
        super().__init__(call_num, title, num_copies, author)

    @property
    def get_release_date(self):
        """
        Gets the release date of the dvd.
        :return: self._release_date
        """
        return self._release_date

    @property
    def get_region_code(self):
        """
        Gets the region code of the dvd.
        :return: self._region_code
        """
        return self._region_code

    def __str__(self):
        return f"---- DVD: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self.get_num_copies()}\n" \
               f"Author: {self.get_author()}\n" \
               f"Release Date: {self.get_release_date()}\n" \
               f"Region Code: {self.get_region_code()}\n"


# =================================JOURNAL==============================================

class Journal(Item):
    """
    Represents a single journal in a library which is identified through
    its call number.
    """

    def __init__(self, call_num, title, num_copies, author, names, issue_number, publisher):
        """
        Constructs a journal item.
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param names: a string
        :param issue_number: an int
        :param publisher: a string
        """
        super().__init__(call_num, title, num_copies, author)
        self._names = names
        self._issue_number = issue_number
        self._publisher = publisher

    @property
    def get_names(self):
        """
        Gets the name of the journal.
        :return: self._names
        """
        return self._names

    @property
    def get_issue_number(self):
        """
        Gets the issue number of the journal.
        :return: self._issue_number
        """
        return self._issue_number

    @property
    def get_publisher(self):
        """
        Gets the publisher of the journal.
        :return: self._publisher
        """
        return self._publisher

    def __str__(self):
        """
        string representation of the Journal item.
        :return: string representation
        """
        return f"---- Journal: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self.get_num_copies()}\n" \
               f"Author: {self.get_author()}\n" \
               f"Names: {self.get_names()}\n" \
               f"Issue Number: {self.get_issue_number()}\n" \
               f"Publisher: {self.get_publisher()}\n"
