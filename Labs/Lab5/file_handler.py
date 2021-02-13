from enum import Enum
from pathlib import Path


class FileExtensions(Enum):
    """
    specifies the file extension type for the dictionary program.
    """
    TXT = ".txt"
    JSON = ".json"


class InvalidFileTypeError(Exception):
    """
    customized exception for invalid file type.
    """
    def __init__(self, invalid_file_type):
        super().__init__(f"ERROR: Invalid file type detected!")
        self.invalid_file_type = invalid_file_type


class FileHandler:
    """
    a FileHandler class used to reading and writing a file.
    """

    @staticmethod
    def load_data(path, file_extension):
        """
        checks if the file extension is in the correct format.
        checks if the file exists in the path/directory.
        :param path: String
        :param file_extension: FileExtensions
        :return: None
        """
        if not Path(path).exists():
            raise FileNotFoundError("ERROR: File not found!")
        else:
            for file in FileExtensions:
                file_type = [file.value]

        if file_extension not in file_type:
            raise InvalidFileTypeError(file_extension)

        with open(path, mode='r', encoding="utf-8") as file:
            data = file.read()
            return data

    @staticmethod
    def write_lines(path, lines):
        """
        writes the lines to the path.
        :param path: String
        :param lines: String
        :return: None
        """
        with open(path, mode='a', encoding="utf-8") as result:
            for line in lines:
                result.write(line)
