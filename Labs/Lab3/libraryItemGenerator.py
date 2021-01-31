from book import Book
from dvd import Dvd
from journal import Journal


class LibraryItemGenerator:
    """
    A class used to generate an item.
    """

    @staticmethod
    def create_item():
        """
        Creates an item.
        :return: an item
        """
        print("What kind of items would you like to add to the library catalogue?")
        print("1. Book")
        print("2. DVD")
        print("3. Journal")

        option = int(input("Select type of item: "))

        title = input("Enter title: ")
        call_num = input("Enter call number: ")
        author = input("Enter author name: ")
        num_copies = input("Enter the number of copies: ")

        if option == 1:
            return Book(call_num, title, num_copies, author)

        if option == 2:
            release_date = input("Enter release date: ")
            region_code = input("Enter region code: ")
            return Dvd(call_num, title, num_copies, author, release_date, region_code)

        if option == 3:
            names = input("Enter name: ")
            issue_number = input("Enter issue number: ")
            publisher = input("Enter publisher: ")
            return Journal(call_num, title, num_copies, author, names, issue_number, publisher)


