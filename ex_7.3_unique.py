list = [1, 5, 3, 2]

unique = True
for i in range(len(list)):
    for j in range(len(list)):
        if i != j:
            if (list[i] == list[j]):
                # print(list[i], "==", list[j], "SAME")
                print("Not Unique")
                unique = False
                exit()

print("Unique")
