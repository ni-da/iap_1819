def replace(pattern, replacement, corpus):
    newSen = ""
    for i in range(len(corpus) - 1):
        if corpus[i] == pattern[0]:  # same 1st char as pattern
            if match_strings(pattern, corpus[i:]):
                corpus = corpus[0:i] + replacement + corpus[i + len(pattern):]
            else:
                newSen += "-"

    print(corpus)
    return newSen


def match_strings(pattern, s2):
    same = True
    counter = 0
    while counter < len(pattern):
        if pattern[counter] != s2[counter]:
            same = False
            break
        counter += 1
    return same


replace("with", "foor", "I play with a sentence without words")
