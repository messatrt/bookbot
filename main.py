def main():
    path = "./books/frankenstien.txt"
    book = get_book(path)
    print(book)

def get_book(path):
    with open(path) as f:
        return f.read()
    
main()