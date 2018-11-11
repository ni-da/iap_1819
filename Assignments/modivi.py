import sys


def is_alpha(a):
    if 'a' <= a <= 'z' or 'A' <= a <= 'Z':
        return True
    return False


a = sys.argv[1].replace("'", "")
prefix = sys.argv[2].replace("'", "")


def brac_uitwerken(a):
    new_word, word_part = "", ""
    first_closeing_brac_index = a.find(")")
    most_inner_open_brac_index = 0
    counter = first_closeing_brac_index

    while counter >= 0:
        if a[counter] == "(":
            most_inner_open_brac_index = counter
            break
        counter -= 1
    binnenste_brac_part = a[most_inner_open_brac_index + 1:first_closeing_brac_index]

    brac_str = (a[a.rfind("(", 0, most_inner_open_brac_index) + 1:most_inner_open_brac_index])
    counter_1 = 0
    ls = ""
    for counter_1 in range(len(binnenste_brac_part)):
        if is_alpha(binnenste_brac_part[counter_1]):
            try:
                if binnenste_brac_part[counter_1 + 1] == "#" and binnenste_brac_part[counter_1 + 2] != "+":
                    word_part += binnenste_brac_part[counter_1]
            except IndexError:
                pass
            new_word += binnenste_brac_part[counter_1]
        elif binnenste_brac_part[counter_1] == "#":
            if word_part == new_word:
                if counter_1 == len(binnenste_brac_part) - 1:
                    ls += (brac_str + new_word + "#")
                else:
                    ls += (brac_str + new_word + "#+")
            else:
                if counter_1 == len(binnenste_brac_part) - 1:
                    ls += (brac_str + word_part + new_word + "#")
                else:
                    ls += (brac_str + word_part + new_word + "#+")
            new_word = ""
            try:
                if binnenste_brac_part[counter_1 + 1] == "+":
                    word_part = ""
            except IndexError:
                pass
        counter_1 += 1
    new_str = a[:most_inner_open_brac_index - len(brac_str)] + ls + a[first_closeing_brac_index + 1:]
    return new_str


def valid_prefix(word, pref):
    pref_counter = 0
    while pref_counter < (len(pref)):
        if word[pref_counter] != pref[pref_counter]:
            return False
        pref_counter += 1
    return True


new_list = []
while a.find("(") != -1:
    a = brac_uitwerken(a)
for i in a.split("#"):
    i = i.replace("+", "")
    i = i.replace("#", "")
    if i not in new_list:
        new_list.append(i)

new_list.pop()

for e in new_list:
    if valid_prefix(e, prefix):
        print(e)
