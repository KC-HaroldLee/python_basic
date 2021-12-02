import numpy as np

# 버전 확인
print(np.__version__) # 1.19.5

# 클래스 이름 확인
print(np.__name__) # numpy

# 특정 메소드 확인
for i in dir(np.ndarray) :
    if not i.startswith("__") :
        if type(np.ndarray.__dict__[i]) != type(np.ndarray.var) :
            print(i)
# T base ctypes data dtype flags flat imag itemsize nbytes ndim real shape size strides


