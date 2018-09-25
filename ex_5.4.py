def print_word_len(s):
    ss = s.split()
    for i in ss:
        print(i, len(i))


print_word_len("Python! programming .... ROCKS")