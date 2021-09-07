# 04.104.py 확인해볼 것

import numpy as np

arr1 = np.arange(6).reshape(2,3)
# print(arr1.ndim) # 2
# print(arr1)
# [[0 1 2]
#  [3 4 5]]

arr2 = np.arange(6,12).reshape(2,3)
# print(arr2.ndim) # 2
# print(arr2)
# [[ 6  7  8]
#  [ 9 10 11]]

merge1 = np.stack([arr1, arr2], axis=0)
merge2 = np.stack([arr1, arr2], axis=-1)

# print(merge1.ndim) # 3
# print(merge1)
# [[[ 0  1  2]
#   [ 3  4  5]]

#  [[ 6  7  8]
#   [ 9 10 11]]]

# print(merge2.ndim) # 3
# print(merge2)
# [[[ 0  6]
#   [ 1  7]
#   [ 2  8]]

#  [[ 3  9]
#   [ 4 10]
#   [ 5 11]]]


arr3 = np.arange(12,18).reshape(2,3)
# print(arr2.ndim) # 2

merge3 = np.stack([arr1, arr2, arr3], axis=-1)
# print(merge3.ndim) # 3
# print(merge3)
# [[[ 0  6 12]
#   [ 1  7 13]
#   [ 2  8 14]]

#  [[ 3  9 15]
#   [ 4 10 16]
#   [ 5 11 17]]]


merge4 = np.stack([arr1, arr2, arr3], axis=0)
# print(merge4.ndim) # 3
# print(merge4)
# [[[ 0  1  2]  
#   [ 3  4  5]] 

#  [[ 6  7  8]  
#   [ 9 10 11]] 

#  [[12 13 14]  
#   [15 16 17]]]


merge5 = np.stack([arr1, arr2, arr3], axis=1)
# print(merge5.ndim) # 3
# print(merge5)
# [[[ 0  1  2]  
#   [ 6  7  8]  
#   [12 13 14]] 

#  [[ 3  4  5]  
#   [ 9 10 11]  
#   [15 16 17]]]

merge6 = np.stack([arr1, arr2, arr3], axis=2)
# print(merge6.ndim) # 3
# print(merge6)
# [[[ 0  6 12]  
#   [ 1  7 13]  
#   [ 2  8 14]] 

#  [[ 3  9 15]  
#   [ 4 10 16]  
#   [ 5 11 17]]]

# merge7 = np.stack([arr1, arr2, arr3], axis=3) 
# numpy.AxisError: axis 3 is out of bounds for array of dimension 3