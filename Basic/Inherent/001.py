class Class1(object):
    def method1(self):
        return 'm1'

c1 = Class1()
print(c1, c1.method1())

class Class2(Class1):
    def method2(self):
        return 'm2'

c2 = Class2()
print(c2, c2.method1())
print(c2, c2.method2())
