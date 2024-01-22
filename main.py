def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    print(letter_count)


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

    return letter_dict


main()
