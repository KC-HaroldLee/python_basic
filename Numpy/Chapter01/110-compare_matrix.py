import numpy as np

print(np.ndarray.__bases__) # (<class 'object'>,)
print(np.matrix.__bases__) # (<class 'numpy.ndarray'>,)

npa1 = np.array([1,2,3,4,5,6,7,8])
mtrx1 = np.matrix([1,2,3,4,5,6,7,8])

print(npa1.shape) # (8,)
print(mtrx1.shape) # (1, 8)


npa2 = npa1.reshape(2,4)
mtrx2 = mtrx1.reshape(2,4)

print(npa2.shape) # (2,4)
print(mtrx2.shape) # (2,4)


# mtx3 = mtx1.reshape(2,4,3) # ValueError

mtrx3 = np.asmatrix(npa1)
mtrx4 = mtrx3.reshape(2,4)
print(mtrx4)

try : 
    mtrx4 * mtrx4 
    # ValueError: shapes (2,4) and (2,4) not aligned: 4 (dim 1) != 2 (dim 0)
except ValueError as e : 
    print (e)
    print(np.multiply(mtrx4,mtrx4))
    # [[ 1  4  9 16]
    #  [25 36 49 64]]
    
mtrx5 = np.matrix([[1,2],[3,4]])
print(mtrx5*mtrx5)
# [[ 7 10]
#  [15 22]]

mtrx6 = np.matrix([[1,2,3,4],[1,2,3,4]])
mtrx7 = np.matrix([[1,2],[3,4],[1,2],[3,4]])
print(mtrx6*mtrx7)
# [[ 7 10]
#  [15 22]]
# [[22 32]
#  [22 32]]

np.multiply(mtrx6,mtrx7)
# ValueError: operands could not be broadcast together with shapes (2,4) (4,2)