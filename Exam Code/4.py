import numpy as np

a = np.array([1,2,3,4,5])

condition = (a>2) & (a<4)
print(a[condition])

condition1 = (a<2) | (a>4)
print(a[condition1])

a1 = np.array([True, True, False])
newa1 = ~a1
print(newa1)