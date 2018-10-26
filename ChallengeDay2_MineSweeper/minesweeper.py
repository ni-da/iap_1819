import sys, random


def reverse_list(old_ls, new_ls=[]):
    if 0 == len(old_ls):
        return
    else:
        new_ls.append(old_ls.pop(len(old_ls) - 1))
        reverse_list(old_ls, new_ls)
    return new_ls


def generate_game_by_minefieldstr(minefieldstr):
    global gameboard_length, gameboard_width
    gameboard_length = len(minefieldstr)
    gameboard_width = len(minefieldstr[0])
    minefieldstr = reverse_list(minefieldstr)

    for y in range(gameboard_length):
        for x in range(gameboard_width):
            print(minefieldstr[y][x], "->", x + 1, ",", y + 1)
            if minefieldstr[y][x] == '1':
                position_mine_fields.append((x + 1, y + 1))
        print()


def print_gameboard(l, w, revealing_fields=[], mine_fields=[]):
    for j in range(l, 0, -1):
        print(j, end="")
        for i in range(1, w + 1):
            skip_field = False
            # show hints about neighbors
            for field in revealing_fields:
                x = field[0]
                y = field[1]
                safe_neb = field[2]  # neighbours
                if i == x and j == y:
                    print("|", safe_neb, sep="", end="")
                    skip_field = True
            # show mines
            for field in mine_fields:
                x = field[0]
                y = field[1]
                if i == x and j == y:
                    print("|*", sep="", end="")
                    skip_field = True
            # if no mines or neighbors are shown, print empty field
            if not skip_field:
                print("| ", end="")
        print("|")
        # print +- after every row
        print(" ", end="")
        for i in range(1, w + 1):
            print("+-", end="")
        print("+")

    # print horizantal nummbers
    print("  ", end="")
    for i in range(1, w + 1):
        print(i, " ", sep="", end="")
    print()


def game_over(x, y):
    if (x, y) in position_mine_fields:
        return True
    return False


def handle_game_over():
    print("Unfortunately, you did not win... Don't give up, and try again!")
    print_gameboard(gameboard_length, gameboard_width, neighbours_fields, mine_fields=position_mine_fields)


def handle_input(x, y):
    player_attempts.append((x, y, 0))
    print_gameboard(gameboard_length, gameboard_width, revealing_fields=player_attempts)


def generate_neighbours_field():
    pass


position_mine_fields = []
player_attempts = []
neighbours_fields = []
gameboard_length = 0
gameboard_width = 0

# format input
if len(sys.argv) == 2:
    a = sys.argv[1].split(",")
    generate_game_by_minefieldstr(a)
elif len(sys.argv) == 4:
    # generate_game_by_random()
    print("generate_game_by_random")

# # start game
# print_gameboard(gameboard_length, gameboard_width)
#
# while True:
#     x = int(input("Give an x: "))
#     y = int(input("Give an y: "))
#     if not game_over(x, y):
#         handle_input(x, y)
#         print(player_attempts)
#         pass
#     else:
#         handle_game_over()
#         break
#
# # player_attempts.append((x, y))
# # print_gameboard(gameboard_length, gameboard_width)
