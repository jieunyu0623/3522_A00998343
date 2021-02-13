from unittest import TestCase

from file_handler import FileHandler, InvalidFileTypeError


class TestFileHandler(TestCase):
    """
    unit test for FileHandler class.
    """

    def test_load_data_file_not_found(self):
        """
        tests if FileNotFoundError exception runs when the file does not exist.
        :return: FileNotFoundError
        """
        self.assertRaises(FileNotFoundError, FileHandler.load_data, "data2.json", ".json")

    def test_load_data_invalid_data_type(self):
        """
        tests if the data type passed to load_data function is in the correct format.
        if not, it throws InvalidFileTypeError.
        only .json and .txt formats are accepted.
        :return: InvalidFileTypeError
        """
        self.assertRaises(InvalidFileTypeError, FileHandler.load_data, "dictionary.py", ".py")

    def test_write_lines(self):
        """
        tests if write_lines function works fine.
        does the function write lines to the path? if yes, it passes the test.
        :return: True
        """
        count = 0
        count_after = 0
        file = "test.txt"
        with open(file) as f:
            for _ in f:
                count += 1

        msg = "\n***dog***\n" \
              "\nA common four-legged animal, especially kept by people as a pet or to hunt or guard things.\n" \
              "\nA dull, unattractive girl or woman.\n" \
              "\nAn iron for holding wood in a fireplace.\n"
        FileHandler.write_lines(file, msg)
        with open(file) as f:
            for _ in f:
                count_after += 1
        self.assertNotEqual(count, count_after)
