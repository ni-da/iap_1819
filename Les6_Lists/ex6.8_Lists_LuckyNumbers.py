def lucky_numbers(n):
    a = [x for x in range(1, n + 1)]
    step = 2
    while len(a) >= step:
        filtered_list = [a[i - 1] for i in range(len(a) + 1) if i % step != 0]
        step += 1
        a = filtered_list
    return a

print(lucky_numbers(15))