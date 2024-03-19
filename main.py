def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    num_chars = character_count(book_text)
    print(num_chars)


# Check for word count of book
def word_count(book_text):
    words = book_text.split()
    return len(words)


# Check for character count (lowered) of book
def character_count(book_text):
    char_count_dict = {}
    for i in book_text:
        lowered_char = i.lower()
        if i != lowered_char:
            i = lowered_char
        if i not in char_count_dict:
            char_count_dict[i] = 1
        else:
            char_count_dict[i] += 1
    return print(char_count_dict)


# Get book content (text)
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()