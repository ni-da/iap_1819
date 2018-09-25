x = int(input())
y = int(input())

counter = 1
for j in range(y):
    for i in range(x):
        print(counter, end=" ")
        counter += 1
    print()
