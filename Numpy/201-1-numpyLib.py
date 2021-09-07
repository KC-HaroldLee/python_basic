# 데이터 형식만 이걸 쓰고 numpy의 메소드를 많이 사용하니까 이렇게는 하지 말것
# from numpy import ndarray

import numpy as np


array = np.array([
    [[1,2,3], [4,5,6]],
    [[7,8,9],[0,0,0]]
    ])

print(array)

print('ndim : ', array.ndim)
print('shape : ', array.shape)
print('dtype : ', array.dtype)