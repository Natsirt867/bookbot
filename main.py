from stats import word_count    
from stats import char_count
from stats import sorted_dict

def get_book_text(fp: str) -> str:
    with open(fp, 'r', encoding='utf-8') as f:
        read_book_text = f.read()
    return read_book_text

def main():
    book_text: str = get_book_text('books/frankenstein.txt')
    print("""============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------""")
    print(f"Found {word_count(book_text)} total words")
    print("--------- Character Count -------")
    sorted_dict(char_count(book_text))
    print("============= END ===============")


if __name__ == "__main__":
    main()
