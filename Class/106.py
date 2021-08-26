# 접근 막기
class CounterManager:
    __insCount = 0
    def __init__(self):
        CounterManager.__insCount += 1

    def staticPrintCount():
        print("Instance Count: %d" % CounterManager.__insCount)
    SPrintCount = staticmethod(staticPrintCount)

print(CounterManager.__insCount)

# a, b, c = CounterManager(), CounterManager(), CounterManager()
# CounterManager.SPrintCount()