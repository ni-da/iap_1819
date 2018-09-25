x = 5

# counter = 9
# for j in range(5):
#     # print(j + counter)
#     for i in range(j+counter):
#         print("*", end="")
#
#     counter -= 3
#     print()

for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(1, x):
    for j in range(1, x - i + 1):
        print(j, end=" ")
    print()
