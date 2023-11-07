# Write a Python program which accepts the user's first and last name and print them in reverse order
# with a space between them.

def main():
    f_name = input("first name: ")
    l_name = input("last name: ")
    fully_reversed = l_name + " " + f_name
    print("Your Name: ", fully_reversed)

if __name__ == "__main__":
    main()