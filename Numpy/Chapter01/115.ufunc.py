import numpy as np

print(type(np.add)) # <class 'numpy.ufunc'>
print(type(np.sort)) # <class 'function'>

# 예시
a = np.array([1,2,3,4])
b = np.add(a,a)
c = np.add.accumulate(a)

print(a) # [1 2 3 4]
print(b) # [2 4 6 8]
print(c) # [ 1  3  6 10]