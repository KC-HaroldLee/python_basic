import numpy as np

np.array(object, dtype=None, copy=True, order='K', subok = False, ndmin = 0) 

# arr1 = np.array([[[[1,2,3],[1,2,3]]]], order='K', subok = False)
arr1 = np.array([[[[1,2,3],[1,2,3]]]], order='K', subok = True)

print('ndim : ', arr1.ndim) # 4 
print('shape : ', arr1.shape) # (1, 1, 2, 3)  
print('dtype : ', arr1.dtype) # int32

print(type(arr1[0])) # <class 'numpy.ndarray'>
print(type(arr1[0][0])) # <class 'numpy.ndarray'>
print(type(arr1[0][0][0])) # <class 'numpy.ndarray'>
print(type(arr1[0][0][0][0])) # <class 'numpy.int32'>  