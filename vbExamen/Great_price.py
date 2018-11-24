def great_price(list):
    allowed_sum = 735.61
    tot_sum = 0
    list_pro = []
    while tot_sum < allowed_sum:
        for i in list:
            for j in range(2):
                temp_sum = tot_sum + i
                if temp_sum <= allowed_sum:
                    tot_sum += i
                    list_pro.append(i)
    return list_pro


a = [400, 200, 50]
b = great_price(a)
print(b)
