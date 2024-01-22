def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    word_count = count_words(text)
    letter_count = count_letters(text)

    print_report(path, word_count, letter_count)


def get_book_text(path):
    with open(path, encoding="utf-8") as file:
        return file.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    lower_text = text.lower()
    letter_dict = {}

    for letter in lower_text:
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1

    letter_list = list(letter_dict.items())
    letter_list.sort()

    return letter_list


def print_report(path, word_count, letter_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    for i in range(0, len(letter_list)):
        print(
            f"The '{letter_list[i][0]}' character was found {letter_list[i][1]} times")
    print("--- End report ---")


main()
