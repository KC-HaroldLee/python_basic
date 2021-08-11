class C(object):
    def __init__(self, v):
        self.value = v

c1 = C(10)
print(c1.value)
c1.value = 20
print(c1.value)
