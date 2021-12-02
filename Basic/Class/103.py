# 상속관계 찾기
class Person:
    pass
class Bird:
    pass
class Student(Person): # 음? 클래스가 들어갈 수도?
    pass

# p, s = Person, Student - 오답
p, s = Person(), Student() # 익숙해질것
print('p is instance of Person : ', isinstance(p, Person)) # true
print('s is instance of Person : ', isinstance(s, Person)) # true

print('p is instance of object : ', isinstance(p, object)) # true
print('s is instance of object : ', isinstance(s, object)) # true

print('p is instance of Bird : ', isinstance(p, Bird)) # flase

print('int is instance of object', isinstance(int, object)) # true
print('bool(ean) is instance of object', isinstance(bool, object)) # true
print('float is instance of object', isinstance(float, object)) # true
print('str(ing) is instance of object', isinstance(str, object)) # true
print('list is instance of object', isinstance(int, object)) # true

