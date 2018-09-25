x = int(input())
y = int(input())


def berekenFac(x):
    proX = 1
    for i in range(x):
        proX *= i + 1
    return proX


r = int(berekenFac(x) / (berekenFac(y) *
                         berekenFac(x - y)))
print(r)
