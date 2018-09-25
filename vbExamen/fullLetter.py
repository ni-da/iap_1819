s = "3AbCdEfGhIjKlMnOpQrStUvWxYz4abcdefghijklmnopqrstuvwxyz5 "


def isLetter(i):
    if "a" <= i <= "z" or "A" <= i <= "Z":
        return True
    else:
        return False


def getWordsList(sentence):
    list = []
    word = ""
    for i in sentence:
        if isLetter(i):
            word += i
        else:
            list.append(word)
            word = ""
    # print(list)
    return list


def isValidWord(word):

    alpha = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    if len(word) >= 26:
        newWord = word.upper()
        counter = 0
        validWord = True
        while counter < 26 and validWord:
            if alpha[counter] in newWord:
                validWord = True
            else:
                return False
            counter += 1
        return True
    else:
        return False


def al_fullLetter(sentence):
    wordsList = getWordsList(sentence)
    newList = []
    for w in wordsList:
        if isValidWord(w):
            newList.append(w)
    return newList




print(al_fullLetter(s))
