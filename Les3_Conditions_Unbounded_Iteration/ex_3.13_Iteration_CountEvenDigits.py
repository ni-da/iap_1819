a = int(input())

counter = 0
for i in str(a):
    if int(i) % 2 == 0:
        counter += 1

print(counter)
