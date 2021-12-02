import numpy as np

vector1 =  np.array([43])
print(vector1) # [43]
print(type(vector1)) # <class 'numpy.ndarray'>
print(vector1.ndim) # 1
print(vector1.shape) # (1,)

vector2 = np.arange(10)
print(vector2) # [0 1 2 3 4 5 6 7 8 9]
print(vector2.dtype) # int32

vector3 = np.arange(10.5, 20.5, 0.5) # a부터 b까지 c간격으로
print(vector3) # [10.5 11.  11.5 12.  12.5 13.  13.5 14.  14.5 15.  15.5 16.  16.5 17.
#  17.5 18.  18.5 19.  19.5 20. ]
print(vector3.dtype) # float64
