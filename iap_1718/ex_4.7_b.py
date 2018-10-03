def print_star_line(m, n):
    for i in range(m):
        print(" ", end="")
    for i in range(n):
        print("*", end="")
    for i in range(m):
        print(" ", end="")

print_star_line(int(input("m: ")), int(input("n: ")))
