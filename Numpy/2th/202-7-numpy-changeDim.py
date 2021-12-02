import numpy as np
from numpy.core.records import array

arr1 = np.arange(12)
# print(arr1) # [ 0  1  2  3  4  5  6  7  8  9 10 11]

reshapedArr1 = arr1.reshape(2, 3, 2)
# print(reshapedArr1) 
# [[[ 0  1]
#   [ 2  3]
#   [ 4  5]]

#  [[ 6  7]
#   [ 8  9]
#   [10 11]]]

reshapedArr2 = np.reshape(arr1, (2, -1), order='F')
# print(reshapedArr2)
# [[ 0  2  4  6  8 10]
#  [ 1  3  5  7  9 11]]

reshapedArr3 = np.reshape(arr1, (3, -1), order='F')
print(reshapedArr3)
# [[ 0  3  6  9]
#  [ 1  4  7 10]
#  [ 2  5  8 11]]

reshapedArr4 = np.reshape(arr1, (3, -1), order='C')
print(reshapedArr4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]