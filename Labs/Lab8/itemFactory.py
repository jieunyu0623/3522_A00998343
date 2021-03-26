from Labs.Lab3.book import Book
from Labs.Lab3.dvd import Dvd
from Labs.Lab3.item import Item
from Labs.Lab3.journal import Journal


class ItemFactory:

    @staticmethod
    def create_book(**items) -> Item:
        return Book(**items)

    @staticmethod
    def create_dvd(**items) -> Item:
        return Dvd(**items)

    @staticmethod
    def create_journal(**items) -> Item:
        return Journal(**items)






