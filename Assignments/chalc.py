import sys
import string

digi = string.digits
math_sign = "*/%^+-"


def validate_input(s):
    if len(s) < 2:
        return False
    else:
        return True


def validate_first_char(e):
    if is_open_brac(e[0]) or is_digit(e[0]):
        return True
    else:
        return False


def validate_last_char(e):
    if is_close_brac(e[len(e) - 1]) or is_digit(e[len(e) - 1]):
        return True
    else:
        return False


def is_digit(a):
    if a in digi:
        return True
    else:
        return False


def is_open_brac(a):
    if a == "(":
        return True
    else:
        return False


def is_close_brac(a):
    if a == ")":
        return True
    else:
        return False


def is_math_sign(a):
    if a in math_sign:
        return True
    else:
        return False


def validate_char(c):
    if is_digit(c) or \
            is_open_brac(c) or \
            is_close_brac(c) or \
            is_math_sign(c):
        return True
    else:
        return False


def validate_expression(expression):
    math_sign = False
    prev_char = ""
    counter_open_brac = 0
    counter_close_brac = 0
    if validate_first_char(expression) and validate_last_char(expression):
        for j in range(len(expression)):
            i = expression[j]
            prev_char = expression[j - 1]
            if validate_char(i):
                if is_math_sign(i):
                    if math_sign:
                        return False  # 2 math sings na elkaar
                    else:
                        math_sign = True
                else:
                    math_sign = False
                if is_close_brac(i) and is_open_brac(prev_char):
                    return False  # empty bracket
                if is_open_brac(i):
                    counter_open_brac += 1
                if is_close_brac(i):
                    counter_close_brac += 1
            else:
                return False  # char not valid of given options
    else:
        return False  # first and last char not valid
    if counter_open_brac != counter_close_brac:
        return False

    return True


def process_input(s):
    wrong_exp_counter = 0
    if validate_input(s):
        for e in s[1:]:
            if not validate_expression(e):
                print(e)
                wrong_exp_counter += 1
        if wrong_exp_counter == 0:
            print("correct")
    else:
        print("no input provided")


process_input(sys.argv)
