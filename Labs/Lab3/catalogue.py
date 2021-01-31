import difflib
import pdb

from Labs.Lab3.book import Book
from Labs.Lab3.dvd import Dvd
from Labs.Lab3.journal import Journal
from libraryItemGenerator import LibraryItemGenerator


class Catalogue:
    """
    A class used to manage library collection of items.
    """

    def __init__(self, catalogue_list):
        """
        Initialize a Catalogue object with a list of Items.
        :param catalogue_list: list of Items
        """
        self._catalogue_list = catalogue_list

    def get_list(self):
        """
        gets the Catalogue list of items.
        :return:
        """
        return self._catalogue_list

    def find_items(self, title):
        """
        Find items with the same and similar title.
        :param title: a string
        :return: a list of titles.
        """
        title_list = []
        for library_item in self._catalogue_list:
            title_list.append(library_item.get_title())
        results = difflib.get_close_matches(title, title_list,
                                            cutoff=0.5)
        return results

    def add_item(self):
        """
        Add a brand new item to the Library with a unique call number.
        if the item already exists, don't add the item.
        """
        item = LibraryItemGenerator.create_item()
        pdb.set_trace()
        self._catalogue_list.append(item)
        found_item = self._retrieve_item_by_call_number(item.call_number)
        if found_item:
            print(f"Could not add item with call number "
                  f"{item.call_number}. It already exists.")
        else:
            self._catalogue_list.append(item)
            print("Item has been added successfully!")
            print("Item details: ")
            print(item)

    def remove_items(self, call_number):
        """
        Remove an existing item from the library's catalogue
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        found_item = self._retrieve_item_by_call_number(call_number)
        if found_item:
            self._catalogue_list.remove(found_item)
            print(f"Successfully removed {found_item.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"book with call number: {call_number} not found.")

    def return_item(self, call_number):
        """
        Return an item with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        status = self.increment_item_count(call_number)
        if status:
            print("item returned successfully!")
        else:
            print(f"Could not find item with call number {call_number}"
                  f". Return failed.")

    def _retrieve_item_by_call_number(self, call_number):
        """
        A private method that encapsulates the retrieval of an item with
        the given call number from the library.
        :param call_number: a string
        :return: book object if found, None otherwise
        """
        found_item = None
        for item in self._catalogue_list:
            if item.call_number == call_number:
                found_item = item
                break
        return found_item

    def display_available_items(self):
        """
        Display all the items in the library.
        """
        print("Item List")
        print("--------------", end="\n\n")
        for library_item in self._catalogue_list:
            print(library_item)

    def increment_item_count(self, call_number):
        """
        Increment the item count for an item with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the item was found and count incremented, false
        otherwise.
        """
        library_item = self._retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.increment_number_of_copies()
            return True
        else:
            return False

    def reduce_item_count(self, call_number):
        """
        Decrement the item count for an item with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the book was found and count decremented, false
        otherwise.
        """
        library_item = self._retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.decrement_number_of_copies()
            return True
        else:
            return False


def main():
    """
    Tests the catalogue methods.
    """
    book = Book("263.25A", "Burgers and Yam Fries", 3, "Dr. Hou")
    journal = Journal("267.21B", "I am hungry!", 5, "Dr. Hou", "THE NEWYORK TIMES", 21, "James Poul")
    dvd = Dvd("193.25C", "Overwatch is fun", 2, "Dr. Hou", "2020-06-23", "BC")
    cat = Catalogue([book, journal, dvd])
    # print(cat.get_list()[0])
    # print(cat.get_list()[1])
    # print(cat.get_list()[2])
    # print(cat.find_items("Burgers and Yam Fries"))
    cat.add_item()
    cat.display_available_items()


if __name__ == '__main__':
    main()


