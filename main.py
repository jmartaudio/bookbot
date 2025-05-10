
def main():
    from stats import get_num_words
    from stats import make_pretty
    num_words  = get_num_words()
    prett_list = make_pretty()
    print(f"Found {num_words} total words")
    for items in prett_list:
        print(items)

if __name__ == "__main__":
    main()
