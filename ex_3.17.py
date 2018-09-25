import random

x = int(input("x: "))
y = int(input("y: "))

nr = random.randrange(x, y+1)
print(nr)

g = int(input("g: "))
while g != nr:
    if nr < g:
        print("LOWER!")
    elif nr > g:
        print("HIGHER!")
    g = int(input("g: "))
print("YESSS!!!!")