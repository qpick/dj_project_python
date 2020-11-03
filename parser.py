import re


class FileManager:
    def __init__(self, name):
        self.name = str(name)
        self.fileName = open(self.name, "r")
        self.context = str(self.fileName.read())
        self.context = self.context.replace("\n", " ")
        self.context = re.sub(" +", " ", self.context)
        self.listContext = []
        self.listContext = re.split("[.?!]", self.context)
        self.noOfSentences = len(self.listContext)
        self.noOfChars = len(self.context)
        self.fileName.close()
        self.dictionary = {"total_sentences": f"{self.noOfSentences}", "total_chars": f"{self.noOfChars}"}

    def contextlist(self):
        return self.listContext

    def contextdic(self):
        return self.dictionary

    def showlist(self):
        for i in self.contextlist():
            print(i)

    def showresult(self):
        print(f"Found total of {self.dictionary['total_sentences']} sentences")
        print(f"With total of {self.dictionary['total_chars']} character in the file")
