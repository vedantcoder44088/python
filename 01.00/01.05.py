# Create a menu-driven program to show various operators supported by python.

def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def power(a,b):
    return a**b
def menu():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Power")

while True:
    menu()
    choice = int(input("Enter Choice: "))

    if choice == 0:
        print("Exiting The Program")
    elif choice in range(1,3):
        n1 = float(input("Enter 1st: "))
        n2 = float(input("Enter 2nd: "))

        if choice == 1:
            print("Result: ", addition(n1,n2))
        elif choice == 2:
            print("Result: ", subtraction(n1,n2))
        elif choice == 3:
            print("Result: ", power(n1,n2))
    else:
        print("Invalid Choice")