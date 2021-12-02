import fractions

# fractions.Fraction(분자 = 0, 분모 = 1)
# fractions.Fraction(Fration 객체)
# fractions.Fraction(문자열)

a = fractions.Fraction(2,3)
print(a) # 2/3
print(type(a)) # <class 'fractions.Fraction'>

a1 = fractions.Fraction(12.12) # 소수도 가능
print(a1) # 6822953435466301/562949953421312

b = fractions.Fraction(a)
print(b) # 2/3
print(type(b)) # <class 'fractions.Fraction'>

c = fractions.Fraction(b, 2)
print(c) # 1/3 - 와... 오버로딩 쩐다
print(type(c)) # <class 'fractions.Fraction'>

d = fractions.Fraction('hello') # ValueError: Invalid literal for Fraction: 'hello'
print(d) # dead code
print(type(d)) # dead code

