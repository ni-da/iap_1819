def replace(pattern, replacement, corpus):
    i = 0
    while i < len(corpus):
        if corpus[i] == pattern[0]:  # same 1st char as pattern
            if match_strings(pattern, corpus[i:]):
                corpus = corpus[0:i] + replacement + corpus[i + len(pattern):]

        i += 1
    return corpus

def match_strings(pattern, s2):
    same = True
    counter = 0
    while counter < len(pattern):
        if pattern[counter] != s2[counter]:
            same = False
            break
        counter += 1
    return same


replace("with", "for", "I play with a sentence without words")
