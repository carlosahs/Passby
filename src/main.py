import math
import random
from typing import List

# constants
DIGITS = [str(i) for i in range(10)]
LOWER_CASES = [
    'a', 'b', 'c', 'd', 'e',
    'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y',
    'z'
]
UPPER_CASES = [l.upper() for l in LOWER_CASES]
SYMBOLS = [
    '!', '@', '#', '$', '%',
    ')', '(', '*', '&', '^',
    '[', ']', ';', '.', ':',
    '/', '?', '-', '=', '+',
    '<', '>', '|', '~', '_',
    ','
]
CHAR_TYPES = {
    "digits": DIGITS,
    "lowercases": LOWER_CASES,
    "uppercases": UPPER_CASES,
    "symbols": SYMBOLS,
}


def compute_splits(n:int) -> List[int]:
    """
    Splits an integer into 4 integers that sum up to the
    integer

    :param n: Integer to split
    :returns: List containing the 4 resulting integers
    """
    higher_part = math.ceil(n / 2)
    lower_part = math.floor(n / 2)

    s1 = math.ceil(higher_part / 2) + 1
    s2 = math.floor(higher_part / 2)
    s3 = math.ceil(lower_part / 2)
    s4 = math.floor(lower_part / 2) - 1

    return [s1, s2, s3, s4]


def compute_password(n:int) -> str:
    """
    Computes a password of length n

    :param n: Length of the password
    :returns password: Computed password
    """
    splits = compute_splits(n)

    # randomly assign a split to each char type
    random.shuffle(splits)
    char_keys = list(CHAR_TYPES.keys())  # get key list
    chars = {
        char_keys[i]: splits[i]
        for i in range(len(CHAR_TYPES))
    }

    password = ""
    for _ in range(n):
        char_type = random.choice(char_keys)

        password += random.choice(CHAR_TYPES[char_type])

        chars[char_type] -= 1
        if chars[char_type] == 0:
            chars.pop(char_type)
            char_keys.remove(char_type)

    return password


if __name__ == '__main__':
    password = compute_password(12)
    print(password)