# nr = 5
#
# result = 1
# for i in range(1, nr + 1):
#     print(i)
#     result *= i
#
# print(result)


def fac(nr):
    res = 1
    if nr == 1:
        return 1
    else:
        # print(nr)
        # res *= fac(nr - 1)
        return nr * fac(nr - 1)
    # return res


print(fac(5))
