import numpy as np

e1 = np.array([1,0,0,0])
e2 = np.array([0,1,0,0])
e3 = np.array([0,0,1,0])
e4 = np.array([0,0,0,1])

eList = [e1, e2, e3, e4]

for e in eList :
    print(np.linalg.norm(e))

    # 1.0
    # 1.0
    # 1.0
    # 1.0