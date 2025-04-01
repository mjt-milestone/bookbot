import sys

from stats import get_num_words, count_characters, sort_report

def check_arguments():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(path_to_file):
    """
    This function takes a path to a file and prints the file contents to the console as a string.
    """
    try:
        with open(path_to_file, 'r') as f:
            file_contents = f.read()
            return file_contents
    except FileNotFoundError:
        print(f"The file at {path_to_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    check_arguments()
    path_to_file = sys.argv[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at <path_to_file>...")
    file_contents = get_book_text(path_to_file)
    if file_contents:
        word_count = get_num_words(file_contents)
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        char_count = count_characters(file_contents)
        sorted_char_count = sort_report(char_count)
        print("--------- Sorted Character Count -------")
        for item in sorted_char_count:
            print(f"{item['character']}: {item['count']}")
    print("============= END ===============")

# Calling the main function
if __name__ == "__main__":
    main()