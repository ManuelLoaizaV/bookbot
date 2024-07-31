def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def get_n_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for chr in text:
        if not chr.isalpha():
            continue
        lowered_chr = chr.lower()
        if lowered_chr in chars:
            chars[lowered_chr] += 1
        else:
            chars[lowered_chr] = 1
    return chars


def chars_dict_to_sorted_list(chars_dict):
    items = list(chars_dict.items())
    items.sort(reverse=True, key=lambda item: item[1])
    return items


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    n_words = get_n_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{n_words} words found in the document")
    for chr, frequency in chars_sorted_list:
        print(f"The '{chr}' character was found {frequency} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
