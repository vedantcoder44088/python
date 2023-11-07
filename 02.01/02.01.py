# Write a function to find out x^y. Function should find out the square of x in case of default
# argument passing.
def power(x,y=2):
    return x**y
result1 = power(5)
result2 = power(2,3)
print("Result 1: ",result1)
print("Result 2: ",result2)