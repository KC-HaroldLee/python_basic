import random

# random.seed[x] 
# 시드가 있긴하다. 비울 경우 시스템 시간에 맞춤

# random.random()
# 기본 (0 <= r <= 1)
print(random.random()) # (0 <= r <= 1)

# random.uniform(a, b)
# 범위지정 (x <= r <= y)
print(random.uniform(3, 4)) # (3 <= r <= 4)

# random.gauss(m, sb)
# 평균과 표준편차 지정
for i in range(5) :
    print(random.gauss(1, 1.0))

# random.randrange([start], stop [,step])
# 임의의 정수 생성
print(random.randrange(20)) # (0 <= r <= 20)

# 옵션을 추가
print(random.randrange(10, 100, 10)) # (0 <= r <= 100) 중 10단위

# + 반복문 (중복 될 수도 있다.)
print([random.randrange(10) for i in range(5)]) # [5, 4, 7, 3, 1]

# 반복문 + (물론 중복 될 수 있다.)
for i in range(5) :
    print(random.randrange(10))
# 4
# 2
# 1
# 6
# 1

# random.sample(population, k)
# 중복없이 뽑아 낸다.
# k개 만큼의 아이템을 첫번째 인자에서 추출한다.

print(random.sample(range(20), 19))
# [6, 9, 14, 17, 1, 3, 13, 12, 19, 18, 5, 16, 0, 2, 7, 15, 11, 8, 10]

print(random.sample(range(20), 21))
# ValueError: Sample larger than population or is negative