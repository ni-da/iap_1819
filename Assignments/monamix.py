import sys


def get_list_from_input(inputt):
    ls = []
    for i in range(1, len(inputt)):
        ls.append(inputt[i])
    return ls


def get_number(a):
    splitted = a.split(':')
    number = splitted[1]
    return number


def filter_min(old_list):
    new_list = []
    return new_list


def filter_max(old_list):
    new_list = []
    return new_list


input_list = get_list_from_input(sys.argv)
prev_ele = ''
for a in range(len(input_list)):
    curr_ele = input_list[a]
    # print(curr_ele)
    if a != len(input_list) - 1:
        next_ele = input_list[a + 1]
    if a == 0:
        if curr_ele < next_ele:
            pass
            print(curr_ele)
    else:
        print(prev_ele, curr_ele, next_ele)
        if prev_ele > curr_ele < next_ele:
            print(curr_ele)

    prev_ele = curr_ele
