def draw_gameboard(l, w):
    counter = l
    while counter >= 0:
        print("  ", end="")
        for i in range(w):
            print("+-", end="")
        print("+", end="")
        print()
        if counter != 0:
            print(counter, end="")
            for i in range(w + 1):
                print(" |", end="")
            print()
        else:
            print("   ", end="")
            for i in range(1, w + 1):
                print(i, "", sep=" ", end="")
        counter -= 1


def generate_all_positions(width, length):
    all_pos = []
    for i in range(1, length + 1):
        row = []
        for j in range(1, width + 1):
            row.append((j, i))
        all_pos.append(row)
    return all_pos


def get_all_neighbors(all_positions):
    all_neighbors = []
    for y in range(1, len(all_positions) + 1):
        for x in range(1, len(all_positions[0]) + 1):
            if (x - 1, y - 1) in all_positions: all_neighbors.append((x - 1, y - 1))
            if (x, y - 1) in all_positions: all_neighbors.append((x, y - 1))
            if (x + 1, y - 1) in all_positions: all_neighbors.append((x + 1, y - 1))

            if (x - 1, y) in all_positions: all_neighbors.append((x - 1, y))
            if (x + 1, y) in all_positions: all_neighbors.append((x + 1, y))

            if (x - 1, y + 1) in all_positions: all_neighbors.append((x - 1, y + 1))
            if (x, y + 1) in all_positions: all_neighbors.append((x, y + 1))
            if (x + 1, y + 1) in all_positions: all_neighbors.append((x + 1, y + 1))
    return all_neighbors


all_pos = generate_all_positions(2, 2)
neb = get_all_neighbors(all_pos)
print(neb)
