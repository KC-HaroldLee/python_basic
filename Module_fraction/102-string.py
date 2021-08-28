import fractions

# 문자열로 활용하기

a = fractions.Fraction('6/16')
print(a) # 3/8
print(type(a)) # <class 'fractions.Fraction'>

b = fractions.Fraction('3.14')
print(b) # 157/50

c = fractions.Fraction('          4/5')
print(c) # 4/5
