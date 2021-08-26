# 아래 오류 없애기
class CounterManager :
    insCount = 0
    def __init__ (self) :
        CounterManager.insCount +=1

    def staticPrintCount() : # 정적메서드 정의
        print("instance Count : ", CounterManager.insCount)

    SPrintCount = staticmethod(staticPrintCount) # 정적메서드 등록
        
    def ClassPrintClass(cls): # 클래스매서드 정의(암묵적으로 첫번째 인자는 클래스를 받음)
        print("instance Count : ", cls.insCount)

    CPrintCount = classmethod(ClassPrintClass) #클래스메서드 등록
    
a, b, c= CounterManager(), CounterManager(), CounterManager()

CounterManager.SPrintCount
b.SPrintCount()
CounterManager.CPrintCount()
b.CPrintCount()