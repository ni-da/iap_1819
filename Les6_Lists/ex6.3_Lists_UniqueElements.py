def is_unique(l):
    unique = True
    for i in l:
        counter = 0
        for j in l:
            if i == j:
                if counter == 0:
                    counter += 1
                else:
                    unique = False
                    break
    return unique


print(is_unique([1, 2, 3, 4, 5, 6, 7, 1, 9]))
print(is_unique(["z", "q", "b", "c", "h", "m", "p", "l", "a"]))
