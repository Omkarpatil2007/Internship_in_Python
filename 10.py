# Numpy

# Array-processing package.
# Multi-dimensional array object

# Numpy Array
# Table of elements
# Index => tuple of positive integers

# Create a virtual env => install & setup packages
# python -m venv name_of_venv

# Install numpy
# pip install numpy

# Create a numpy array
# import numpy as np

# # Rank 1 array
# npArr = np.array([1,2,3])
# print(npArr)

# # Rank 2 array
# npArr = np.array(
#     [
#         [1,2,3],
#         [4,5,6]
#     ]
# )
# print(npArr)

# # Create array with tuple
# npArr = np.array((10,20,30))
# print(npArr)
# print(type(npArr))

# Accesing the array

# npArr = np.array([
#     [1,2,3,4],
#     [2,4,6,8],
#     [1,3,5,7],
# ])
# # print(npArr)

# print(npArr[2,2])
# print(npArr[:2, ::2])


#Practice
import numpy as np
# arr=np.array([1,2,3])
# print(arr)

arr=np.array(
    [
        [1,2,3],
        [2,3,4],
        [4,5,6]
    ])
print(arr)

#access the array
print(arr[2])
print(arr[:2 :-1])
print(arr[1,1])