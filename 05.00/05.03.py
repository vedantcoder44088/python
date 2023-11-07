

f1 = open("text0301.txt", "r")
f2 = open("text0302.txt", "a")

for lines in f1:
    f2.write(lines)

f1.close()
f2.close()
