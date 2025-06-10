# stats file for functions
from collections import defaultdict


def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        return f.read()


def get_num_words(filepath: str) -> int:
    text = get_book_text(filepath)
    return len(text.split())


def get_num_characters(filepath: str) -> dict:
    text = get_book_text(filepath).lower()
    count = defaultdict(int)
    for c in text:
        count[c] += 1
    return count


def get_sorted_dict(count: dict) -> dict:
    sorted_count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))

    return sorted_count
