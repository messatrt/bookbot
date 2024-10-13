def main():
    book_path = "./books/frankenstien.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    words = get_char_count(text)
    #print(words)
    list = dict_to_list(words)
    list.sort(reverse=True,key=sort_on)
    for i in list:
        print(f"The '{i["char"]}' character was found {i["count"]} times")
    print("-- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_count(text:str):
    char_dict = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_dict:
            char_dict[lowered] += 1
        else:
            char_dict[lowered] = 1
    return char_dict

def dict_to_list(dict:dict):
    l = []
    for x in dict:
        if x.isalpha():
            d = {"char" : 0, "count" : 0}
            d["char"] = x
            d["count"] = dict[x]
            l.append(d)
    return l

def sort_on(dict:dict):
    return dict["count"]
main()
