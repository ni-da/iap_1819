def codeMineField(m):
    prevChr = m[0]
    currChr = ""
    nextChr = ""
    newStr = ""
    for i in range(len(m)-1):
        mineCounter = 0
        prevChr = m[i - 1]
        currChr = m[i]
        nextChr = m[i + 1]
        if prevChr == "X":
            mineCounter += 1
        if nextChr == "X":
            mineCounter += 1
        newStr += str(mineCounter)

    print(newStr)

codeMineField("XX XXX XX")