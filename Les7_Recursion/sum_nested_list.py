import sys, ast


def list_avg(nested_num_list):
    tot = 0
    for element in nested_num_list:
        # print("ele0", element)
        if type(element) == type([]):
            tot += list_avg(element)
        else:
            # print("ele", element)
            tot += int(element)
    return int(tot // len(nested_num_list))


a = sys.argv[1]
b = ""
for i in range(1, len(a) - 1):
    b += a[i]
b = ast.literal_eval(b)

# def stringlist_to_real_list(input_string):
#     clean_input = input_string.replace('[', '').replace(']', '')
#     return clean_input.split(',')
#
# def convert_to_list(liststring):
#     newList = []
#     sublist = []
#     listingMode = False
#     for ele in liststring:
#         if ele == '[':
#             listingMode = True
#
#
# b = convert_to_list(a)  # [2, 3, 4]
# print(b)
# print("TYPE B:", type(b))
print("Average approval rate is", list_avg(b))
