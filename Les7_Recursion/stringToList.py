import ast

# def convert_to_list(liststring):
#     newList = []
#     sublist = []
#     listingMode = False
#     for ele in liststring:
#         if ele == '[':
#             listingMode = True
#         elif ele == ']' and listingMode:
#             liststring = False
#             newList.append(sublist)
#         elif ele == ','

a = "[1,[2,3],[4,5,6],[7,[8,90],10],[11,120,[13]]]"


# b = a.split(',[')
# print(b)
# print(len(b))


def is_digit(a):
    digi = '0123456789'
    if a in digi:
        return True
    else:
        return False


def list_avg(nested_num_list):
    newList = []
    sublist = []
    item = ""
    listingMode = False
    for element in nested_num_list[1:len(nested_num_list) - 1]:
        # print("ele0", element)
        if element == "[":
            listingMode = True
        elif element == ']' and listingMode:
            listingMode = False
            sublist.append(int(item))
            item = ""
            newList.append(sublist)
            sublist = []
            # newList.append(sublist)
        elif is_digit(element):
            item += element
        else:
            if not listingMode:
                # print(item)
                newList.append(int(item))
                item = ""
            if listingMode:
                sublist.append(int(item))
                item = ""
    return newList


# print(ast.literal_eval(a))
print(list_avg(a))


# print(type(list_avg(a)))

def strlist_to_listtype(nested_num_list):
    newList = []
    sublist = []
    item = ""
    listingMode = False
    for element in nested_num_list[1:len(nested_num_list) - 1]:
        # print("ele0", element)
        if element == "[":
            listingMode = True
        elif element == ']' and listingMode:
            listingMode = False
            sublist.append(int(item))
            print(sublist)
            item = ""
            newList.append(sublist)
            sublist = []
            # newList.append(sublist)
        elif is_digit(element):
            item += element
        else:
            if not listingMode:
                # print(item)
                newList.append(int(item))
                item = ""
            if listingMode:
                sublist.append(int(item))
                item = ""
    return newList
