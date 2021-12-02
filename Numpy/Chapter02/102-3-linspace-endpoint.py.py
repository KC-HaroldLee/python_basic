import numpy as np

la1 = np.linspace(1,10,10, endpoint=False, retstep=True)
print (la1)
# (array([1. , 1.9, 2.8, 3.7, 4.6, 5.5, 6.4, 7.3, 8.2, 9.1]), 0.9)

la2 = np.linspace(1,10,10, endpoint=True, retstep=True)
print (la2)
# (array([ 1.,  2.,  3.,  4.,  5.,  6.,  7.,  8.,  9., 10.]), 1.0)