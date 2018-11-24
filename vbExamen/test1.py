def substring(s, x, y):
    new_str = ""
    for i in range(y):
        new_str += s[(i + x) % len(s)]
    return new_str


def count_words(string, word):
    word_count = 0
    s = 0
    while len(string) > 0:
        if string[s] == word[s]:
            ss = substring(string, s, len(word))
            if ss == word:
                word_count += 1
                string = string[s + len(word):]
            else:
                s += 1
        else:
            s += 1

    print(word_count)


count_words("abcabcaaaabc", "abc")
