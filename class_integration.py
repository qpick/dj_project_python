class Parserfile():

    def __init__(self, file_name):
        self.lines = open(file_name, 'r').readlines()

    def process(self):
        number_of_sentences = len(self.lines)
        characters = 0

        for lines in self.lines:
            characters += len(lines)

        new_dict = {"sentences": self.lines, "stats": {'total_sentences': number_of_sentences, 'total_chars': characters}}
        return new_dict

