def fibonacci_values(i):
    ls = [0, 1]
    for f in range(0, i-2):
        prev_value1 = ls[f]
        prev_value2 = ls[f + 1]
        ls.append(prev_value1 + prev_value2)
    return ls


print(fibonacci_values(7))
