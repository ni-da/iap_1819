def is_heap(list):
    for i in range(len(list)):
        if type(list[i]) == type([]):
            print((list[i]))
            if len(list[i]) > 2:
                return False
            for e in list[i]:
                if list[i - 1] < e:
                    return False
    return True



a = is_heap([7, [4], [6, [5, [3]], [4]]])
print(a)
