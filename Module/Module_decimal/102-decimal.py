# Decimal도 객체가 있다.
# 음~ 그냥 데이터 형식의 한 종류라고 생각해보면서 배워본다.

from decimal import Decimal

a = Decimal(3)
print(a) # 3
print(type(a)) # <class 'decimal.Decimal'>

b = Decimal('1.2')
print(b) # 1.2
print(type(b)) # <class 'decimal.Decimal'>

c = Decimal(str(2/5))
print(c)

# d = Decimal(str('2/5')) # decimal.InvalidOperation: [<class 'decimal.ConversionSyntax'>]
# print(d)

e = Decimal(('-infinity')) # 음의 무한대
print(e) # -Infinity

f = Decimal('-0')
print(f) # -0 ?????