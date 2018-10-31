def r_sum(nested_num_list):
    tot = 0
    total_srt = ""
    for element in nested_num_list:
        if type(element) == type([]):
            tot += r_sum(element)
        elif type(element) == type("Ok"):
            print(element)
        else:
            tot += element
    return tot


a = [1, 2, 3, "Na", [2], [1, 3, 1], "Ni", 2, 3, 2]

print(r_sum(a))


def get_all_neighbors_by_current_position(currX, currY):
    pass


fields_content = []
player_attempts, player_inputs = []


def get_all_neighbors_information_by_current_position(currX, currY):
    neighbors = get_all_neighbors_by_current_position(currX, currY)
    # neighbors.append((currX, currY))
    for neighbor in neighbors:
        for field in fields_content:
            if neighbor[0] == field[0] and neighbor[1] == field[1]:
                if field[2] != "*":
                    if field not in player_attempts:
                        player_attempts.append(field)
                        player_inputs.append((field[0], field[1]))
                if field[2] == 0:
                    get_all_neighbors_information_by_current_position(field[0], field[1])
    return
