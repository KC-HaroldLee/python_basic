import numpy as np

# 변환과 기본 데이터형
l = [1,2,3,4,5]
print(type(l)) # <class 'list'>

nda1 = np.array(l)
print(type(nda1)) # <class 'numpy.ndarray'>
print(nda1.dtype) # int32
nda1_1 = np.ndarray(l, dtype=np.uint8)
print(nda1_1.dtype) # uint32

t = (4,6)
nda2 = np.ndarray(t)
print(type(nda2)) # <class 'numpy.ndarray'>
print(nda2.dtype) # float64

print(nda2)
# [[6.23042070e-307 4.67296746e-307 1.69121096e-306 9.34609111e-307 1.42413555e-306 1.78019082e-306]
#  [1.37960147e-306 1.33511562e-306 2.22518251e-306 1.33511969e-306 1.78022342e-306 1.05700345e-307]
#  [1.11261502e-306 1.42410839e-306 7.56597770e-307 6.23059726e-307 1.42419530e-306 1.37962185e-306]
#  [1.37962049e-306 1.24610723e-306 1.02359984e-306 1.60220800e-306 2.22522596e-306 0.00000000e+000]]

nda3 = np.ndarray((2,2))
print(nda3)
# [[6.23042070e-307 3.56043053e-307]
#  [1.37961641e-306 6.23039354e-307]]

nda4 = np.zeros(t)
print(nda4)
# [[0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0. 0.]]



# 레퍼런스 확인
print(nda1) # [1 2 3 4 5] # <class 'numpy.ndarray'>
print(nda1.data) # <memory at 0x0000018FEDDD9B88>
print(nda1.data.obj) # [1 2 3 4 5] # <class 'numpy.ndarray'>
print(nda1.data.obj.data) # [1 2 3 4 5] # <class 'numpy.ndarray'> - 같음

# 복제가아닌 별칭(참고하는 데이터는 같음)
nda1_ref = nda1
print(bool(nda1.data==nda1_ref.data)) # True
nda1[0] = 100
print(bool(nda1[0]==nda1_ref[0])) # True


# 진짜 복제
nda_copy = np.ndarray(nda1)
print(bool(nda1.data==nda_copy.data)) # False