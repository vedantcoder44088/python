def get_numbers():
    number=[]
    while True:
        num = input("Enter Number(For Finish Enter Empty String): ")
        if num == "":
            break
        number.append(float(num))
    return number
number = get_numbers()

list_number = list(number)
tuple_number = tuple(number)
print(list_number)
print(tuple_number)



