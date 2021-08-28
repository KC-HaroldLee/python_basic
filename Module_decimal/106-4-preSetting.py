import decimal
print(decimal.DefaultContext)
# Context(prec=28, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, 
# capitals=1, clamp=0, flags=[], traps=[InvalidOperation, DivisionByZero, Overflow])
# 아무것도 세팅 안했을 때 getContext()와 같다

print(decimal.BasicContext) 
# Context(prec=9, rounding=ROUND_HALF_UP, Emin=-999999, Emax=999999,
# capitals=1, clamp=0, flags=[], traps=[Clamped, InvalidOperation, DivisionByZero, Overflow, Underflow])
# 소수점 자리수가 편(?)해진다. ounding의 변화. traps에 하나 추가. Underflow가 추가된다

print(decimal.ExtendedContext) # 확장이라는데 흠...
#Context(prec=9, rounding=ROUND_HALF_EVEN, Emin=-999999, Emax=999999, capitals=1, clamp=0, flags=[], traps=[])

print(type(decimal.ExtendedContext)) # <class 'decimal.Context'>
print(type(decimal.getcontext())) # <class 'decimal.Context'>