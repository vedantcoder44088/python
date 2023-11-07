import numpy as np

# a) Extract all odd numbers from the array using the "where" clause.
array = np.array([1,2,3,2,3,4,3,4,5,6])
odds = array[np.where(array % 2 != 0)]
print("Odd numbers:", odds)

# b) Replace all odd numbers in the array with -1
array[array % 2 != 0] = -1
print("Array after replacement:", array)

# c) Convert a 1D array to a 2D array with 2 rows and 5 columns.
array_2d = array.reshape(2, 5)
print("2D Array:")
print(array_2d)

# d) Get the common items between array1 and array2
array1 = np.array([1,2,3,2,3,4,3,4,5,6])
array2 = np.array([7,2,10,2,7,4,9,4,9,8])
common_elements = np.intersect1d(array1, array2)
print("Common elements:", common_elements)

# e) Perform Matrix multiplication on 2 matrices.
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result_matrix = np.dot(matrix1, matrix2)
print("Matrix Multiplication Result:")
print(result_matrix)

# f) Using numpy and matplotlib/pylab generate bar plots for appropriate data.
import matplotlib.pyplot as plt

data = np.array([1, 2, 3, 4, 5])
plt.bar(np.arange(len(data)), data)
plt.show()
