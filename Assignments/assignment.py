import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

for i in range(a, b + 1):
    counter = 0
    for j in range(c + 1):
        print(i ** j, " ", end="", sep="")
        counter += i ** j
    print("sum ", counter, end="", sep="")
    counter = 0
    print()
