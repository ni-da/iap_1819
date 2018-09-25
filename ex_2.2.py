# Write a program that asks for a value x and writes the following
# list (x = 7):
# 1 2 3 4 5 6 7
# The output of your program should exactly match the output given above.

x = int(input("x: "))
for i in range(x):
    print(i+1, end=" ")