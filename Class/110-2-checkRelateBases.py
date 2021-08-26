#관계 확인
class Parent :
    def __bases__(self) :
        print('재정의 성공~!')
# class Child(Parent) :
#     pass
# class Uncle :
#     pass
# class Cousin(Uncle) :
#     pass

# 앞뒤로 바꿔본다
p = Parent()
print(p.__bases__)
# print(Child.__bases__)
# print(Uncle.__bases__)
# print(Cousin.__bases__)
