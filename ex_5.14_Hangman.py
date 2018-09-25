def showRightGuessed(word, char, rightGuessed):
    for i in word:
        if i == char:
            print(i, end="")
        elif i in rightGuessed:
            print(i, end="")
        else:
            print("_", end="")
    print()


word = "dog"
inputChr = input("Letter: ")
inputStr = inputChr
maxAttemps = 5  
wrongAttmp = 0
rightGuessed = ""

while rightGuessed != word or wrongAttmp < maxAttemps - 1:
    print(inputStr)
    print()
    inputStr += inputChr

    inputChr = input("A letter: ")
    if inputChr not in word:  # char not in word
        wrongAttmp += 1
    else:
        print("GOOD!!")
        rightGuessed += inputChr
        showRightGuessed(word, inputChr, rightGuessed)
        #
        # for i in word:
        #     if i == inputChr:
        #         print(i, end="")
        #     else:
        #         print("_", end="")

if wrongAttmp == maxAttemps - 1:
    print("Out of points!")
    exit()

# if rightGuessed != word
# print(inputChr)
