from typing import Counter
import sys

if len(sys.argv) <2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath, 'r') as f:
        contents = f.read()
        return contents

def get_num_words():
    contents = get_book_text(filepath)
    word_list = contents.split()
    num_words = len(word_list)
    return num_words

def remove_non_letters(input_string):
    letters_only = ''.join(char for char in input_string if char.isalpha())
    return letters_only

def get_num_characters():
    raw_text = get_book_text(filepath)
    lc_text = raw_text.lower()
    lc_text = remove_non_letters(lc_text)
    characters = list(lc_text)
    num_characters = Counter(characters)
    return num_characters

def make_pretty():
    num_characters = get_num_characters()
    sorted_items = sorted(num_characters.items(), key=lambda item: item[1], reverse=True)
    pretty_list = [f"{key}: {value}" for key, value in sorted_items]
    return pretty_list
