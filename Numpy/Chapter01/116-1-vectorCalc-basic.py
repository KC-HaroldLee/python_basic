import numpy as np

a = np.arange(6, 10) # [6,7,8,9]
b = np.arange(10, 14) # [10, 11, 12, 13]

c = a * b # [ 60  77  96 117]

d = a[:, np.newaxis] # [[6],[7],[8],[9]]
e = b[np.newaxis, :]

print(bool(d.ndim == e.ndim)) # True
print(d @ e)
print(np.multiply(d, e)) # 도 같음
# [[ 60  66  72  78]
#  [ 70  77  84  91]
#  [ 80  88  96 104]
#  [ 90  99 108 117]]

d2 = a[:, np.newaxis, np.newaxis] 
# [[[6]]
#  [[7]]
#  [[8]]
#  [[9]]]
d3 = a[np.newaxis, np.newaxis, :]
# [[[6 7 8 9]]]