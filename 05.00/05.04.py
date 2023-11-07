import re
f = open("text04.txt", "r")
s = f.read()
numbers = re.findall('[0-9]+', s)
if numbers:
    print("Number Is : ",numbers)
elif not numbers:
    print("Number Not In File")