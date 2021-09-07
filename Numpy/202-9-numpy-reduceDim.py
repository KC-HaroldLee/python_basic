import numpy as np

arr1 = np.arange(12).reshape(3, -1)
print(arr1)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

flat1F = arr1.flatten(order='F')
# [ 0  4  8  1  5  9  2  6 10  3  7 11]
flat1C = arr1.flatten(order='C')
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(flat1F)
print(flat1C)