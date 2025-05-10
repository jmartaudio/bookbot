
def main():
    from stats import get_num_words
    from stats import get_num_characters
    num_words  = get_num_words()
    num_characters = get_num_characters()
    print(f"{num_words} words found in the document")
    print(num_characters)

if __name__ == "__main__":
    main()
