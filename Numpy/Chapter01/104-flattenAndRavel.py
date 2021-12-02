import numpy as np

npa = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,0,0]]])
print(npa.ndim)

# flatten()
# 1차원으로 변경
npa_flatten = npa.flatten()
print(npa_flatten) # [1 2 3 4 5 6 7 8 9 0 0 0]
print(npa_flatten.ndim) # 1
print(bool(npa.data==npa_flatten.data)) # False

# ravel()
# 뷰 역할 내부데이터를 그대로 반환한다.
npa_raveled = npa.ravel()
print(npa_raveled) # [1 2 3 4 5 6 7 8 9 0 0 0]
print(npa_raveled.ndim) # 1
print(bool(npa.data==npa_raveled.data)) # False

npa[0][0][0] = 99

print(npa) # [[[99  2  3], [ 4  5  6]], [[ 7  8  9], [ 0  0  0]]]
print(npa_flatten) # [1 2 3 4 5 6 7 8 9 0 0 0]
print(npa_raveled) # [99  2  3  4  5  6  7  8  9  0  0  0]

npa_flatten[0] = 11

print(npa) # [[[99  2  3], [ 4  5  6]], [[ 7  8  9], [ 0  0  0]]]
print(npa_flatten) # [11 2 3 4 5 6 7 8 9 0 0 0]
print(npa_raveled) # [99  2  3  4  5  6  7  8  9  0  0  0]

npa_raveled[0] = 77

print(npa) # [[[77  2  3], [ 4  5  6]], [[ 7  8  9], [ 0  0  0]]]
print(npa_flatten) # [1 2 3 4 5 6 7 8 9 0 0 0]
print(npa_raveled) # [99  2  3  4  5  6  7  8  9  0  0  0]
