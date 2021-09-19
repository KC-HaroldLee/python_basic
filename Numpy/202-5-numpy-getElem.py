import numpy as np

arr1 = np.array([[1,2,3],[4,5,6],[6,7,8]], order='K', subok = True)

print(arr1[-1]) # [6 7 8]
print(arr1[1]) # [4 5 6]