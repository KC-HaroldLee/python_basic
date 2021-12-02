#계산기 만들기
class Cal(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def add(self):
        return self.v1+self.v2
    def substract(self):
        return self.v1-self.v2
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
            print(self.v1, "은 이제 self.v1")
        else:
            print("int도 str가 아닙니다.")
    def setV2(self, v):
        if isinstance(v, int):
            self.v2 = v
            print(self.v2, "은 이제 self.v2")
        else:
            print("int가 아닙니다.")
    def getV1(self, v):
        return self.v1
    def getV2(self, v):
        return self.v2

class CalMultiply(Cal):
    def multiply(self):
        return self.v1 * self.v2

c1 = CalMultiply(10, 5)
print(c1.add())
print(c1.multiply())
