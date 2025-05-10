
def get_book_text(filepath):
    with open(filepath, 'r') as f:
        contents = f.read()
        return contents

def get_num_words():
    contents = get_book_text("./books/frankenstein.txt")
    word_list = contents.split()
    num_words = len(word_list)
    return num_words
