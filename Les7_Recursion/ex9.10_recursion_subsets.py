def sub_sets(list):
    return sub_sets_recur([], list)


def sub_sets_recur(current, subset):
    if len(subset) == 0:
        return [current]
    else:
        return sub_sets_recur(current, subset[1:]) + \
               sub_sets_recur(current + [subset[0]], subset[1:])


# data = [4, 5, 6]
data = (input().split())
print(data)
new_data = sub_sets(data)
for i in new_data:
    for j in i:
        print(j, end=" ")
    print()
