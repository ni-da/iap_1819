def make_tuple(i, j):
    return "(" + str(i) + "," + str(j) + ")"


l1 = [make_tuple(i, j)
      for i in range(10) if i % 2 == 1
      for j in range(10) if j % 2 == 0 or i % 3 == 0]

print(l1)


tup_list = []
for i in range(10):
    if i % 2 == 1:
        for j in range(10):
            if j % 2 == 0 or i % 3 == 0:
                tup_list.append(make_tuple(i,j))

print(tup_list == l1)