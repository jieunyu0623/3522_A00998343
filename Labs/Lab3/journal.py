from Labs.Lab3.item import Item


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

    def get_names(self):
        """
        Gets the name of the journal.
        :return: self._names
        """
        return self._names

    def get_issue_number(self):
        """
        Gets the issue number of the journal.
        :return: self._issue_number
        """
        return self._issue_number

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


def main():
    """
    Tests the journal methods.
    """
    journal = Journal("263.25A", "Burgers and Yam Fries", 3, "Dr. Hou", "THE NEWYORK TIMES", 21, "James Poul")
    print(journal)
    print(journal.check_availability())


if __name__ == '__main__':
    main()
