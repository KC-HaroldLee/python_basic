import numpy as np


# np.eye(n, m, k=0, dtype=None) # n * m 크기의 k만큼 오프셋 된 행렬 생성
a = np.eye(4, 5, k=1, dtype=np.uint32)
# print(a)
# [[0 1 0 0 0]
#  [0 0 1 0 0]
#  [0 0 0 1 0]
#  [0 0 0 0 1]]

# np.identity(n, dtype=None) # n * n 크기의 단위 행렬 생성
b = np.identity(5, np.float32)
# print(b)
# [[1. 0. 0. 0. 0.]
#  [0. 1. 0. 0. 0.]
#  [0. 0. 1. 0. 0.]
#  [0. 0. 0. 1. 0.]
#  [0. 0. 0. 0. 1.]]

# np.ones([n, m, ...], dtype=None) # 지정된배열 크기로 1이 채워진 배열 생성
c = np.ones([4,2,7], np.uint8) # 가장 바깥 쪽부터 4,2,7
# print(c)
# [[[1 1 1 1 1 1 1]
#   [1 1 1 1 1 1 1]]

#  [[1 1 1 1 1 1 1]
#   [1 1 1 1 1 1 1]]

#  [[1 1 1 1 1 1 1]
#   [1 1 1 1 1 1 1]]

#  [[1 1 1 1 1 1 1]
#   [1 1 1 1 1 1 1]]]

d = np.ones_like(b, dtype=np.uint8)
# print(d)
# [[1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]]

e = np.ones_like(d, dtype=np.bool_)
# print(e)
# [[ True  True  True  True  True]
#  [ True  True  True  True  True]
#  [ True  True  True  True  True]
#  [ True  True  True  True  True]
#  [ True  True  True  True  True]]

f = np.ones_like(e, dtype=np.uint0)
# print(f)
#[[1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]
#  [1 1 1 1 1]]

# zeros, zeros_like 생략!

# np.full([n,m, ...], fill_value, dtype=None) # fill_value 로 채우기
g = np.full([1,2,3], 7, dtype=np.uint16)
# print(g)
# [[[7 7 7]
#   [7 7 7]]]

h = np.full([2,2], 99999999999, dtype=np.uint8)
# print(h) 
# [[255 255]
#  [255 255]]

i = np.full([3,3], -10, dtype=np.bool_)
# print(i)
# [[ True  True  True]
#  [ True  True  True]
#  [ True  True  True]]

j = np.full([4,4], -260, dtype=np.uint8)
# print(j)
# [[251 251 251 251]
#  [251 251 251 251]
#  [251 251 251 251]
#  [251 251 251 251]]


# np.ndarray.fill(object, value)
k = np.ndarray.fill(j[0], 200)
# print(k) # None
# print(type(k)) # <class 'NoneType'>
# print(j)
# [[200 200 200 200] # 이쪽 줄이 바뀜
#  [252 252 252 252]
#  [252 252 252 252]
#  [252 252 252 252]]

# l = np.ndarray.fill([[1,2,3],[4,5,6]], 5) 
# TypeError: descriptor 'fill' for 'numpy.ndarray' objects doesn't apply to a 'list' object

# np.empty([n,m, ...], dtype=dtype)
# 초기화 되지 않은 배열을 생성
m = np.empty([2,5], dtype=np.uint8)
print(m)
n = np.empty([2,4], dtype=np.bool_)
print(n)
o = np.empty([2,6], dtype=np.float32)
print(o)


# np.diag(v, k=0) # 2차원 배열이하의 v배열울 k만큼 오프셋 된 대각 행렬 생성
# np.diagflat(v, k=0) # N차원 배열인 v배열을 1차원 으로 변경 후 k만큼 오프셋하여 대각 행렬 생성

p = np.diagflat(g, k=0)
print(p)
#[[7 0 0 0 0 0]
#  [0 7 0 0 0 0]
#  [0 0 7 0 0 0]
#  [0 0 0 7 0 0]
#  [0 0 0 0 7 0]
#  [0 0 0 0 0 7]]

# np.arange (start=0 , end, step=1, dtype=dtype)
# start ~ end-1 사이 값을 step만큼 띄운 배열 생성
q = np.arange(90, step=10)
print(q) # [ 0 10 20 30 40 50 60 70 80]


# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# start ~ end 값을 num만큼 생성한 1차원 배열 생성

# no.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None)
# start ~ end 값을 num만큼 생성 후  base만큼 띄운 로그 배열 생성