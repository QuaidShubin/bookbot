from stats import get_num_words, get_num_characters
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    char_count = get_num_characters(path)
    word_count = get_num_words(path)
    output = f"""
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count} total words
--------- Character Count -------
"""

    for c, v in char_count.items():
        if not c.isalpha():
            continue
        output += f"\n{c}: {v}"
    output += "\n============= END ==============="
    print(output)


if __name__ == "__main__":
    main()
