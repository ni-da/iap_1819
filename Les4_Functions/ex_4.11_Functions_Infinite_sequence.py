string = "word"
index = -3
length = 9


def create_sequence(string, index, length):
    smaller_index_str = string[index + 1:]
    # new_string = smaller_index_str
    new_string = ""
    len_new_str = len(new_string)
    # add the chars  of word
    # add reverse chars
    # add more word chars
    while len_new_str < length:
        # add word chars
        for s in string:
            if len(new_string) < length:
                # new_string += s
                new_string += "w"
        for i in string:
            if len(new_string) < length:
                # new_string += i
                new_string += "e"
        len_new_str = len(new_string)
    return new_string


print(create_sequence("word", -5, 15))
