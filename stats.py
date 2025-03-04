# Functon to count the words in the document
def word_count(input_text: str) -> str:
    return len(input_text.split())

# Function to count the characters in the document
def char_count(input_text: str) -> dict[str: int]:
    lower_chars: str = input_text.lower()

    chars_sep: dict[str: int] = {}

    for char in (lower_chars):    
        if char not in chars_sep:
            chars_sep[char] = 0
        chars_sep[char] += 1

    return chars_sep

# Function to return key "num" from dict 
def sort_on(item: list[dict[str: str, str: int]]) -> int:
    return item["num"]

# Function to print sorted dict
def sorted_dict(argv: dict[str: int]) -> None:

    new_list: list[str: str, str: int] = []

    # Iterate through dict argv, for each letter in argv check if alpha character
    # if it is alpha, append to new list in key: value, key: value format (double dict?)
    for letter in argv:
        if letter.isalpha(): 
            new_list.append({"letter": letter, "num": argv[letter]})
    
    # Sort the list, using "num" aka sort numbers highest to lowest
    new_list.sort(reverse=True, key=sort_on)
    
    # For every instance of i in our new list, print the values (our now sorted dict)
    for i in new_list:
        print(f"{i['letter']}: {i['num']}")
