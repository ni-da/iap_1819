def is_ordered(a):
    sorted = True
    # prev_value = a[0]
    # next_value = a[1]
    for i in range(len(a) - 1):
        prev_value = a[i]
        next_value = a[i+1]
        if not (prev_value <= a[i] <= next_value):
            sorted = False
            break
        # prev_value = a[i]
        # next_value = a[i + 1]
    return sorted


a = [1, 2, 3, 4, 5, 6, 7, 9, 8]

print(is_ordered(a))
