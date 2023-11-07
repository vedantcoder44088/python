# Write a python program to find out even numbers from a list using filter ().

my_list = [1,2,3,4,5]
even_result = list(filter(lambda x: x % 2 == 0, my_list))
print("Even Numbers: ",even_result)