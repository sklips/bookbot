from stats import count_words, count_chars, dict_sorter
import sys
def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()





if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        PATH = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {PATH}")
        print("----------- Word Count ----------")
        print(f"Found {count_words(get_book_text(PATH))} total words")
        print("--------- Character Count -------")
        for i in dict_sorter(count_chars(get_book_text(PATH))):
            if i["char"].isalpha():
                print(f"{i["char"]}: {i["num"]}")
        print("============= END ===============")

