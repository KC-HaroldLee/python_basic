class Cal(object):
    _history = []
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
    def add(self):
        result = self.v1+self.v2
        # Cal._history.append("add : " + str(result))
        Cal._history.append("add : %d+%d=%d" % (self.v1, self.v2, result))
        return result
    def substract(self):
        return self.v1-self.v2
    def setV1(self, v):
        if isinstance(v, int):
            self.v1 = v
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

    @classmethod
    def history(cls):
        for item in Cal._history:
            print (item)

c1 = Cal(10,10)

c1.add()
Cal.history()
