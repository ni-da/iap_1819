a = ['a', 'b', 'c', 'd', 'e']


def reverse_list(old_ls, new_ls=[]):
    if 0 == len(old_ls):
        return
    else:
        new_ls.append(old_ls.pop(len(old_ls) - 1))
        reverse_list(old_ls, new_ls)
    return new_ls


print(reverse_list(a))
# new_list = []
# couter = len(a) - 1
# while couter >= 0:
#     new_list.append(a[couter])
#     couter -= 1
#
# print(new_list)
