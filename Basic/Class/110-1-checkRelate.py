#관계 확인

class Parent :
    pass
class Child(Parent) :
    pass
class Uncle :
    pass
class Cousin(Uncle) :
    pass

# 앞뒤로 바꿔본다
print(issubclass(Parent, Child)) # False
print(issubclass(Child, Parent)) # True

# 부모 끼리
print(issubclass(Parent, Uncle)) # False

# 부모를 바꾼다
print(issubclass(Uncle, Child)) # False

# 그쪽 집안
print(issubclass(Uncle, Cousin)) # False
print(issubclass(Cousin, Uncle)) # True
