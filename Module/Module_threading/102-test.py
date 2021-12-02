from threading import Thread, Lock
import time

count = 10
lock = Lock() # ?그냥 쓰면 안돼?

class developer(Thread) :
    def __init__(self, name) : # 초기화를 하고
        Thread.__init__(self) # (재)정의를 한다.
        self.name = name
        self.fixed = 0
    def run(self) :
        global count
        while 1 :
            lock.acquire() # lock
            if count > 0 :
                count -= 1
                lock.release # unlock
                self.fixed += 1
                time.sleep(0.1) # 음... 텀?
            else :
                lock.release()
                break


dev_list = []
for name in ['NIRVANA', 'OFFSPRING', 'GREENDAY'] :
    dev = developer(name) # 스레드 생성
    dev_list.append(dev)
    dev.start() # 스레드 시작 run()은 어디갔죠?
    for dev in dev_list :  
        dev.join()
        print(dev.name, 'fixed', dev.fixed)
