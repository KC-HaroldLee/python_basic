# 그외의 함수들
import numpy as np

# np.reshape(array, newshape, order ='C')
# 입력 배열의 새로운 모양을 설정 (newshape는 정수 또는 정수형 튜플)
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

b = np.reshape(a, (2,6), order='C')
print(b)
# [[ 1  2  3  4  5  6] 
#  [ 7  8  9 10 11 12]]

c = np.reshape(a, (6,2), order='C')
print(c)
# [[ 1  2]
#  [ 3  4]
#  [ 5  6]
#  [ 7  8]
#  [ 9 10]
#  [11 12]]

d = np.reshape(a, (3,-1), order='C')