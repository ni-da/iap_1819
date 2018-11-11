a = [11, 2, 3, 5, 8], 2


def n_sum(list, n):
    for i in list:
        for j in list:
            if i + j in list:
                print(i, j)


def combinationUtil(arr, n, r, index, data, i):
    if (index == r):
        for j in range(r):
            print(data[j], end=" ")
        print(" ")
        return

    # When no more elements are there to put in data[]
    if (i >= n):
        return

    # current is included, put next at next location
    data[index] = arr[i]
    combinationUtil(arr, n, r,
                    index + 1, data, i + 1)

    # current is excluded, replace it with
    # next (Note that i+1 is passed, but index is not changed)
    combinationUtil(arr, n, r, index,
                    data, i + 1)


n_sum([11, 2, 3, 5, 8], 2)
