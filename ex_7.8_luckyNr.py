def findLuckyNr(n):
    L = [i + 1 for i in range(n)]
    n = []
    print(L)
    del L[1::2]
    print(L)
    del L[::3]
    print(L)

    # for i in range(len(L)):
    #     if i % 2 == 0:
    #         n.append(L[i])
    # print(n)
    #
    # del n[1::3]
    # print(n)

    #
    # for i in range(len(n)):
    #     if i ==
    #         print(i)
    #     # if i != i + 3:
    #     #     print(n[i])


findLuckyNr(22)
