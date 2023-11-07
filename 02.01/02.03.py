
def fibonacci_with_recursion(n):
    if n <= 0:
        return "Incorrect input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_with_recursion(n - 1) + fibonacci_with_recursion(n - 2)


n_terms = 4

# Using recursion
print("Fibonacci series using recursion:")
for i in range(1, n_terms + 1):
    print(fibonacci_with_recursion(i), end=" ")

