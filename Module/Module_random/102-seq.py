# random.choice(seq)
# 입력받은 시퀀스 객체의 임의의 아이템을 반환한다.
# 만약 비어있다면... 아래 참조
import random

l = list(range(20)) # 캐스트 안하면 range 객체
print(random.choice(l)) # (0 <= r < 20)
print([random.choice(l) for i in range(3)]) # 중복은 나온다.

print(random.sample(l, 3)) # 중복 제거!