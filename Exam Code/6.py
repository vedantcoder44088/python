import numpy as np
a = np.array([[1,2], [4,5]])
b = np.array([[1,2], [4,5]])
print(a)
print(a.flatten())
print(np.dot(a,b))
print(np.transpose(a))

print(np.linalg.det(a))
print(np.linalg.inv(a))