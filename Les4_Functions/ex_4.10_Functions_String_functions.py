def substring(s, x, y):
    new_str = ""
    for i in range(y):
        new_str += s[(i + x) % len(s)]
    return new_str


def find_pos(word, s):
    counter = 0
    while counter < len(s):
        if s[counter] == word[0]:
            ss = substring(s, counter, len(word))
            if ss == word:
                return counter
        counter += 1
    return None


def in_string(word, s):
    if find_pos(word, s) is not None:
        return True
    return False


# print(find_pos("with", "a sentence with words"))

# print(in_string("with", "a sentence with words"))

print(in_string("en", "a sentence with words"))
