import decimal

d1 = decimal.Decimal('3.14')
d2 = decimal.Decimal() # 0
# print(d1 / d2) # decimal.DivisionByZero: [<class 'decimal.DivisionByZero'>]

decimal.getcontext().traps[decimal.DivisionByZero] = 0 # 비활성화
print(d1 / d2) # Infinity (무한대 값)