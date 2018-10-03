def encode(s, n):
    newstr = ""
    for i in range(len(s)):
        charCode = ord(s[i]);
        if charCode >= 97 and charCode <= 122 or charCode >= 65 and charCode <= 90:
            newChrCode = charCode + n % 26
        else:
            newChrCode = charCode

        newstr += chr(newChrCode)

        # print(chr(newChrCode), end="")
    print(newstr)


encode("alphabet: from a to z", 33)
