def print_star_pyramid(h):
    for i in range(1, h + 1):
        for j in range(1, i+2):
            print("*", end="")
        print()

print_star_pyramid(int(input("h: ")))
