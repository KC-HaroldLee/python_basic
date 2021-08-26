# 클래스의 생성과 소멸
class MyClass :
    def __init__ (self, value) : # 기억나지? self
        # self.Value(value)
        self.Value = value
        print('클래스 생성!')
        print('Value = ', value)
    
    def __del__ (self) :
        print('클래스 소멸')
        print('그리고 궁금해서 쳐보는', self)

# mc = MyClass() - 오답

def test() :
    mc = MyClass(10)

test()
