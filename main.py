def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    char_list = get_dict_list(char_count)
    char_list.sort(reverse = True, key = sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print()
    print(f"{num_words} words found in this document")
    print()
    for dict in char_list:
        print(f"The '{dict["name"]}' character was found {dict["num"]} times")
    print("--- End Report ---")
   
def sort_on(char_count):
    return char_count["num"]

def get_dict_list(char_count):
    list_of_char = []
    for key, value in char_count.items():
        list_of_char.append({"name": key, "num": value})
    return list_of_char

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