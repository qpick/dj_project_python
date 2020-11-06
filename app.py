from class_integration import Parserfile


# import of function
from function_integration import process_function


def main():
    create_parser = Parserfile('example.txt')
    data = create_parser.process()
    print(
        data.get('stats', {}).get('total_sentences', 0)
    )

    # call of the function
    data = process_function('example.txt')
    print(
        data.get('stats', {}).get('total_sentences', 0)
    )


# pass

if __name__ == '__main__':
    main()
