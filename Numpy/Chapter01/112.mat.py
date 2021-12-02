import numpy as np

# 2차원 매트릭스를 만든다.

mat1 = np.mat('1,2,3 ; 4,5,6 ; 7,8,9') 
# <class 'numpy.matrix'> 
# 문자열 형태로 만들때는 ';'를 활용한다.
# mat1 = np.mat('1,2,3 ; 4,5,6 ; a,b,c')
# ValueError: malformed node or string: <_ast.Name object at 0x000001E114289A48>
# 당연 숫자이외의 다른 문자열이 들어가면 안된다.

mat2 = np.mat([[1,2,3],[4,5,6],[7,8,9]]) 
# <class 'numpy.matrix'>

# 클래스가 바뀐다.
# 내용은 그대로
print(mat1.A) # <class 'numpy.ndarray'>
print(mat1.getA()) # <class 'numpy.ndarray'>

# 열과 축을 변환한다.
# 클래스는 그대로
print(mat1.H) # <class 'numpy.matrix'>
print(mat1.T) # <class 'numpy.matrix'>
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]
