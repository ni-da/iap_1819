def strange_order(s, t):
    shortest_length = 0
    if len(s) < len(t):
        shortest_length = len(s)
    else:
        shortest_length = len(t)
    for i in range(shortest_length):
        if i % 2 == 0:
            if s[i] >= t[i]:
                return False
        else:
            if s[i] <= t[i]:
                return False
    return True


print(strange_order("aaaaaaa", "bbbbbbb"))
