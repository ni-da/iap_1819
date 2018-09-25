m = int(input())
for i in [200, 100, 50, 20, 10, 5, 2, 1]:
    coins = m // i
    m = m - (coins * i)
    if i > 50:
        print(i // 100, "-euros: ", coins, sep="")
    else:
        print(i, "c-euros: ", coins, sep="")
