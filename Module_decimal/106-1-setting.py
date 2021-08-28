import decimal
d1 = decimal.Decimal('3.14')
d2 = decimal.Decimal(7)
print(d1 / d2) # 0.4485714285714285714285714286

# 현재 환경설정을 알아보는 방법
print(decimal.getcontext())
# Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, 
# Emax=999999, capitals=1, clamp=0, flags=[Inexact, Rounded], 
# traps=[InvalidOperation, DivisionByZero, Overflow])
