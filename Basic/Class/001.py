#계산기 만들기
class Cal(object):
    def __init__(self, int1, int2):
        # print(self)
        print(int1, int2)
        self.int1 = int1
        self.int2 = int2
    def add(self):
        return self.int1+self.int2

c1 = Cal(10,10)
print(c1.add())
# print(c1.substract())

c2 = Cal(30,20)
# print(c2.add())
# print(c2.substract())
