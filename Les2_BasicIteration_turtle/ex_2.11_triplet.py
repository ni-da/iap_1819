p = ["A", "C", "G", "T"]

# counter = 0
# for i in p:
#     for j in p:
#         for k in p:
#             print(i, j, k, sep="")
#     print()
#
# print(counter)

counter = 0
while counter < 4:
    for i in p:
        print(p[counter], i, sep="")
    counter += 1
