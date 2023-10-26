import numpy as np


# ex1 : Write a NumPy program to test whether none of the elements of a given array is zero.

arr = np.array([1, 2, 3, 4])
print(np.all(arr))

arr = np.array([0, 1, 2, 3])
print(np.all(arr))

# ex2 : Write a NumPy program to test whether any of the elements of a given array is non-zero.

arr = np.array([1, 2, 3, 4])
print(np.any(arr))

arr = np.array([0, 1, 2, 3])
print(np.any(arr))

arr = np.array([0, 0, 0, 0])
print(np.any(arr))

# ex3 : Write a NumPy program to test element-wise for NaN of a given array.

arr = np.array([1, 2, np.nan, 4])
print(np.isnan(arr))

# ex4 : Write a NumPy program to create an element-wise comparison (greater, greater_equal, less and less_equal) of two given arrays.

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([2, 3, 4, 5])
print(np.greater(arr1, arr2))
print(np.greater_equal(arr1, arr2))
print(np.less(arr1, arr2))
print(np.less_equal(arr1, arr2))

# ex5 : Write a NumPy program to create an array of 10 zeros, 10 ones, 10 fives.

arr = np.zeros(10)
print(arr)

arr = np.ones(10)
print(arr)

arr = np.ones(10) * 5
print(arr)

# ex6 : Write a NumPy program to create an array of the integers from 30 to 70.

arr = np.arange(30, 71)
print(arr)


# ex7 : Write a NumPy program to create an array of all the even integers from 30 to 70.

arr = np.arange(30, 71, 2)
print(arr)

# ex8 : Write a NumPy program to create a 3x4 matrix filled with values from 10 to 21.

arr = np.arange(10, 22).reshape(3, 4)
print(arr)

# ex9 : Write a NumPy program to find the dimension of a given matrix, the number of rows and columns of this matrix and its size.

print(arr.ndim)
print(arr.shape)
print(arr.size)

# ex10 : Write a Python program to find the maximum and minimum value of a given flattened array.

arr = np.arange(0, 4).reshape(2, 2)

print(arr.max())
print(arr.min())

# ex11 : Write a NumPy program to get the minimum and maximum value of a given array along the second axis.

print(arr.max(axis=1))
print(arr.min(axis=1))

# ex12 : Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array.

arr = np.arange(1, 7)

print(arr.argmax())
print(arr.argmin())

# ex13 : Write a NumPy program to compute pearson product-moment correlation coefficients of two given arrays.

arr1 = [0, 1, 3]
arr2 = [2, 4, 5]

print(np.corrcoef(arr1, arr2))

