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


def get_all_neighbors_by_current_position(currX, currY):
    all_neighbors = []
    x = currX + 1
    y = currY - 1
    if x > 0 and y > 0:
        if x <= len(all_positions[0]) and y <= len(all_positions):
            all_neighbors.append((x, y))
    x = currX - 1
    y = currY + 1
    if x > 0 and y > 0:
        if x <= len(all_positions[0]) and y <= len(all_positions):
            all_neighbors.append((x, y))
    for j in range(3):
        for i in (-1, 1):
            if j == 0:
                x = i + currX
                y = i + currY
            elif j == 1:
                x = currX
                y = currY + i
            elif j == 2:
                x = currX + i
                y = currY
            if x > 0 and y > 0:
                if x <= len(all_positions[0]) and y <= len(all_positions):
                    all_neighbors.append((x, y))
    return all_neighbors


# def get_all_neighbors_information_by_current_position(currX, currY):
#     neighbors = get_all_neighbors_by_current_position(currX, currY)
#     neighbors.append((currX, currY))
#     for neb in neighbors:
#         for field in fields_content:
#             if neb[0] == field[0] and neb[1] == field[1]:
#                 if field[2] == 0:
#                     get_all_neighbors_information_by_current_position(field[0], field[1])
#                 elif field[2] != "*":
#                     if field not in neighbors_information:
#                         player_attempts.append(field)


all_positions = generate_all_positions(4, 5)
# print(all_positions)
neb = get_all_neighbors_by_current_position(3, 3)
print(neb)
