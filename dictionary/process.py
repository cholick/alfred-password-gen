words = {}
with open("2of12inf.txt", "r") as words_file:
    lines = words_file.readlines()
    for word in lines:
        word = word.strip("\n%!")
        word_len = len(word)
        if 3 < word_len < 14:
            words[word_len] = words.get(word_len, []) + [word]

with open("processed.py", "w") as process_words_file:
    process_words_file.write("words = ")
    process_words_file.write(str(words))
