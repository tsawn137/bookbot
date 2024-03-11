def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    
    print(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for j in num_chars_dict:
        sorted_list.append({"char": j, "num": num_chars_dict[j]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_chars_dict(text):
    chars = {}
    for c in text:
        i = c.lower()
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()