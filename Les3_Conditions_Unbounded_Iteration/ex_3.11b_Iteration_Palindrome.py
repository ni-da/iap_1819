w = input()
i = 0
j = len(w)
isPlain = "is a palindrome"
while i < len(w) and j >= 0:
    if w[i] != w[j - 1]:
        isPlain = "is not a palindrome"

        break
    i += 1
    j -= 1
print(w, isPlain)
