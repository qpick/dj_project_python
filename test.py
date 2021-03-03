import unittest
from parser import FileParser


class TestParser(unittest.TestCase):
    test_file = 'test/data/sample1.txt'

    def test_handle_non_existent_path_to_file(self):
        """Test that there is clean exit on non-existing/false path of file."""
        not_existing_path = '/not/existing/path'
        with self.assertRaises(SystemExit):
            (FileParser()).parse(not_existing_path)

    def test_parser_return_correct_text_of_file_first_sentences(self):
        """Test that parser return correct text of the first sentence."""
        data = (FileParser()).parse(self.test_file)
        self.assertFalse(data['sentences'][0] == '')

    def test_parser_return_correct_text_of_file_second_sentences(self):
        """Test that parser return correct text of the second sentence."""
        data = (FileParser()).parse(self.test_file)
        self.assertFalse(data['sentences'][1] == '')

    def test_parser_return_correct_number_of_sentences(self):
        """Test that parser return correct number of sentences."""
        data = (FileParser()).parse(self.test_file)
        self.assertFalse(data['stats']['total_sentences'] == 0)

    def test_parser_return_correct_number_of_characters(self):
        """Test that parser return correct number of characters."""
        data = (FileParser()).parse(self.test_file)
        self.assertFalse(data['stats']['total_chars'] == 0)


if __name__ == "__main__":
    unittest.main()
