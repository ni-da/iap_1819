list = []
a = 0
b = 1
list.append(a)
list.append(b)
for i in range(10):
    c = a + b
    a = b
    b = c
    list.append(c)

print(list)
