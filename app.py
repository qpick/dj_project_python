import time
from parser import FileParser


def main():
    """Main entry"""
    start_time = time.time()

    file = 'example.txt'
    # file = 'test.txt'
    file_parser = FileParser()
    data = file_parser.parse(file)

    print_output_data(data['sentences'], data['stats']['total_chars'])
    print_time_for_calculating_and_output(start_time)


def print_output_data(sentences, total_chars):
    """Print data to console, return none."""
    print(f'Find total of {len(sentences)} sentences')
    print(f'Find total of {total_chars}  character in the file')
    print('===============================================================')
    for items in sentences:
        print('SENTENCE: ', items)


def print_time_for_calculating_and_output(start_time):
    """Print data to console, return none."""
    end_time = time.time()
    total_time = end_time - start_time

    print('===============================================================')
    print('Time to read and print the file: ', total_time, ' seconds')


if __name__ == '__main__':
    main()
