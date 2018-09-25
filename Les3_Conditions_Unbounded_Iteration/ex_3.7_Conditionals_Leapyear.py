X = int(input())

m = "is not a leap year"

if X % 4 == 0 and (X % 100 != 0 or X % 400 == 0):
    m = "is a leap year"
else:
    m = "is not a leap year"
print(X, m)
