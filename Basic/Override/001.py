class C1:
    def m(self):
        return 'C1.m 입니다'

class C2(C1):
    def m(self):
        return super().m() + 'C1에게 상속 받았지만 C2.m 입니다'

o = C2()
print(o.m())
