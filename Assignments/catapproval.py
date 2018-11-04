import sys, ast


def list_avg(nested_num_list):
    tot = 0
    for element in nested_num_list:
        if type(element) == type([]):
            tot += list_avg(element)
        else:
            tot += int(element)
    return int(tot // len(nested_num_list))


a = sys.argv[1]
b = ""
for i in range(1, len(a) - 1):
    b += a[i]
b = ast.literal_eval(b)

print("Average approval rate is", list_avg(b))
