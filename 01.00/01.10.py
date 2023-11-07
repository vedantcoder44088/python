# Write a Python program to print the calendar of a given month and year.

import calendar
month = int(input("Enter Month: "))
year = int(input("Enter Year: "))

print(calendar.month(year, month))