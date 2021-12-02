import numpy as np

la1 = np.linspace(1,21,5, dtype=np.int32, retstep=True)
print (la1)
# (array([ 1,  6, 11, 16, 21]), 5.0)
print(la1[0])
print(la1[1])

la2 = np.linspace(1,10,10, retstep=True)
print(la2)
# (array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.]), 1.0)
print(la2[0])
print(la2[1])