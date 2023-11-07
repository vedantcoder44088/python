import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])
newa = a.reshape(2,5)
newb = a.reshape(5,2)
print(newa)
print(newb)

a = np.array([[1,2,3], [4,5,6]])
print(a.reshape(-1))