from stats import get_num_words, get_num_characters


def main():
    count = get_num_characters("./books/frankenstein.txt")
    print(count)


if __name__ == "__main__":
    main()
