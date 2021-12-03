def process_function(file_name):
    lines = open(file_name, 'r').readlines()

    number_of_sentences = len(lines)
    characters = 0

    for lines in lines:
        characters += len(lines)

    new_dict = {"sentences": lines, "stats": {'total_sentences': number_of_sentences, 'total_chars': characters}}
    return new_dict
