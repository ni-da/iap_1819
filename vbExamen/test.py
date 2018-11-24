string = "ababab"
matching_str = "ab"
str_list = [i for i in string]
new_list = []


def substring(s, x, y):
    new_str = ""
    for i in range(y):
        new_str += s[(i + x) % len(s)]
    return new_str


def find_pos(word, s):
    counter = 0
    while counter < len(s):
        if s[counter] == word[0]:
            ss = substring(s, counter, len(word))
            if ss == word:
                return counter
        counter += 1
    return None


# i = 0
# counter = 0
# while i < len(str_list):
#     if str_list[i] == matching_str[0]:
#         for m in range(len(matching_str)):
#             if str_list[i + m] != matching_str[m]:
#                 break
#         counter += 1
#     i += 1
# print(counter)


def count_words(string, word):
    word_count = 0
    s = 0
    while s < len(string):
        if string[s] == word[0]:
            ss = substring(string, s, len(word))
            if ss == word:
                word_count += 1
                string = string[s + len(word):]
        s += 1
    print(word_count)


count_words("abcabcaaaabc", "abc")
