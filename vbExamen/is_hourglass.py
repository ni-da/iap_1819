def check_words(w1, w2):
    if len(w1) != len(w2) - 1:
        return False
    chars_list = [i * 0 for i in range(26)]
    for w in w1:
        index = ord(w) - ord('a')
        chars_list[index] += 1
    for w in w2:
        index = ord(w) - ord('a')
        chars_list[index] -= 1
    counter = 0
    for i in chars_list:
        if i == 0:
            counter += 1
    if counter != 25:
        return False
    return True


def is_hourglass(words):
    for i in range(len(words) - 1):
        if not check_words(words[i], words[i + 1]):
            return False
    return True


wordss = ["a",
          "aa",
          "abb",
          "aabb",
          "aaabbb"]
print(is_hourglass(wordss))
