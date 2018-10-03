def find_occurrences(pattern, s):
    newStr = ""
    for i in range(len(s)):
        patternCounter = 0
        if s[i] == pattern[0]:
            while patternCounter < len(pattern):
                if (s[i + patternCounter] != pattern[patternCounter]):
                    break
                patternCounter += 1
        if patternCounter == len(pattern):
            newStr += str(i) + ","

    print(newStr)


s = "It is. oky to it is."
pattern = "t is"
find_occurrences(pattern, s)

# print(s.find(pattern, 3))
