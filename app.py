from class_integration import Parserfile


# importiranje na funkcija
# from function_integration import parser


def main():
    create_parser = Parserfile()
    create_parser.characters('example.txt')
    counter = create_parser.sentences('example.txt')
    create_parser.create_dict('example.txt', counter)
    create_parser.create_list('example.txt')

    # povikuvanje na funckija
    # parser()


# pass


if __name__ == '__main__':
    main()
