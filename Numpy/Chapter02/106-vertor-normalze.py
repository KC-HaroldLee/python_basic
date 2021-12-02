import numpy as np

v_3 = np.array([1,2,3])
v_3_n = np.linalg.norm(v_3) # 3.7416573867739413

# 이 벡터에 벡터의 크기를 나눈다.
v_3_u = v_3 / v_3_n
# [0.26726124 0.53452248 0.80178373]
print(np.linalg.norm(v_3_u)) # 1.0