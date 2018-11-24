counter = 0


def height(lst):
    global counter
    for i in lst:
        if type(i) == type([]):
            height(i)
        else:
            counter += 1
    return counter


list = [0]
a = height(list)
counter = counter - (len(list) - 1)

print(counter)
