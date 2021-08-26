class Tiger:
    def Jump(self):
        print("호랑이처럼 멀리 점프하기")
    def Bite(self):
        print("호랑이 이빨~")

class Lion:
    def Bite(self):
        print("사자처럼 한입에 꿀꺽하기")

class Liger(Tiger, Lion):
    def Play(self):
        print("라이거만의 사육사와 재미있게 놀기")

l = Liger()
l.Bite()

#print(l.__mro__) # 안됨
print(Liger.__mro__) # Method Resolution Order