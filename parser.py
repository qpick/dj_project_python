file = open("example.txt", "r")

number_of_lines = 0
number_of_characters = 0

for line in file:
  line = line.strip("\n")

  number_of_lines += 1
  number_of_characters += len(line)

print("sentences:", number_of_lines, "characters:", number_of_characters)
print("Found total of", number_of_lines, "sentences")
print("Found total of", number_of_characters, "characters")



file = open('example.txt','r')
text_list = []

for line in file:
    text_list.append(line.strip("\n"))

print(text_list)

file = open('example.txt','r')
dict = {'total_sentences': number_of_lines, 'total_characters': number_of_characters, 'key3' :3 }

print (dict)

 







