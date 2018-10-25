# def strange_function():
#     value = input("Give input: ")
#     if len(value) != 0:
#         strange_function()
#         print(value)
#
#
# strange_function()

def strange_function_1():
    values = ""
    value = input("Give input: ")
    while len(value) != 0:
        values += value
        value = input("Give input: ")
    print(values)


strange_function_1()
