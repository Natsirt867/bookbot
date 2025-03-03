from stats import word_count    
from stats import char_count
from stats import sorted_dict
import sys



def get_book_text(fp: str) -> str:
    with open(fp, 'r', encoding='utf-8') as f:
        read_book_text = f.read()
    return read_book_text

def main():
    book_text: str = get_book_text(sys.argv[1])
    print("""============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------""")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    sorted_dict(char_count(book_text))
    print("============= END ===============")
    return 0

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        raise IndexError("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()
