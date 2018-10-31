outFile = open("sometext.txt", "wt")
outFile.write("Hello world")
outFile.close()

outFile = open("sometext.txt", "r")
print(outFile.readline())
outFile.close()
    