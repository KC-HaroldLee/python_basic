#정적 메소드와 클래스 메소드
class MyClass:
    def __init__(self, value):
        self.Value = value
        print("Class is created! Value = ", value)

    def __del__(self):
        print("Class is deleted!")

def foo():
    d = MyClass(10)

foo()
