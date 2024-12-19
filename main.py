def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    print(f"{num_words} words found in this document")
    print(char_count)

def get_char_count(text):
    letter_count = {}
    lower_char = text.lower()
    for l in lower_char:
        if l.isalpha():
            if l in letter_count:
                letter_count[l] += 1
            else:
                letter_count[l] = 1
    return letter_count

def get_num_words(book_text):
    words = book_text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()