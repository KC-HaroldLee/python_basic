#정적 메서드, 클래스 메서드
class CounterManager :
    insCount = 10
    def __init__ (self) : # 인스턴스 객체가 생성되면 클래스 영역의 insCount변수 값이 증가
            CounterManager.insCount +=1
    def printInstanceCount():
        print("instanceCount : ", CounterManager.insCount)
    
a, b, c= CounterManager(), CounterManager(), CounterManager() # 세개가 호출되었으니
CounterManager.printInstanceCount() # 여기는 13!
b.printInstanceCount() # 암묵적으로 인스턴스 객체를 받기때문에 에러
# TypeError: printInstanceCount() takes 0 positional arguments but 1 was given