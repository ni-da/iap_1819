def convert_to_uppercase(s):
    codeA = ord('a') - ord('A')
    new_str = ""
    for i in s:
        if not ('a' <= i <= 'z'):
            new_str += i
        else:
            value = ord(i) - codeA
            new_str += chr(value)
    return new_str


print(convert_to_uppercase("a NicE mIX of LeTterS"))
