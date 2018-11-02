# def get_all_neighbors_information_by_current_position(currX, currY):
#     neighbors = get_all_neighbors_by_current_position(currX, currY)
#     # neighbors.append((currX, currY))
#     for neighbor in neighbors:
#         for field in fields_content:
#             if neighbor[0] == field[0] and neighbor[1] == field[1]:
#                 if field[2] != "*":
#                     if field not in player_attempts:
#                         player_attempts.append(field)
#                         player_inputs.append((field[0], field[1]))


a = [(1, 1), (1, 2), (2, 2), (2, 1)]
b = [(1, 1), (1, 2, 0), (2, 2, 0), (2, 1, 0)]


# def do(currX, currY):
#     for neighbor in a:
#         for field in b:
#             if neighbor[0] == field[0] and neighbor[1] == field[1]:
