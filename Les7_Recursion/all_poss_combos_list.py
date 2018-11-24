def perm(lst):
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [lst]
    else:
        new_list = []
        for i in range(len(lst)):
            x = lst[i]
            xs = lst[:i] + lst[i + 1:]
            for p in perm(xs):
                e = [x] + p
                new_list.append(e)
        return new_list


data = ['a', 'b', 'c']
new_lst = perm(data)
print(new_lst)
