import numpy as np

#ndarray가 아닌 array이다.
l = [1,2,3,4,5]
npa1 = np.array(l, dtype=np.float)
print(npa1)

npa2 = np.array([[1,2,3],[4,5,6]])
print(npa2.shape) # (2, 3)
print(npa2.ndim) # 2
print(npa2.dtype) # int32

print(npa2.itemsize) # 4 # 각 원소의 데이터 크기
print(npa2.size) # 6
print(npa2.strides) # (12, 4) # 한 행의 데이터 크기, 각 원소의 데이터 크기

print(bool((npa2.shape[1] * npa2.itemsize) == npa2.strides[0])) # True
print(bool(npa2.itemsize == npa2.strides[1])) # True

# 3차원 배열에서 실험
npa3 = np.zeros((3,4,5), dtype=np.int32)
print(npa3.itemsize) # 4
print(npa3.strides)  # (80, 20, 4)
print(npa3[0].strides) # (20, 4)
print(npa3[0][0].strides) # (4,) ???
print((npa3[0][0].strides)[0]) # 4
print((npa3[0][0].strides)[1]) # IndexError: tuple index out of range