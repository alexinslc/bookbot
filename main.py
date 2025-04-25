import sys
from stats import get_num_words
from stats import get_character_count
from stats import sort_character_count



def get_book_text(path_to_file):
    with open(path_to_file) as file:
       file_contents = file.read()
    return file_contents


def main():
    # Check if sys.argv has two entries
    # If not, print a message explaining how to use the program and exit with status code 1
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        # If sys.argv has two entries, use the second entry as the book path
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_character_count = get_character_count(text)
    num_words = get_num_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count --------")
    print(sort_character_count(num_character_count))
    print("============= END ===============")

main()