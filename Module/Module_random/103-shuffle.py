import random

l = list(range(20))
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

s = random.sample(l, 5) # 두번째 인자는 개수
print(l)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(s)
# [14, 15, 19, 4, 5]

random.shuffle(l)
print(l)
# [4, 19, 8, 6, 1, 0, 13, 3, 7, 17, 2, 18, 10, 16, 9, 15, 14, 11, 5, 12]