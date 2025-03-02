def word_count(input_text: str) -> str:
    count = 0
    words_sep = input_text.split()
    for i in words_sep:
        count = count + 1
    return f"{count} words found in the document"
 
