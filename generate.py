import json
import random
import sys
import secrets

from dictionary.processed import words

MIN_LENGTH = 10
MAX_LENGTH = 35
DEFAULT_LENGTH = 16
MIN_WORD_LEN = 4
SPECIAL_CHARS = '!@#$%^&*()-_=+"\',./\\:;{}~'


def get_word(length: int) -> str:
    word_options = words[length]
    word = word_options[secrets.randbelow(len(word_options))]

    caps_chance = random.random()
    # low chance of all-caps, but just for shorter words
    if caps_chance > .9 and len(word) < 9:
        word = word.upper()
    elif caps_chance > .45:
        word = word.capitalize()

    return word


def get_word_lengths(total_length: int) -> [int]:
    min_word_length = 4
    max_word_length = 13
    lengths = []
    remaining = total_length
    while remaining >= min_word_length:
        length = random.randint(min_word_length, min(max_word_length, remaining))
        if remaining - length < min_word_length:
            if remaining > max_word_length:
                continue
            else:
                length = remaining
        lengths.append(length)
        remaining -= length

    # try again if we ended up with just one word
    if len(lengths) == 1:
        lengths = get_word_lengths(total_length)
    return lengths


def generate(length: int) -> [str]:
    number_count = 1 + secrets.randbelow(int(length * .2))
    symbol_count = 1 + secrets.randbelow(int(length * .1))
    word_lengths = get_word_lengths(length - symbol_count - number_count)

    components = []

    for word_length in word_lengths:
        components.append(get_word(word_length))
    for i in range(0, number_count):
        components.append(str(secrets.randbelow(10)))
    for i in range(0, symbol_count):
        components.append(SPECIAL_CHARS[secrets.randbelow(len(SPECIAL_CHARS))])

    random.shuffle(components)

    return "".join(components)


def validated_input() -> int:
    try:
        query = int(sys.argv[1])
        if query < MIN_LENGTH or query > MAX_LENGTH:
            return -1
        else:
            return query
    except:
        return -1


def main(args: list) -> dict:
    length = DEFAULT_LENGTH
    if len(args) > 0:
        length = validated_input()
        if length < 0:
            return {"items": [{
                "title": f"Invalid input; if supplied, arg must be a number between {MIN_LENGTH} and {MAX_LENGTH}",
                "valid": False,
            }]}

    passwords = []
    for i in range(0, 8):
        password = generate(length)
        passwords.append({
            "title": password,
            "arg": password,
        })

    return {"items": passwords}


if __name__ == "__main__":
    output = main(sys.argv[1:])

    sys.stdout.write(json.dumps(output))
