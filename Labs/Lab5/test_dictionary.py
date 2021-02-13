from unittest import TestCase

from dictionary import WordNotFound, Dictionary, DictionaryNotLoaded


class TestDictionary(TestCase):
    """
    unit test for Dictionary class.
    """
    def test_word_not_found(self):
        """
        tests if no words are found and throws the WordNotFound exception.
        :return: WordNotFound
        """
        d = Dictionary()
        d.load_dictionary("data.json")
        self.assertRaises(WordNotFound, d.query_definition, "xxxx")

    def test_is_data_loaded(self):
        """
        tests if is_data_loaded funtion works fine.
        :return: True
        """
        d = Dictionary()
        d.load_dictionary("data.json")
        self.assertTrue(d.is_data_loaded, "Dictionary is empty!")

    def test_dictionary_not_loaded(self):
        """
        tests if DictionaryNotLoaded exception occurs when the dictionary is not loaded.
        :return: DictionaryNotLoaded
        """
        d = Dictionary()
        self.assertRaises(DictionaryNotLoaded, d.query_definition, "hello")

    def test_write_definition(self):
        """
        tests if write_definition function works fine.
        :return: String
        """
        d = Dictionary()
        d.load_dictionary("data.json")
        output = "\n***dog***\n" \
                 "\nA common four-legged animal, especially kept by people as a pet or to hunt or guard things.\n" \
                 "\nA dull, unattractive girl or woman.\n" \
                 "\nAn iron for holding wood in a fireplace.\n"
        self.assertEqual(d.write_definition("dog"), output)
