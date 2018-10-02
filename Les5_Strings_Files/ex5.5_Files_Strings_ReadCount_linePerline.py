# inputFile = input("Input file: ")
# outputFile = input("Output file: ")

readFile = open("test_read.txt", "r")
writeFile = open("test_write.txt", "w")

for line in readFile:
    lineList = line.split()

    writeFile.write(str(len(lineList)) + "\n")

readFile.close()
writeFile.close()
