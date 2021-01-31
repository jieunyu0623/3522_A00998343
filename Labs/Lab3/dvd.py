from Labs.Lab3.item import Item


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

    def get_release_date(self):
        """
        Gets the release date of the dvd.
        :return: self._release_date
        """
        return self._release_date

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


def main():
    """
    Tests the dvd methods.
    """
    dvd = Dvd("263.25A", "Burgers and Yam Fries", 3, "Dr. Hou", "2020-06-23", "BC")
    print(dvd)
    print(dvd.check_availability())


if __name__ == '__main__':
    main()
