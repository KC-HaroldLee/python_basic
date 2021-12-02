import numpy as np

# 벡터 크기 구하기

# 만약 피타고라스처럼 한 단계씩 구하면?
v = np.arange(3,5) # [3 4]
v_p = np.power(v,2) # [9 16]
print (np.sum(v_p)) # 25
v_r = np.sqrt(np.sum(v_p)) 
print (v_r)# 5.0

# hypot()을 사용
# 두개의 인자를 받는다.
print(np.hypot(v[0],v[1])) # 5.0
# print(np.hypot(v[0],v[1],v[1]))
 # TypeError: return arrays must be of ArrayType

# 더 많은 원소를 위해서는 # np.linalg.norm()을 활용
print(np.linalg.norm(v)) # 5.0
v2 = np.arange(3,6)
print(np.linalg.norm(v2)) # 7.0710678118654755