import json
import random
import sys
import secrets

from dictionary.processed import words

MIN_LENGTH = 10
MAX_LENGTH = 25
DEFAULT_LENGTH = 15
MIN_WORD_LEN = 4
SPECIAL_CHARS = '!@#$%^&*()-_=+"\',./\\:;{}~'


def debug(*args):
    print(*args, file=sys.stderr)


def get_word(length: int) -> str:
    word_options = words[length]
    word = word_options[secrets.randbelow(len(word_options))]
    if secrets.randbelow(2):
        word = word.capitalize()

    return word


def generate(length: int) -> [str]:
    number_count = 1 + secrets.randbelow(int(length * .15))
    symbol_count = 1

    remaining_len = length - symbol_count - 2 * MIN_WORD_LEN - number_count
    word1_extra = secrets.randbelow(remaining_len + 1)
    word1_len = MIN_WORD_LEN + word1_extra
    word2_len = MIN_WORD_LEN + remaining_len - word1_extra

    word1 = get_word(word1_len)
    word2 = get_word(word2_len)

    components = []
    for i in range(0, number_count):
        components.append(str(secrets.randbelow(10)))
    components.append(word1)
    components.append(word2)
    random.shuffle(components)
    components.insert(
        1 + secrets.randbelow(len(components) - 1),
        SPECIAL_CHARS[secrets.randbelow(len(SPECIAL_CHARS))]
    )

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
    # debug("returning", output)

    sys.stdout.write(json.dumps(output))
