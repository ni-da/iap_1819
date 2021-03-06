# Author: Nida Ilyas
# Student number: 1747417
#
# I have implemented all features of the game.
# I have implemented the bonus features.
# Bonus checks: not enough arguments provided! There must be at least 1 mine-free field.
# * minefieldstring; all rows should be same size. Every character of a row must be
# a digit. A row can only contain a 0 or 1.
# * width, length, mines: all 3 inputs must be a digit. The number of mines must be in the
# range of width*length.
# While playing; the provided positions(x,y) must be valid digits, still hidden. (not reveald) and
# in the range of gameboard.
# The gameboard looks pretty okay till width = 99 and height = 99
# At large inputs, it can take long to show on screen. So, wait long enough!

import sys, random


def is_digit(a):
    digi = '0123456789'
    for i in a:
        if i not in digi:
            return False
    return True


# reverse a list: used to reverse the minefieldstr
def reverse_list(list):
    if len(list) == 0:
        return []
    else:
        return [list[-1]] + reverse_list(list[:-1])


# decodes the minefieldstr by iterating over every string and afterwards over every character of the string.
# if it's a '1', its considerd mine. And as result, it's appened to the mines list.
# While iterating, all the positions on the gameboard are calculated and added to the all_positions list.
def generate_game_by_minefieldstr(minefieldstr):
    global gameboard_length, gameboard_width

    gameboard_length = len(minefieldstr)
    gameboard_width = len(minefieldstr[0])
    minefieldstr = reverse_list(minefieldstr)

    for y in range(gameboard_length):
        row = []
        for x in range(gameboard_width):
            row.append((x + 1, y + 1))
            if minefieldstr[y][x] == '1':
                position_mines.append((x + 1, y + 1))
        all_positions.append(row)


# generates 2 random numbers for x and y, such that 1<= randomNumber <= length, width.
def generate_random_mines(gameboard_width, gameboard_length, minesToGenerate):
    random_generated_mines = []
    while len(random_generated_mines) < (minesToGenerate):
        random_x = random.randint(1, gameboard_width)
        random_y = random.randint(1, gameboard_length)
        if (random_x, random_y) not in random_generated_mines:
            random_generated_mines.append((random_x, random_y))
    return (random_generated_mines)


# Iterrates over length and width of the gameboard.
# While iterating, all the positions on the gameboard are calculated and added to the all_positions list.
def generate_game_by_random(gameboard_width, gameboard_length, minesToGenerate):
    global position_mines
    position_mines = generate_random_mines(gameboard_width, gameboard_length, minesToGenerate)
    # print(position_mines)
    for y in range(gameboard_length):
        row = []
        for x in range(gameboard_width):
            row.append((x + 1, y + 1))
        all_positions.append(row)


# it iterate over every field, and checks on the neighbors of it. On the basis of
# neighbor's status (mine of not), the number is calculated for every field.
def fill_content_in_fields():
    if len(position_mines) == 0:
        print("")
    for positionRow in all_positions:
        for position in positionRow:
            mines_in_neighborhood = 0
            neighbors = get_all_neighbors_by_current_position(position[0], position[1])
            for neighbor in neighbors:
                if neighbor in position_mines:
                    mines_in_neighborhood += 1
            fields_content.append((position[0], position[1], mines_in_neighborhood))
    counter = 0
    while counter < len(fields_content):
        field = fields_content[counter]
        if (field[0], field[1]) in position_mines:
            fields_content[counter] = ((field[0], field[1], "*"))
        counter += 1


# calculates every neighbors by minor calculations
def get_all_neighbors_by_current_position(currX, currY):
    all_neighbors = []
    # all_neighbors.append((currX, currX))
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


def is_zero_field(currX, currY):
    for field in fields_content:
        if currX == field[0] and currY == field[1]:
            if field[2] == 0:
                return True
    return False


def get_all_neighbors_of_a_zero_field(currX, currY):
    neighbors = get_all_neighbors_by_current_position(currX, currY)
    for neighbor in neighbors:
        for field in fields_content:
            if (field[0], field[1]) not in all_all_neighbours:
                if neighbor[0] == field[0] and neighbor[1] == field[1]:
                    if field[2] != "*":
                        all_all_neighbours.append((field[0], field[1]))
                    if field[2] == 0:
                        get_all_neighbors_of_a_zero_field(neighbor[0], neighbor[1])
    return


# It fetches information about every possible neighbor. If a neighbor is 0 if fetches
# information about it's neighbor.
# It a neighbor isn't 0, if appends the position and the number to the player_attempts list.
def get_revealing_field(currX, currY):
    if is_zero_field(currX, currY):
        get_all_neighbors_of_a_zero_field(currX, currY)
    all_all_neighbours.append((currX, currY))
    for neighbor in all_all_neighbours:
        for field in fields_content:
            if neighbor[0] == field[0] and neighbor[1] == field[1]:
                if field not in player_attempts:
                    player_attempts.append(field)
                    player_inputs.append((field[0], field[1]))


# prints the gameboard
def print_gameboard(l, w, revealing_fields=[]):
    print("  ", end="")
    for i in range(1, w + 1):
        if i > 9:
            print("+--", end="")
        else:
            print("+-", end="")
    print("+")
    # print vertical numbers
    for j in range(l, 0, -1):
        if 9 < j < 100:
            print(j, "", sep="", end="")
        else:
            print(j, " ", sep="", end="")
        for i in range(1, w + 1):
            skip_field = False
            # show hints about neighbors
            for field in revealing_fields:
                x = field[0]
                y = field[1]
                content = field[2]  # neighbours
                if i == x and j == y:
                    if i > 9:
                        print("| ", content, sep="", end="")
                    else:
                        print("|", content, sep="", end="")
                    skip_field = True
            if not skip_field:
                if i > 9:
                    print("|  ", end="")
                else:
                    print("| ", end="")
        print("|")
        # print +- after every row

        print("  ", end="")
        for i in range(1, w + 1):
            if i > 9:
                print("+--", end="")
            else:
                print("+-", end="")
        print("+")

        # print horizantal nummbers

    print("   ", end="")
    for i in range(1, w + 1):
        print(i, " ", sep="", end="")
    print()


# checks if game is over. The x,y are the values, given by the player.
# It checks whether the position given by the player is in the list of mines.
def game_over(x, y):
    if (x, y) in position_mines:
        return True
    return False


# when game is over. A message is shown and also the whole gameboard filled with all values is printed.
def handle_game_over():
    print("Unfortunately, you did not win... Don't give up, and try again!")
    print_gameboard(gameboard_length, gameboard_width, revealing_fields=fields_content)


# Validates the given input and prints the gameboard.
def handle_input(x, y):
    get_revealing_field(x, y)
    if len(player_attempts) == len(fields_content) - len(position_mines):
        print("Congratulations, you have won!")
        print_gameboard(gameboard_length, gameboard_width, revealing_fields=fields_content)
        sys.exit()
    else:
        print_gameboard(gameboard_length, gameboard_width, revealing_fields=player_attempts)


def validate_minefieldstr(minefieldstr):
    length_first_row = len(minefieldstr[0])
    for row in minefieldstr:
        if length_first_row != len(row):
            print("All rows of minefieldstring should be of same length.")
            return False
        for element in row:
            if not is_digit(element):
                print("A minefieldstring should only contain digits.")
                return False
            else:
                if not (int(element) == 0 or int(element) == 1):  # start here
                    print("A minefieldstring should only contain a 0 or 1.")
                    return False
    return True


def validate_minefieldarguments(arguments):
    gameboard_width = arguments[0]
    gameboard_length = arguments[1]
    minesToGenerate = arguments[2]

    if not is_digit(gameboard_length):
        print("The provided length is not a valid digit.")
        return False
    if not is_digit(gameboard_width):
        print("The provided width is not a valid digit.")
        return False
    if not is_digit(minesToGenerate):
        print("The provided number of mines is not a valid digit.")
        return False
    if int(minesToGenerate) > int(gameboard_width) * int(gameboard_length):
        print("The amount of mines must be in the range of gameboard's width * length.")
        return False
    return True


def print_arguments_options():
    option1 = 'Option 1: Minefieldstr, for example "minesweeper.py 1001,1010,1100,0001,0000"'
    option2 = 'Option 2: for example "minesweeper.py Width Length Mines"'
    print(option1)
    print(option2)


def valid_xy_input(x, y):
    if x == "" or y == "":
        print("x,y: field can't be empty!")
        return False
    if not is_digit(x) or not is_digit(y):
        print(x, ',', y, "field doesn't contain a valid digit! Try another field position.")
        return False
    x = int(x)
    y = int(y)
    if (x, y) in player_inputs:
        print(x, ',', y, "field is already reveald! Try another field position.")
        return False
    if (x < 1 or y < 1) or (x > gameboard_width or y > gameboard_length):
        print(x, ',', y, "field is not in the range of gameboard! Try another field position.")
        return False
    return True


def checkMines():
    if len(position_mines) == gameboard_length * gameboard_width:
        print("At least a single field should not hold a mine.")
        sys.exit()


# START
all_all_neighbours = []

fields_content = []
all_positions = []
position_mines = []

player_attempts = []
player_inputs = []

gameboard_length = 0
gameboard_width = 0

# format input
if len(sys.argv) == 1:
    print("Not enough arguments provided.")
    print_arguments_options()
    sys.exit()
elif len(sys.argv) == 2:
    a = sys.argv[1].split(",")
    if validate_minefieldstr(a):
        generate_game_by_minefieldstr(a)
    else:
        print("Provided argumants are not valid!")
        print_arguments_options()
        sys.exit()
elif len(sys.argv) == 4:
    if validate_minefieldarguments(sys.argv[1:]):
        gameboard_width = int(sys.argv[1])
        gameboard_length = int(sys.argv[2])
        minesToGenerate = int(sys.argv[3])
        generate_game_by_random(gameboard_width, gameboard_length, minesToGenerate)
    else:
        print("Provided argumants are not valid!")
        print_arguments_options()
        sys.exit()
else:
    print("Provided argumants are not valid!")
    print_arguments_options()
    sys.exit()
checkMines()
# start game
fill_content_in_fields()
print_gameboard(gameboard_length, gameboard_width)

while True:
    x = input("Give an x: ")
    y = input("Give an y: ")
    while not valid_xy_input(x, y):
        x = input("Give an x: ")
        y = input("Give an y: ")
    x = int(x)
    y = int(y)
    if not game_over(x, y):
        handle_input(x, y)
        pass
    else:
        handle_game_over()
        break
