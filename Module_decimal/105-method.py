import decimal

a = decimal.Decimal('64')
print(a.sqrt()) # 8

# e는 자연상수
b = decimal.Decimal('123.456')
print(b.exp()) # 4.132944352778093449576854412E+53

# ln()은 자연로그 결과
c = decimal.Decimal('123.456')
print(c.ln()) # 4.815884817283263883109232105

# compare()는 비교 -1, 0, 1 반환
d = decimal.Decimal

def compareTool(x, y) :
    x = decimal.Decimal(x)
    y = decimal.Decimal(y)
    result = x.compare(y)

    if result == -1 :
        print('나중이 크네')
    elif result == 1 :
        print('처음이 크네')
    elif result == 0 :
        print('같네')

compareTool(2,3) # 나중이 크네
compareTool(3,3) # 같네
compareTool(3,2) # 처음이 크네


# 원본을 기준으로 하는
# copy_abs() 원본의 절대값을 갖는 객체를 반환
# copy_negate() 원본의 음수값을 갖는 객체를 반환
# copy_sign(other) 원본 값의 인자의 부호(other)를 갖는 객체를 반환

e = decimal.Decimal(-2)
print(e.copy_abs()) # 2
print(e.copy_negate()) # 2
print(e.copy_sign(a)) # 2
print(e.copy_sign(e)) # -2

f = decimal.Decimal(5)
print(f.copy_abs()) # 5
print(f.copy_negate()) # -5
print(f.copy_sign(a)) # 5
print(f.copy_sign(e)) # -5


# 판별한다.
# is_signed() 부호비트가 있다면(즉 음수면) True를 반환(부호 부분이 1이면 True)
# is_finite() 유한수
# is_infinite() 무한수
# is_zero() 0, +0, -0 모두 True