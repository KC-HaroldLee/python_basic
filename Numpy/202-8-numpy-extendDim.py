import numpy as np

arr1 = np.arange(4)
print(arr1.ndim) # 1
arr2 = [arr1]
# print(arr2.ndim) # AttributeError: 'list' object has no attribute 'ndim'

axis1 = arr1[np.newaxis]
print(axis1.ndim) # 2
print(axis1) # [[0 1 2 3]]

axis2 = arr1[:, np.newaxis]
print(axis2.ndim) # 2
print(axis2)
# [[0]
#  [1]
#  [2]
#  [3]]

# axis1111 = arr1[np.newaxis[np.newaxis[np.newaxis[np.newaxis[np.newaxis[np.newaxis]]]]]]
# print(axis1111.ndim) # 2
# print(axis1111) # [[0 1 2 3]]

# axis2222 = arr1[:, np.newaxis[:, np.newaxis[:, np.newaxis[:, np.newaxis[:, np.newaxis]]]]]
# print(axis2222.ndim) # 2
# print(axis2222) # [[0 1 2 3]]