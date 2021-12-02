# 아래는 import하지 않고 사용할 수 있다.

# sum(iterable , [start])
# 단순 총 합계
l = [1,2,3,4,5,6,7,8,9]
print(sum(l)) # 45
print(sum(l , 1000)) # 1045

# max(iterable), min(iterable), abs()
print(max(l),',',min(l)) # 9 , 1
print(abs(-50)) # 50

# pow()
print(pow(2,10)) # 1024

# round()
print(round(55.555555)) # 56
print(round(55.555555, 2)) # 55.56
print(round(55.555555, 4)) # 55.5556
print(round(55.555555, -1)) # 60.0

# divmod(a,b)
# 나눠서 몫과 나머지를 튜플 형태로 반환
print(divmod(5,2)) # (2, 1)