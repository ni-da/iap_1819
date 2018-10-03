def cleanup_spaces(s):
    prevChar = ""
    recentChar = ""
    newstr = ""
    for i in range(len(s)):
        prevChar = s[i-1]
        recentChar = s[i]
        # print(prevChar)
        if prevChar == " " and recentChar == " ":
            newstr = s[:i] + s[i+1:]
            print(newstr)
    print(newstr)

cleanup_spaces("A  simple  example  string  !")