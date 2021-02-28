import sys
import re
import time
from nltk.tokenize.punkt import PunktSentenceTokenizer, PunktParameters


class FileParser:

    def parse(self, file_name):
        """Take file as input, return text of sentences from the file, total number of sentences and characters."""
        start_time = time.time()
        file_content = self._get_file_content(file_name)
        total_chars = len(file_content.replace(' ', ''))
        sentences = self._get_sentences(file_content)
        self._print_output_data(sentences, total_chars)
        self._print_time_for_calculating_and_output(start_time)

        return {
            'sentences': sentences,
            'stats': {'total_sentences': len(sentences), 'total_chars': total_chars}
        }

    def _get_file_content(self, file_name):
        """Open file, return the content of the file."""
        try:
            file = open(file_name)
            file_content = file.read()
            file.close()
        except IOError:
            print(f'Cannot open file {file_name}')
            sys.exit(0)

        return file_content

    def _get_sentences(self, file_content):
        """Refactor text, return sentences."""
        file_content = file_content[file_content.find('['):].replace('[', '').replace(']', '')
        punkt_param = PunktParameters()
        punkt_param.abbrev_types = set(['u.s', 'up'])
        sentence_splitter = PunktSentenceTokenizer(punkt_param)
        file_content = file_content.replace('!"', '^"')
        sentences = sentence_splitter.tokenize(file_content)
        sentences = [re.sub(' +', ' ', i) for i in sentences]
        sentences = [i.replace('\n', ' ') for i in sentences]
        sentences = [i.replace('^', '!') for i in sentences]

        return sentences

    def _print_output_data(self, sentences, total_chars):
        """Print data to console, return none."""
        print(f'Find total of {len(sentences)} sentences')
        print(f'Find total of {total_chars}  character in the file')
        print('===============================================================')
        for items in sentences:
            print('SENTENCE: ', items)

    def _print_time_for_calculating_and_output(self, start_time):
        """Print data to console, return none."""
        end_time = time.time()
        total_time = end_time - start_time

        print('===============================================================')
        print('Time to read and print the file: ', total_time, ' seconds')
