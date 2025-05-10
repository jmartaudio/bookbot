
def main():
    from stats import get_num_words
    num_words  = get_num_words()
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()
