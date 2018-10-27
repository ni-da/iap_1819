a = -1
b = 1

x = 1
y = 1
counter = 0
while counter < 5:
    counter += 1

# for i in (-1, 1):
#     print(x + i, y + i)
#
# for i in (-1, 1):
#     print(x, y + i)
#
# for i in (-1, 1):
#     print(x + i, y)
#
# for j in range(3):
#     for i in (-1, 1):
#         if j == 0:
#             print(x + i, y + i)
#         elif j == 1:
#             print(x, y + i)
#         elif j == 2:
#             print(x + i, y)

print(x + 1, y - 1)
print(x - 1, y + 1)
for i in (1, -1, -1, 1):
    print(x + i, y + i)
