# Prime or not prime. Input: L= [3,4,6,9,11] Output: L= [P, NP, NP, NP, P] using map function.

def is_prime(num):
    if num <= 1:
        return "NP"
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "NP"
    return "P"

numbers = (3, 4, 6, 9, 11)
result = list(map(is_prime, numbers))
print(result)

