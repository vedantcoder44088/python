import numpy as np

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])

print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)

a1 = np.array([True, True, False])
b1 = np.array([False, True, True])
print(np.logical_and(a1,b1))
print(np.logical_or(a1,b1))