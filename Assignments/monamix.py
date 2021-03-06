import sys


def get_number(a):
    splitted = a.split(':')
    number = (splitted[len(splitted) - 1])
    if number.isdigit():
        return int(number)
    else:
        print("Identifiers should be numeric.")
        sys.exit()


def get_name(s):
    s = s[::-1]
    pos = s.find(":")
    s = (s[pos + 1:])
    s = s[::-1]
    return str(s)


def filter_min(numbersList):
    new_list = []
    i = 0
    while i < len(numbersList):
        if i == 0:
            if get_number(numbersList[i]) < get_number(numbersList[i + 1]):
                new_list.append(numbersList[i])
        elif i == (len(numbersList)) - 1:
            if get_number(numbersList[i]) < get_number(numbersList[i - 1]):
                new_list.append(numbersList[i])
        else:
            if get_number(numbersList[i]) < get_number(numbersList[i - 1]) and get_number(numbersList[i]) < get_number(
                    numbersList[i + 1]):
                new_list.append(numbersList[i])
        i += 1
    return new_list


def filter_max(numbersList):
    new_list = []
    i = 0
    while i < len(numbersList):
        if i == 0:
            if get_number(numbersList[i]) > get_number(numbersList[i + 1]):
                new_list.append(numbersList[i])
        elif i == (len(numbersList)) - 1:
            if get_number(numbersList[i]) > get_number(numbersList[i - 1]):
                new_list.append(numbersList[i])
        else:
            if get_number(numbersList[i]) > get_number(numbersList[i - 1]) and get_number(numbersList[i]) > get_number(
                    numbersList[i + 1]):
                new_list.append(numbersList[i])
        i += 1
    return new_list


if len(sys.argv) < 2:
    print("No input provided.")
else:
    list = sys.argv[1:]
    while len(list) > 1:
        list = filter_min(list)
        print("min ", end="")
        for j in list:
            print(j, end=' ')
        print()
        if len(list) <= 1:
            break
        list = filter_max(list)
        print("max ", end="")
        for j in list:
            print(j, end=' ')
        print()
    print("Inhabitant", get_name(list[0]), "(id:", str(get_number(list[0])) + ") is the new Monarch")
