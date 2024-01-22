def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    word_count = count_words(text)
    print(word_count)


def get_book_text(path):
    with open("./books/frankenstein.txt", encoding="utf-8") as file:
        return file.read()


def count_words(text):
    words = text.split()
    return len(words)


main()
