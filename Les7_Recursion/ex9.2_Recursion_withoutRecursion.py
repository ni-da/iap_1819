def print_first(string, i):
    for j in range(i, len(string)):
        print(string[j], end="")


print_first("STRING", 2)

print()
def print_last(string, i):
    j = len(string) - 1
    while j >= i:
        print(string[j], end="")
        j -= 1


print_last("STRING", 2)
