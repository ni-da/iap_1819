l = [0, 1, 2, 3, 4, 5]
n = 1

m = [i * 0 for i in range(6)]

for i in range(len(l)):
    pos = (i + 2) % len(l) - 1

    m[pos] = l[i]

print(m)
