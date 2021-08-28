import decimal

a1 = decimal.Decimal(3.14)
b2 = decimal.Decimal(0.86)
print(a1 + b2) # 8.699999999999999733546474090

a2 = decimal.Decimal('3.14')
b2 = decimal.Decimal('0.86')
print(a2 + b2) # 4.00

# '-' '*' '/' 생략

a3 = decimal.Decimal(3)
b3 = decimal.Decimal(2)
print(a3 % b3) # 1

# 내장 자료형과도 가능

a4 = decimal.Decimal(3)
b4 = 4

print(a4 + b4) # 7 

# 심지어 인자로도 전달된다.

def testPow(a) :
    return a*a
a5 = decimal.Decimal(8)
print(testPow(a5)) # 64