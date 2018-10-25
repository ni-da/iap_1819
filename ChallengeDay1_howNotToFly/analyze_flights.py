import sys


def split_line(theLine):
    data = []
    dataChunk = ""
    stringMode = False
    for i in theLine:
        if i != ",":
            if i == '"':
                if not stringMode:
                    stringMode = True
                else:
                    stringMode = False
                    dataChunk += i
            else:
                dataChunk += i
        else:
            if not stringMode:
                dataChunk.replace('"', "")
                data.append(dataChunk)
                dataChunk = ""
    return (data)


fileName = sys.argv[1]
lineCounter = 0
mynewhandle = open(fileName, "r")
som = 0
sum_data = [0] * 10

while True:
    theLine = mynewhandle.readline()
    if len(theLine) == 0:
        break
    lineCounter += 1
    if lineCounter != 1:
        dataChunk = ""
        stringMode = False
        data = split_line(theLine)
        if data[6] != "":
            sum_data[0] += int(float(data[6]))
        if data[7] != "":
            sum_data[1] += int(float(data[7]))
            for j in range(2, 10):
                sum_data[j] += int(float(data[j + 11]))
mynewhandle.close()

print_desc = ["Flights:", "Delayed", "Cancelled", "Diverted",
              "Delayed minutes:", "carrier: ", "weather: ", "nas: ",
              "security: ", "late aircraft: "]

for p in range(len(print_desc)):
    if 1 <= p <= 3:
        print(print_desc[p], "flights:", sum_data[p])
        if p == 3:
            print()
    elif p == 0 or p == 4:
        print(print_desc[p], sum_data[p])
    else:
        print("Delayed by ", print_desc[p], int(sum_data[p] / (sum_data[4] / 100)), "%", sep="")
