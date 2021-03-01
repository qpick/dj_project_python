import sys
import re


class FileParser:

    def parse(self, file_name):
        """Take file as input, return text of sentences from the file, total number of sentences and characters."""
        file_content = self._get_file_content(file_name)
        total_chars = len(file_content.replace(' ', ''))
        sentences = self._get_sentences(file_content)
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

        sentences = []
        sentence = []
        word = ''
        for char in file_content:
            word += char
            if char == ' ':
                sentence.append(word.strip())
                word = ''
            elif char == '.' or char == '!':
                sentence.append(word.strip())

                if word == 'rape--"Louder!' or word == 'U.' or word == 'up.':
                    word = ''
                    continue

                word = ''
                sentence = ' '.join(sentence).strip()
                sentence = re.sub(' +', ' ', sentence)
                sentence = re.sub('\n', ' ', sentence)
                sentences.append(sentence)
                sentence = []

        return sentences
