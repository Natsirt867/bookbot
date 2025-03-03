# Functon to count the words in the document
def word_count(input_text: str) -> str:
    count: int = 0
    words_sep: list[str] = input_text.split()
    for i in words_sep:
        count = count + 1
    return f"{count}"

# Function to count the characters in the document
def char_count(input_text: str) -> int:
    lower_chars: str = input_text.lower()

    count: int = 0
    chars_sep: list[str: int] = {}

    while (count < (len(lower_chars))):
        for i in (lower_chars):    
            if i not in chars_sep:
                chars_sep[i] = 0
            for j in chars_sep:
                if i == j:
                    chars_sep[j] += 1
            count += 1

    return chars_sep

# Function to return key "num" from dict 
def sort_on(dict: list[str: str, str: int]) -> str:
    return dict["num"]

# Function to print sorted dict
def sorted_dict(argv: dict[str: int]) -> None:

    new_list: list[str: str, str: int] = []

    # iterate through dict argv, for each letter in argv check if alpha character
    # if it is alpha, append to new list in key: value, key: value format (double dict?)
    for letter in argv:
        if letter.isalpha(): 
            new_list.append({"letter": letter, "num": argv[letter]})
    
    # Sort the list, using "num" aka sort numbers highest to lowest
    new_list.sort(reverse=True, key=sort_on)
    
    # For every instance of i in our new list, print the values (our now sorted dict)
    for i in new_list:
        print(f"{i['letter']}: {i['num']}")
