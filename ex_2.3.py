# Assume you have a list of numbers = [12, 10, 32, 3, 66,
# 17, 42, 99, 20].

# (a) Write a loop that writes each of the numbers on a separate line.

numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]

ex = input("a, b: ")
for i in numbers:
    if ex == "a":
        print(i)
    elif ex == "b":
        print(i, ": ", i * i)

