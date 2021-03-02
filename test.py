import os
import unittest
from parser import FileParser
from unittest.mock import mock_open, patch


class TestParser(unittest.TestCase):
    def setUp(self):
        """Create example file for test parsing with 2 sentences and total 28 characters"""
        with patch('__main__.open', mock_open()):
            with open('fictional_example_text.txt', 'w') as file:
                file.write('[Text For Test. Second sentence.')

    def tearDown(self):
        """Delete the example file for test parsing"""
        os.remove('fictional_example_text.txt')

    def test_handle_non_existent_path_to_file(self):
        """Test that there is clean exit on non-existing/false path of file."""
        not_existing_path = '/not/existing/path'
        with self.assertRaises(SystemExit):
            (FileParser()).parse(not_existing_path)

    def test_parser_return_correct_text_of_file_first_sentences(self):
        """Test that parser return correct text of the first sentence."""
        data = (FileParser()).parse('fictional_example_text.txt')
        self.assertEqual(data['sentences'][0], 'Text For Test.')

    def test_parser_return_correct_text_of_file_second_sentences(self):
        """Test that parser return correct text of the second sentence."""
        data = (FileParser()).parse('fictional_example_text.txt')
        self.assertEqual(data['sentences'][1], 'Second sentence.')

    def test_parser_return_correct_number_of_sentences(self):
        """Test that parser return correct number of sentences."""
        data = (FileParser()).parse('fictional_example_text.txt')
        self.assertEqual(data['stats']['total_sentences'], 2)

    def test_parser_return_correct_number_of_characters(self):
        """Test that parser return correct number of characters."""
        data = (FileParser()).parse('fictional_example_text.txt')
        self.assertEqual(data['stats']['total_chars'], 28)


if __name__ == "__main__":
    unittest.main()
