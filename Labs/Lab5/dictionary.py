import json
import os
from difflib import get_close_matches

from file_handler import FileHandler, InvalidFileTypeError


class WordNotFound(Exception):
    """
    customized exception for words that are not found in the dictionary.
    """
    def __init__(self, no_word):
        super().__init__(f"\"{no_word}\"was not found in the dictionary!")
        self.no_word = no_word


class DictionaryNotLoaded(Exception):
    """
    customized exception for data not loaded into the dictionary.
    """
    def __init__(self):
        super().__init__("Dictionary is empty!")


class Dictionary:
    """
    represents a dictionary class with data stored in JSON format.
    """

    def __init__(self):
        """
        initializes dictionary by loading the dat into the dictionary.
        output (output.txt) is the destination where the search history is stored to.
        """
        self._data = None
        self._output = "./output.txt"

    def is_data_loaded(self):
        """
        checks if the data is loaded or not in the dictionary.
        :return: boolean
        """
        return self._data is not None

    def load_dictionary(self, filepath):
        """
        loads the dictionary with the file passed into the method.
        :param filepath: String
        :return: None
        """
        # gets the name and extension split into two in a list.
        name_extension = os.path.splitext(filepath)
        data = FileHandler.load_data(filepath, name_extension[1])

        try:
            self._data = json.loads(data)
        except FileNotFoundError as e:
            print(f"{e}\nThe filepath {filepath} does not exist")
        except InvalidFileTypeError as e:
            print(f"{e}\nThe file type {name_extension[1]} is invalid")
        except Exception as e:
            print(f"{e}\nUnknown Exception caught")
        else:
            print("the dictionary file has been loaded. No exceptions occurred.")
        finally:
            print("Done checking error")

    def write_definition(self, word):
        """
        formats the definitions of a word searched.
        :param word: String
        :return: String
        """
        definitions = self._data.get(word)
        output = f"\n*** {word} ***\n"
        for definition in definitions:
            output += f"\n{definition}\n"
        return output

    def query_definition(self, word):
        """
        looks up the dictionary and see if the word passed exists
        in the dictionary. If the word exists, loads all the definitions
        of the word.
        :param word: String
        :return: String
        """
        if self.is_data_loaded():
            output = ""
            if word in self._data:
                output = self.write_definition(word)
            elif word.lower() in self._data:
                output = self.write_definition(word.lower())
            elif word.capitalize() in self._data:
                output = self.write_definition(word.capitalize())
            elif word.title() in self._data:
                output = self.write_definition(word.title())
            else:
                close_match = get_close_matches(word.lower(), self._data)
                print("Did you mean ")
                if close_match:
                    for match in close_match:
                        print(f"{match}")
                else:
                    raise WordNotFound(word)
        else:
            raise DictionaryNotLoaded()

        return output

    def search(self):
        """
        simulates the dictionary.
        the user prompt to ask for a word to look up.
        any words that are searched are stored in output.txt
        :return: None
        """
        file_type = input("Please enter the name of the dictionary file: ")
        if file_type:
            self.load_dictionary(file_type)
        else:
            raise FileNotFoundError

        while True:
            print("\n\nTo exit the program, please type \"exitprogram\".")
            user_input = input("Word to search: ")
            if user_input.lower() == "exitprogram":
                print("Thank you for using the dictionary program!")
                break
            try:
                result = self.query_definition(user_input)
                if result:
                    print(f"\nResults: {result}")
            except WordNotFound as e:
                print(e)
            else:
                count = 0
                count_after = 0
                with open(self._output) as output:
                    for _ in output:
                        count += 1
                FileHandler.write_lines(self._output, result)
                with open(self._output) as op:
                    for _ in op:
                        count_after += 1

                if count != count_after:
                    print("\nWords successfully written to output.txt!")
            finally:
                print("**** End of search ****")


def main():
    """
    the main to test dictionary class.
    """

    dictionary = Dictionary()
    dictionary.search()


if __name__ == '__main__':
    main()
