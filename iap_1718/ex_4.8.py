m = 6
n = 4

for i in range(1, m + 1):
    res = 1
    for j in range(1, n+1):
        res = res*i
        print(res, end=" ")
    print()
