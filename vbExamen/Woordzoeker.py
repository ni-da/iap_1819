lettermatrix = [['e', 'i', 'k', 'z', 't'],
                ['e', 'y', 'u', 'e', 'n'],
                ['n', 'o', 'p', 'r', 'e'],
                ['x', 'z', 'y', 'g', 't']]


def puzzle_matrix(lettermatrix, word):
    for i in range(len(lettermatrix)):
        for j in range(len(lettermatrix[i])):
            if lettermatrix[i][j] == word[0]:
                # same row -- right left
                if i != 0:
                    print("Up!", lettermatrix[i - 1][j])  # check up
                if i != len(lettermatrix) - 1:
                    print("Down!", lettermatrix[i + 1][j])  # check down

                if j != 0:
                    print("LEFT!", lettermatrix[i][j - 1])  # check left
                if j != len(lettermatrix[i]) - 1:
                    print("RIGHT!", lettermatrix[i][j + 1])  # check right

                # print(i, ", ", j)


puzzle_matrix(lettermatrix, "eik")
