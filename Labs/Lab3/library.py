""" This module houses the library"""
from Labs.Lab3.book import Book
from catalogue import Catalogue


class Library:
    """
    The Library consists of a list of books, DVDs and Journals in Catalogue and provides an
    interface for users to check out, return and find items.
    """

    def __init__(self, catalogue_list: Catalogue):
        """
        Initialize the library with a list of items.
        :param catalogue_list: a sequence of catalogue objects.
        """
        self._catalogue_list = catalogue_list

    def get_catalogue(self):
        """
        Gets the catalogue lists in Library.
        :return: self._catalogue_list
        """
        return self._catalogue_list

    def get_list(self):
        """
        Gets the catalogue list of Items.
        :return: self._catalogue_list.get_list()
        """
        return self._catalogue_list.get_list()

    def check_out(self, call_number):
        """
        Check out an item with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        for item in self._catalogue_list.get_list():
            if item.check_availability():
                if call_number in self._catalogue_list:
                    copies = item.get_num_copies()
                    if copies > 0:
                        self._catalogue_list.reduce_item_count(call_number)
                        print("Checkout complete!")
                    else:
                        print(f"Could not find book with call number {call_number}"
                              f". Checkout failed.")
            else:
                print(f"No copies left for call number {call_number}"
                      f". Checkout failed.")

    def display_library_menu(self):
        """
        Display the library menu allowing the user to either access the
        list of items, check out, return, find, add, remove an item.
        """
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!")
            print("-----------------------")
            print("1. Display all items")
            print("2. Check Out an item")
            print("3. Return an item")
            print("4. Find an item")
            print("5. Add an item")
            print("6. Remove an item")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7)")

            # handle user pressing only enter in menu
            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.get_catalogue().display_available_items()
                user_input = input("Press Enter to continue")

            elif user_input == 2:
                call_number = input("Enter the call number of the item"
                                    " you wish to check out.")
                self.check_out(call_number)
            elif user_input == 3:
                call_number = input("Enter the call number of the item"
                                    " you wish to return.")
                self.get_catalogue().return_item(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the item:")
                found_titles = self.get_catalogue().find_items(input_title)
                print("We found the following:")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                self.get_catalogue().add_item()

            elif user_input == 6:
                call_number = input("Enter the call number of the item")
                self.get_catalogue().remove_items(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """

    b1 = Book("100.200.300", "Harry Potter 1", 2, "J K Rowling"),
    b2 = Book("999.224.854", "Harry Potter 2", 5, "J K Rowling"),
    b3 = Book("631.495.302", "Harry Potter 3", 4, "J K Rowling"),
    b4 = Book("123.02.204", "The Cat in the Hat", 1, "Dr. Seuss")
    cat = Catalogue([b1, b2, b3, b4])
    lib = Library(cat)

    lib.display_library_menu()


if __name__ == '__main__':
    main()
