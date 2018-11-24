def merge_sort(list):
    if len(list) > 1:
        M = len(list) // 2
        L = list[:M]
        R = list[M:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                list[k] = L[i]
                i += 1
            else:
                list[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            list[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            list[k] = R[j]
            j += 1
            k += 1
        return list


l = [8, 1, 5, 7, 2, 4, 6, 9, 10, 3]
print(merge_sort(l))
