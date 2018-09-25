def replace(pattern, replace, corpus):
    newstr = ""
    for i in range(len(corpus)):
        strCounter = i
        if corpus[i] == pattern[0]:
            for p in range(len(pattern)):
                if pattern[p] == corpus[strCounter+p]:
                    print(pattern[p], "=",corpus[strCounter+p])
                    newstr = corpus[:strCounter]+replace+ corpus[strCounter+len(pattern):]
    print(newstr)


replace("with", "for", "I play with a sentence")
