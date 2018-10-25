def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        ackermann(m - 1, 1)
    elif n > 0 and m > 0:
        ackermann(m - 1, ackermann(m, n - 1))


ackermann(3, 6)
