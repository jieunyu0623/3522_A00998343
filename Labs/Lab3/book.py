from Labs.Lab3.item import Item


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


def main():
    """
    Tests the book methods.
    """
    book = Book("263.25A", "Burgers and Yam Fries", 3, "Dr. Hou")
    print(book)
    print(book.check_availability())


if __name__ == '__main__':
    main()
