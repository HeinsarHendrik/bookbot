def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = word_count(book_text)
    num_chars = character_count(book_text)
    generate_report(book_path,num_words,num_chars)
    

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
    return char_count_dict

def generate_report(book_path,num_words,num_chars):

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words were found in the document \n")

    # Create list of dictionaries
    char_list = []
    char_list_dict = {}
    for i in num_chars:
        is_letter = i.isalpha()
        if is_letter == True:
            char_list.append({"char":i,"num":num_chars[i]})

    # Sort list
    def sort_on(dict):
        return dict["num"]
    
    char_list.sort(reverse=True, key=sort_on)

    # Print number of characters report
    for i in range(0, len(char_list)):
        print(f"The character {char_list[i]["char"]} character was found {char_list[i]["num"]} times")

    print("--- End of report ---")

# Get book content (text)
def get_book_text(path):
    with open(path) as f:
        return f.read()

main()