# a = 1
class Cls :
    a = 2
    def m(self):
        # a = 3
        return a

c1 = Cls()
print(c1.m())
