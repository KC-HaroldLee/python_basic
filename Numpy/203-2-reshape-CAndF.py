# 그외의 함수들
import numpy as np

# order F,C
a = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

b = np.reshape(a, (2,6), order='C')
print(b)
# [[ 1  2  3  4  5  6] 
#  [ 7  8  9 10 11 12]]

c = np.reshape(a, (2,6), order='F')
print(c)
# [[ 1  3  5  7  9 11]
#  [ 2  4  6  8 10 12]]

