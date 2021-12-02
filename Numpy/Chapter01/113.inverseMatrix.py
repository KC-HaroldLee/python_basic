import numpy as np
from numpy import linalg

mat0 = np.mat([[1,2,3],[4,5,6],[7,8,9]]) 
mat1 = np.mat([[1,2],[3,4]]) 
mat2 = np.mat([[1,2],[3,4],[5,6]]) 
mat3 = np.mat([[1,2],[3,4],[5,6],[7,8]]) 

matList = [mat0, mat1, mat2, mat3]

idx = 0
for mat in matList :
    try :
        print('{0}번째 mat 변환 중'.format(idx))
        print(linalg.inv(mat))
        print('---------------------------------')
    except linalg.LinAlgError : 
        print('{0}번째 mat에서 linalg.LinAlgError 발생!'.format(idx))
    idx += 1

print('변환 끝')


