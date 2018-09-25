x = 13

lengthLastAns = len(str(10 * x))

for i in range(11):
    lengthCurrAns = len(str(i * x))
    lengthCurrI = len(str(i))
    print(x, " times",
          " " * (2 - lengthCurrI + 1)
          , i,
          " =",
          " " * (lengthLastAns - lengthCurrAns + 1),
          i * x,
          sep="")
