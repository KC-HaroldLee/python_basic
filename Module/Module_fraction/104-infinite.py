import math
from fractions import Fraction

# limit_denominator(최대 분모)분모를 제어한다

fract1 = Fraction.from_float(math.pi)
print(fract1) # 884279719003555/281474976710656
print(fract1.limit_denominator(10)) # 22/7
print(fract1.limit_denominator(100)) # 311/99
print(fract1.limit_denominator(1000)) # 311/99
print(fract1.limit_denominator(50000)) # 104348/33215
print(fract1.limit_denominator(1)) # 3 (;;;)