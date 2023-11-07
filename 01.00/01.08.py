# Write a python program to check if the entered year is leap year or not.

year = int(input("Enter The Year: "))
if year%4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")