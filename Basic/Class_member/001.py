class Cs:
    @staticmethod
    def static_method():
        print("스태틱 메소드")
    @classmethod
    def class_method(cls):
        print("클래스 메소드")
    def instance_method(self):
        print("인스턴스 메소드")



inst = Cs()
Cs.static_method()
Cs.class_method()
inst.instance_method()
