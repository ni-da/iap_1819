x = int(input())


def cal_doub_sum(x):
    double_sum = 0
    for i in range(1, x + 1):
        for j in range(1, i+1):
            double_sum += j
    return double_sum


print(cal_doub_sum(x))
