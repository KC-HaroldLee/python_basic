import numpy as np

# npa = np.zeros((2,3,4), dtype=np.int32)
# npa = np.array((2,3,4))
npa = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[0,0,0]]])

print(npa.__array_interface__)
# {'data': (1291377711664, False),
#  'strides': None, 
#  'descr': [('', '<i4')],
#  'typestr': '<i4',
#  'shape': (2, 2, 3),
#  'version': 3}

print(npa.__array_interface__['shape']) # (2, 2, 3)
