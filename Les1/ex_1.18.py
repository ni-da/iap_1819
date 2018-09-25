a = 0
a += int(input())
a += int(input()) * 2
a += int(input()) * 5
a += int(input()) * 10
a += int(input()) * 20

print("You have ", a // 100, ".", str(a % 100)[0], a % 10, " euro!", sep="")
