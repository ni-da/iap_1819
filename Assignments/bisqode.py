import sys


def convert_to_code(s):
    if s == " ":
        return 26
    code = (ord(s) - 97) % 26
    return code


def calculate_power(n, exponent):
    res = 1
    while exponent != 0:
        res *= n
        exponent -= 1
    return res


def calculate_base27(tekst):
    som = 0
    counter = len(tekst) - 1
    for i in tekst:
        code = convert_to_code(i)
        code_res = code * (calculate_power(27, counter))
        som += code_res
        counter -= 1
    return som


def convert_to_base2(r):
    temp_bin = ""
    while r >= 0:
        reminder = int(r % 2)
        if reminder == 1:
            r = (r / 2) - 0.5
        else:
            r = r / 2
        temp_bin += str(reminder)
        if r == 0:
            break
    return reverse(temp_bin)


def reverse(tekst_to_reverse):
    reversed_tekst = ""
    counter = len(tekst_to_reverse) - 1

    while counter >= 0:
        reversed_tekst += tekst_to_reverse[counter]
        counter -= 1
    return reversed_tekst


def calculate_root(length_bin):
    root_counter = 1
    root = 0
    while root < length_bin:
        root = root_counter * root_counter
        root_counter += 1
    return (root_counter - 1, root)


def add_zeros(base2):
    root_counter, total_length = calculate_root(len(base2))
    zeros_to_add = total_length - len(base2)
    new_bin = base2
    for i in range(zeros_to_add):
        new_bin = "0" + new_bin
    return (root_counter, new_bin)


def print_output(a, times):
    old = 0
    counter = 0
    while counter < len(a) + times:
        print(a[old:counter])
        old = counter
        counter += times


tekst = sys.argv[1]
base27 = calculate_base27(tekst)
base2 = convert_to_base2(base27)
times, zero_added = add_zeros(base2)
print_output(zero_added, times)
