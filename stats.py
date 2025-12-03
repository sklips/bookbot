def count_words(text):
    return len(text.split())



def count_chars(text):
    chars = {}
    for char in text.lower():
        chars[char] = chars.get(char, 0) + 1
    return chars

def dict_sorter(char_dict):
    dicts = []
    for char, value in char_dict.items():
        dicts.append({"char": char,"num":value})
        dicts.sort(reverse=True,key=lambda x: x["num"])
    return dicts

