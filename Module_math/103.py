# 수치 연산
import math
# celi(x)
# 올림연산(N>=x를 만족하는 가장 작은 정수를 반환) 
print(math.ceil(56.1)) # 57

# floor(x)
# 내림연산(N<=x를 만족하는 가장 큰수를 반환)
print(math.floor(56.5)) # 56

# round()는 math에 없다.
# math.round() < 없음
round(23.2) # 내장함수

# trunc(x)
# x의 정수부분만 반환한다.(버림 연산)
print(math.trunc(55.5)) # 55

# copysign(x, y) 
# 부호만 x에 복사해서 반환
print(math.copysign(-5.4, 1)) # 5.4

# fabs(x)
# x의 절대값을 반환
print(math.fabs(-53)) # 53.0

# factorial(x)
print(math.factorial(10)) # 3628800

# fmod(x, y)
# C라이브러리에 잇는 fmod()함수를 호출한다(?)
# 값이 x % y....
# 항상 동일하지 않다고 한다...
print(math.fmod(10, 3)) # 1.0
print(math.fmod(11, 3)) # 2.0
print(math.fmod(15, 3)) # 0.0
print(math.fmod(99, 98) ) # 1.0

# fsum(iterable)
# 입력받은 값의 값을 구한다.
l = [1,2,3,4,5,6,7,8,9,10]
print(math.fsum(l)) # 55.0

# modf(x)
# 소수, 정수로 튜플 형태로 분리한다.
print(math.modf(-6.5)) # (-0.5, -6.0)
print(math.modf(123.4)) # (0.4000000000000057, 123.0)
print(math.modf(1.2)) # (0.19999999999999996, 1.0)
print(math.modf(math.pi*1)) # (0.14159265358979312, 3.0)
