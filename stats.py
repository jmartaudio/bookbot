from typing import Counter


filepath = "./books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        contents = f.read()
        return contents

def get_num_words():
    contents = get_book_text(filepath)
    word_list = contents.split()
    num_words = len(word_list)
    return num_words

def get_num_characters():
    raw_text = get_book_text(filepath)
    lc_text = raw_text.lower()
    characters = list(lc_text)
    num_characters = Counter(characters)
    return num_characters


