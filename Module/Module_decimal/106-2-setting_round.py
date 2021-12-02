import decimal

d1 = decimal.Decimal('3.14')
d2 = decimal.Decimal(7)

# 소수점 반올림 위치 지정
decimal.getcontext().prec = 7
print(d1 / d2) # 0.4485714

# 강제 올림
decimal.getcontext().rounding = decimal.ROUND_CEILING
print(d1 / d2) # 0.4485715

# 그 외의 것들
decimal.ROUND_05UP
decimal.ROUND_FLOOR
decimal.ROUND_HALF_UP
decimal.ROUND_HALF_DOWN
decimal.ROUND_HALF_EVEN
decimal.ROUND_UP
decimal.ROUND_DOWN