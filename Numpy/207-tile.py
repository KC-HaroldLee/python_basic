import numpy as np

# np.tile(arrays, reps)
# 입력 배열을 반복해서 연결(?) reps은 튜플도 가능

a = np.array([[1,2],[3,4]])
print(a)
# [[1 2]
#  [3 4]]
b = np.tile(a, 1)
print(b)
# [[1 2]
#  [3 4]]

c = np.tile(a, 4)
print(c)
# [[1 2 1 2 1 2 1 2]
#  [3 4 3 4 3 4 3 4]]

d = np.tile(a, (4,4))
print(d)
# [[1 2 1 2 1 2 1 2]
#  [3 4 3 4 3 4 3 4]
#  [1 2 1 2 1 2 1 2]
#  [3 4 3 4 3 4 3 4]
#  [1 2 1 2 1 2 1 2]
#  [3 4 3 4 3 4 3 4]
#  [1 2 1 2 1 2 1 2]
#  [3 4 3 4 3 4 3 4]]