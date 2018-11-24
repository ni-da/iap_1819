def partition(alist, first, last):
    pivotValue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotValue:
            leftmark = leftmark + 1
        while alist[rightmark] >= pivotValue and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


def quickSortHelper(alist, first_index, last_index):
    print(alist, first_index, last_index)
    if first_index < last_index:
        print(alist, first_index, last_index, "true")
        splitPoint = partition(alist, first_index, last_index)
        quickSortHelper(alist, first_index, splitPoint - 1)
        quickSortHelper(alist, splitPoint + 1, last_index)


def quicksort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quicksort(alist)
print(alist)
