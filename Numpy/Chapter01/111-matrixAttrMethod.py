import numpy as np

npaDir = set(dir(np.ndarray))
mtrxDir = set(dir(np.matrix))

print(npaDir-mtrxDir) # set()
# print(mtrxDir-npaDir)
# {'A1', '_collapse', 'H', '__module__', 'getA', 'getT', 
# 'I', '_align', 'A', 'getI', '__dict__', 'getH', 'getA1'}