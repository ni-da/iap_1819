w = input()
a = "abcdefghijklmnopqrstuvwxyz"

counter = 0
for i in a:
    for j in w:
        if i == j:
            counter += 1
    print(i, ": ", counter, sep="")
    counter = 0
