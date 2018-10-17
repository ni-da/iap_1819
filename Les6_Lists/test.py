def do(list):
    for i in range(len(list) - 1):
        for j in range(i + 1, len(list)):
            if list[j] == list[j]:
                return False

    return True


print(do([5,1, 2, 3, 5, 6, 2]))
