# 1) Addition of first 15 numbers using loop. 2) Addition of any 15 numbers using a loop.

total1 = 0
for i in range(1,16):
    total1 += i
print("Sum Of First 15 Number: ", total1)

total2 = 0
for i in range(1,16):
    try:
        num = float(input("Number: "))
        total2 += num
    except ValueError:
        print("Error")
print("Sum Of The 15 Number: ", total2)