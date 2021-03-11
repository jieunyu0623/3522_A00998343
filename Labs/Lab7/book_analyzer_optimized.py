import cProfile
import re
import pstats
import io

"""
This module is responsible for holding a badly written (but not so bad
that you won't find this in the workplace) BookAnalyzer class that needs
to be profiled and optimized.
"""


class BookAnalyzerProfiled:
    """
    This class provides the ability to load the words in a text file in
    memory and provide the ability to filter out the words that appear
    only once.
    """

    # a constant to help filter out common punctuation.
    # COMMON_PUNCTUATION = [",", "*", ";", ".", ":", "(", "[", "]", ")"]

    def __init__(self):
        self.text = None

    def read_data(self, src="House of Usher.txt"):
        """
        Reads through a text file and loads in all the words. This
        function also processes the words such that all whitespace and
        common punctuation is removed.
        :param src: the name of the file, a string
        """
        # read lines
        with open(src, mode='r', encoding='utf-8') as book_file:
            self.text = book_file.readlines()

        # strip out empty lines
        stripped_text = [line for line in self.text if line != "\n"]
        self.text = stripped_text

        # convert list of lines to list of words
        words = [word for line in self.text for word in line.split()]
        self.text = words

        # remove common punctuation from words
        temp_text = {}
        for word in self.text:
            text_word = re.sub(r'[,*;.:()[\]]', '', word)

            if text_word not in temp_text:
                temp_text[text_word] = 1

        self.text = temp_text.keys()

        return self.text

    # @staticmethod
    # def is_unique(word, word_list):
    #     """
    #     Checks to see if the given word appears in the provided sequence.
    #     This check is case in-sensitive.
    #     :param word: a string
    #     :param word_list: a sequence of words
    #     :return: True if not found, false otherwise
    #     """
    #     word_lowered = word.lower()
    #     for a_word in word_list:
    #         if word_lowered == a_word.lower():
    #             return False
    #     return True

    # def find_unique_words(self):
    #     """
    #     Filters out all the words in the text
    #     :return: a list of all the unique words.
    #     """
    #     temp_text = self.text
    #     unique_words = []
    #     while temp_text:
    #         word = temp_text.pop()
    #         if self.is_unique(word, temp_text):
    #             unique_words.append(word)
    #     return unique_words


def main():
    pr = cProfile.Profile()
    pr.enable()

    # … code to be profiled comes here …
    # … end code to be profiled …

    book_analyzer = BookAnalyzerProfiled()
    book_analyzer = book_analyzer.read_data()
    # unique_words = book_analyzer.find_unique_words()
    # print("-" * 50)
    # print(f"List of unique words (Count: {len(book_analyzer)})")
    # print("-" * 50)
    # for word in book_analyzer:
    #     print(word)
    # print("-" * 50)

    pr.disable()
    s = io.StringIO()
    sortby = pstats.SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).strip_dirs().sort_stats(sortby)
    ps.print_stats()  # print to the StringIO output stream ‘s’.
    print(s.getvalue())  # print the output stream ‘s’


if __name__ == '__main__':
    main()
