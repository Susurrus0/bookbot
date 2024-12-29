def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        book_contents = f.read()
        print(book_contents)
    words = book_contents.split()
    print(f"--- Begin report of {book} ---")
    print(count_words(words))
    print(count_chars(words))


def count_words(words):
    word_count = len(words)
    return f"{word_count} words found in the document."


def count_chars(words):
    chars_dict = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }
    for word in words:
        for letter in word:
            # print(letter)
            if letter.lower() in chars_dict:
                chars_dict[letter.lower()] += 1
    sorted_chars = sorted(chars_dict.items(), key=lambda item: item[1], reverse=True)
    return_string = ""
    for char in sorted_chars:
        return_string += (f"The {char[0]} character was found {char[1]} times.\n")
    return return_string

main()
