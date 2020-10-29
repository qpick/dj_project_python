def parser():
    file = open("example.txt", "r")
    counter = 0
    content = file.read()
    co_list = content.split("\n")
    for i in co_list:
        if i:
            counter += 1

    print("%s = %d" % ("Found total of sentences", counter), file=open("example.txt", "a"))
    print("%s = %d\n" % ("sentences", counter), file=open("example.txt", "a"))
    number_of_characters = len(content)
    print("%s = %d" % ("Found total of characters", number_of_characters), file=open("example.txt", "a"))
    new_dict = {'total_sentences': counter}
    print(([f'{key} : {new_dict[key]}' for key in new_dict]), file=open("example.txt", "a"))

    file = open("example.txt", "r")
    lists = []
    lines = file.read().splitlines()
    for line in lines:
        lists.append(line)

    print(lists, file=open("example.txt", "a"))
