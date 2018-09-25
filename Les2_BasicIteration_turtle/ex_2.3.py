import math

numbers = [12, 10, 32, 3, 66,
           17, 42, 99, 20]

# (a) Write a loop that writes each of the numbers on a separate line.
for i in numbers:
    print(i)

# (b) Adjust the loop in such a way that it writes each number and its square on a separate line.
for i in numbers:
    print(i, i * i)

print("--- C ---")
# (c) Adjust your program in such a way that the sum of the original numbers
# and the sum of their squares are written out at the bottom.
sumNr = 0
sumSqr = 0
for i in numbers:
    print(i, i * i)
    sumNr += i
    sumSqr += i * i
print("---------")
print(sumNr, sumSqr)

print("--- D ---")
# (d) Adjust your program in such a way that the product of the original numbers
# is written out at the bottom.
proNr = 1
sumSqr = 0

for i in numbers:
    print(i, i * i)
    proNr *= i
    sumSqr += i * i

print("---------")
print(proNr, sumSqr)
