#계산기 만들기
class Cal(object):
    def __init__(self, v1, v2):
        # prv(self)
        # print(v1, v2)
        self.v1 = v1
        self.v2 = v2
    def add(self):
        return self.v1+self.v2
    def substract(self):
        return self.v1-self.v2
    def setV1(self, v):
        # dataType = type(v)
        # print(dataType)
        # if dataType == "<class 'int'>":
        if isinstance(v, int):
            self.v1 = v
            print(self.v1, "은 이제 self.v1")
        # elif isinstance(v, str):
        #     print("str, 문자열이네여")
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

c1 = Cal(10,10)

c1.setV1(5)
c1.setV1('5')

c1.v2 = 7
