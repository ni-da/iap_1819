def check_aant_rijen(lijst):
    if len(lijst) < 3:
        return False
    return True


def check_unique(r1, r2):
    for r in r1:
        if r in r2:
            return False
    for r in r2:
        if r in r1:
            return False
    return True


def check_row3(row1, row2, table):
    for row in table:
        if row != row1 and row != row2:
            for r in row:
                if r not in row1 and r not in row2:
                    return False
    return True


def is_special(table):
    two_unique_rows = False
    valid_third_row = False
    unique = []

    if not check_aant_rijen(table):
        return False
    counter = 0
    while two_unique_rows == False or counter < len(table):
        row = table[counter]
        counter_1 = 0
        while two_unique_rows == False or counter_1 < len(table):
            row_1 = table[counter_1]
            if check_unique(row, row_1):
                two_unique_rows = True
                break
            counter_1 += 1
        if two_unique_rows:
            break
        counter += 1

    if check_row3(row, row_1, table):
        valid_third_row = True

    if two_unique_rows and valid_third_row:
        return True
    return False


a = is_special([[1, 2], [1, 2], [1, 1, 2, 2]])
print(a)
