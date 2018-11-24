def check_length(string, n, m):
    if len(string) >= n * m:
        return True
    return False


def substring(string, frm, y):
    new_str = ""
    for i in range(y):
        new_str += string[(i + frm) % len(string)]
    return new_str


def count_words(string, word):
    word_count = 0
    s = 0
    while len(string) > 0 and s < len(string) - 1:
        if string[s] == word[0]:
            ss = substring(string, s, len(word))
            if ss == word:
                word_count += 1
                string = string[s + len(word):]
            else:
                string = string[s:]
                s += 1
        else:
            string = string[s:]
            s += 1
    return word_count


def has_repetition(string, n, m):
    if not check_length(string, n, m):
        return False
    match_prefix = string[:n]
    if count_words(string, match_prefix) >= m:
        return True
    return False


a = has_repetition("abcabcaaaabc", 3, 3)
print(a)
