list_int = int(input())
list = [i for i in range(1, list_int + 1)]
n = int(input())


def subsets(list, n):
    list_len = len(list)
    subsets_recv(list, "", list_len, n)


def subsets_recv(lst, prefix, lst_len, n):
    if n == 0:
        print(prefix)
        return
    for i in range(lst_len):
        new_prefix = str(prefix) + str(lst[i])
        subsets_recv(lst, new_prefix, lst_len, n - 1)


def combos(list, n):
    list_len = len(list)
    rec_combos(list, "", n)


def rec_combos(list, prefix, n):
    if n == 0:
        print(prefix)
        return
    for i in range(len(list)):
        new_prefix = str(prefix) + str(list[i])
        rec_combos(list, new_prefix, n - 1)


combos(list, n)
subsets(list, n)
