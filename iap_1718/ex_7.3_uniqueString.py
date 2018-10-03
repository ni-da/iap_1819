s = "abcd"

unique = True
for i in range(len(s)):
    for j in range(len(s)):
        if i != j:
            if (s[i] == s[j]):
                # print(list[i], "==", list[j], "SAME")
                print("Not Unique")
                unique = False
                exit()

print("Unique")
    