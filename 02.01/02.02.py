def factorial_without_recursion(n):
    factorial = 1
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            factorial *= i
        return factorial

def factorial_with_recursion(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0:
        return 1
    else:
        return n * factorial_with_recursion(n - 1)

number = 5
result1 = factorial_without_recursion(number)
result2 = factorial_with_recursion(number)

print(f"The factorial of {number} is (Without Recursion): {result1}")
print(f"The factorial of {number} is (With Recursion): {result2}")