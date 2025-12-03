from stats import count_words, count_chars

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()




PATH = "books/frankenstein.txt"
if __name__ == "__main__":
    print(f"Found {count_words(get_book_text(PATH))} total words")
    print(count_chars(get_book_text(PATH)))
