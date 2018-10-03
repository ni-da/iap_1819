# Write a function that checks whether a list of numbers is ordered.

l = [1, 6, 5, 8, 2]
o = [1, 2, 2, 4, 6, 9]


def isOrders(list):
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            print("Not orderd")
            exit()
    print("Orderd!")


isOrders(o)
