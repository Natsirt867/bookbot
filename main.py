from stats import word_count    

def get_book_text(fp: str) -> str:
    with open(fp, 'r', encoding='utf-8') as f:
        read_book_text = f.read()
    return read_book_text

def main():
    book_text = get_book_text('books/frankenstein.txt')
    print(word_count(book_text))

if __name__ == "__main__":
    main()
