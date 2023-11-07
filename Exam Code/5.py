import numpy as np

a = np.array([1,2,3,4,5])
print("Original-a:", a)
b = a
print("Original-b:", b)
b[1] = 0
print("After Change - a:", a)
print("After Change - b:", b)

