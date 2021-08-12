class Cs():
    count = 0
    def __init__(self):
        Cs.count = Cs.count + 1
    @classmethod # 쫌 귀찮네
    def getCount(cls):
        # return Cs.count
        return cls.count

inst1 = Cs()
inst2 = Cs()
inst3 = Cs()
inst4 = Cs()
inst5 = Cs()

print(Cs.getCount())
