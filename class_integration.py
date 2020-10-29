class Parserfile():
    def __init__(self):
        self.file_name = "example.txt"

    def create_list(self, file_name):
        self.file_name = file_name
        file = open("example.txt", "r")

        lists = []
        lines = file.read().splitlines()
        for line in lines:
            lists.append(line)

        print(lists, file=open("example.txt", "a"))

    def sentences(self, file_name):
        self.file_name = file_name
        file = open("example.txt", "r")
        counter = 0

        content = file.read()
        co_list = content.split("\n")

        for i in co_list:
            if i:
                counter += 1
        print("%s = %d" % ("Found total of sentences", counter), file=open("example.txt", "a"))
        print("%s = %d\n" % ("sentences", counter), file=open("example.txt", "a"))
        return counter

    def characters(self, file_name):
        self.file_name = file_name
        file = open("example.txt")
        data = file.read()
        number_of_characters = len(data)

        print("%s = %d" % ("Found total of characters", number_of_characters), file=open("example.txt", "a"))

    def create_dict(self, file_name, counter):
        self.file_name = file_name

        new_dict = {'total_sentences': counter}
        print(([f'{key} : {new_dict[key]}' for key in new_dict]), file=open("example.txt", "a"))


