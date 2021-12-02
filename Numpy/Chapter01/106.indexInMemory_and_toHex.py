import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8]])
print(a.data.obj[0])
print(a.dtype)
print(a.data.hex())
# 01000000
# 02000000
# 03000000
# 04000000
# 05000000
# 06000000
# 07000000
# 08000000

