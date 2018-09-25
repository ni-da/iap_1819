a = input()
b = input()
m = "are anagrams"
# for i in a:
#     if i not in b:
#         m = "are not anagrams"
#         break
#
# print(a, "and", b, m)


counter = 0
for i in a:
    for j in b:
        if i == j:
            counter += 1

    if counter == 0:
        m = "are not anagrams"
        break

    counter = 0

print(a, "and", b, m)

# a = "abcdefghijklmnopqrstuvwxyz"
# isAna = True
# for a in a:
#     countF = 0
#     for j in range()
