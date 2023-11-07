global_var = "I am global"

def function_scoping_demo():
    local_var = "I am local"
    print("Inside the function:")
    print(local_var)
    print(global_var)

print("Outside the function:")
print(global_var)  # Accessing global variable
# print(local_var)  # Uncommenting this line will result in an error

function_scoping_demo()
