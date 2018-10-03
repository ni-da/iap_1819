def is_good(i):
    return (i ** 3) % 2 == 0

l1 = []
for i in range(1, 100):
    if is_good(i):
        l1.append((i ** 2) - 1)

print(l1)



L = [(i ** 2) - 1 for i in range(1, 100) if (i ** 3) % 2 == 0]
print(L)
