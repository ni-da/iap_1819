x = int(input())


def berekenFac(x):
    fac = 1
    for i in range(x):
        fac *= i + 1
    return fac


sum = 0
for i in range(x):
    sum += berekenFac(i + 1)
print(sum)
