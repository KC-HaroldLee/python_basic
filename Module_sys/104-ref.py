# sys.getrefcount(object)
# 객체의 레퍼런스 카운트 값을 반환한다.
# 일반적으로 임시객체가 참조하는 경우도 포함되어 1보다 크다
import sys

t1 = 'test refcount'
print(sys.getrefcount(t1)) # 4

t2 = t1
print(sys.getrefcount(t2)) # 5

t3 = t2
print(sys.getrefcount(t3)) # 6

t5 = 1
print(sys.getrefcount(t5)) # 90

