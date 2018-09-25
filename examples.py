def showRightGuessed(word, char):
    rightGuessed = ""
    for i in word:
        if i == chr or i in rightGuessed:
            rightGuessed += chr
            print(i, end="")
        else:
            print("_", end="")


word = "dog"
inputChr = input("A letter: ")
rightGuessed = ""
# chr = "o"
showRightGuessed(word, inputChr)

# for i in word:
#     if i == chr:
#         rightGuessed += chr
#         print(i, end="")
#     else:print("_", end="")
