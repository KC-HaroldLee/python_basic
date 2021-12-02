import numpy as np

a = np.zeros((5,5), np.uint8)
# print(a)

for i in range(5) :
    a[i][i] = 2

# print(a)

# print(a!= 0) # T 대각선
# print(a!= 1) # 모두 T
# print(a!= 2) # F 대각선


boolNpa0 = np.zeros((5,5), np.bool) # dtype = bool
boolNpa1 = a!= 0 # dtype = bool
boolNpa2 = (a!= 1) # dtype = bool
boolNpa3 = ((a!= 2)) # dtype = bool


# any() 하나라도 True가 있다면
print(boolNpa0.any()) # False
print(boolNpa1.any()) # True
print(boolNpa2.any()) # True
print(boolNpa3.any()) # True

# all() 모두 True라면
print(boolNpa0.all()) # False
print(boolNpa1.all()) # False
print(boolNpa2.all()) # True
print(boolNpa3.all()) # False

# 도움이 필요할 때
help(np.ndarray.any)
print(help(np.ndarray.any))