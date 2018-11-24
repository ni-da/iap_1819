def remove_chars(w1, w2):
    new_w1 = ""
    new_w2 = ""
    for w in w1:
        if w not in w2:
            new_w1 += w
    for w in w2:
        if w not in w1:
            new_w2 += w
    return new_w1, new_w2


def extract_message(list):
    new_str = ""
    new_w1, new_w2 = "", ""

    for word_index in range(len(list) - 1):
        if word_index == 0:
            new_w1, new_w2 = remove_chars(list[word_index], list[word_index + 1])
        else:
            new_w1, new_w2 = remove_chars(new_w2, list[word_index + 1])
        if word_index == len(list) - 2:
            new_str += new_w1 + new_w2
        else:
            new_str += new_w1

    print(new_str)


extract_message(["axba", "baycb", "czbc"])
