import sys


def get_number(s):
    s = s.split(":")
    s = (s[len(s) - 1])
    if s.isdigit():
        return int(s)
    else:
        print("Identifiers should be numeric.")
        sys.exit()


def get_name(s):
    s = s[::-1]
    pos = s.find(":")
    s = (s[pos + 1:])
    s = s[::-1]
    return str(s)


def local_min(numbersList):
    min_list = []
    i = 0
    while i < len(numbersList):
        if i == 0:
            if get_number(numbersList[i]) < get_number(numbersList[i + 1]):
                min_list.append(numbersList[i])
        elif i == (len(numbersList)) - 1:
            if get_number(numbersList[i]) < get_number(numbersList[i - 1]):
                min_list.append(numbersList[i])
        else:
            if get_number(numbersList[i]) < get_number(numbersList[i - 1]) and get_number(numbersList[i]) < get_number(
                    numbersList[i + 1]):
                min_list.append(numbersList[i])
        i += 1
    return min_list


def local_max(numbersList):
    max_list = []
    i = 0
    while i < len(numbersList):
        if i == 0:
            if get_number(numbersList[i]) > get_number(numbersList[i + 1]):
                max_list.append(numbersList[i])
        elif i == (len(numbersList)) - 1:
            if get_number(numbersList[i]) > get_number(numbersList[i - 1]):
                max_list.append(numbersList[i])
        else:
            if get_number(numbersList[i]) > get_number(numbersList[i - 1]) and get_number(numbersList[i]) > get_number(
                    numbersList[i + 1]):
                max_list.append(numbersList[i])
        i += 1
    return max_list


if len(sys.argv) < 2:
    print("No input provided.")
else:
    list = sys.argv[1:]
    while len(list) > 1:
        # print min
        list = local_min(list)
        print("min ", end="")
        for j in list:
            print(j, end=' ')
        print()
        if len(list) <= 1:
            break
        # print max
        list = local_max(list)
        print("max ", end="")
        for j in list:
            print(j, end=' ')
        print()
    print("Inhabitant", get_name(list[0]), "(id:", str(get_number(list[0])) + ") is the new Monarch")

# input_list = list = sys.argv[1:]
# prev_ele = ''
# for a in range(len(input_list)):
#     curr_ele = input_list[a]
#     # print(curr_ele)
#     if a != len(input_list) - 1:
#         next_ele = input_list[a + 1]
#     if a == 0:
#         if curr_ele < next_ele:
#             pass
#             print(curr_ele)
#     else:
#         print(prev_ele, curr_ele, next_ele)
#         print(prev_ele.split(":")[1], curr_ele.split(":")[1], next_ele.split(":")[1])
#         if prev_ele.split(":")[1] > curr_ele.split(":")[1] < next_ele.split(":")[1]:
#             print(curr_ele)
#
#     prev_ele = curr_ele
#
