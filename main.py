def main():
  path = "./books/frankenstein.txt"
  text = get_book_text(path)
  print(text)

def get_book_text(path):
  with open("./books/frankenstein.txt", encoding="utf-8") as file:
    return file.read()

main()