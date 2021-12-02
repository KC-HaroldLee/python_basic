import numpy as np


# np.stack(arrays, axis = 0)
# 입력배열들을 축을 기준으로 병합

a = np.array([[[1,1],[1,1]],[[1,1],[1,1]]])
b = np.array([[[2,2],[2,2]],[[2,2],[2,2]]])

c0 = np.stack((a,b), axis=0)
# print(c0)
# [[[[1 1], [1 1]], [[1 1], [1 1]]], [[[2 2], [2 2]], [[2 2], [2 2]]]]

c1 = np.stack((a,b), axis=1)
# print(c1)
# [[[[1 1], [1 1]], [[2 2], [2 2]]], [[[1 1], [1 1]], [[2 2], [2 2]]]]

c2 = np.stack((a,b), axis=2)
# print(c2)
# [[[[1 1], [2 2]], [[1 1], [2 2]]], [[[1 1], [2 2]], [[1 1], [2 2]]]]

c3 = np.stack((a,b), axis=3)
# print(c3)
# [[[[1 2], [1 2]], [[1 2], [1 2]]], [[[1 2], [1 2]], [[1 2], [1 2]]]]

# c4 = np.stack((a,b), axis=4) # axis 4 is out of bounds for array of dimension 4

d =(a+b)
# print (d)
# [[[3 3], [3 3]], [[3 3], [3 3]]]

e = np.array([[1,1],[1,1]])
f = np.array([[[2,2],[2,2]]])
# g = np.stack((e,f), axis=0) 
# ValueError: all input arrays must have the same shape

if e.shape == f.shape :
    g = np.stack((e,f), axis=0) 
    print(g)
else :
    print('두 배열 차원이 일치하지 않음')
    print('e의 차원 = {0}, f의 차원= {1}'.format(e.shape, f.shape))
    # 두 배열 차원이 일치하지 않음
    # e의 차원 = (2, 2), f의 차원= (1, 2, 2)
