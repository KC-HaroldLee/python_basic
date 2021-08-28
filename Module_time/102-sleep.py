import time

t1 = time.time()
time.sleep(5) # 5초간 sleep
t2 = time.time()

spendtime = (t2 - t1)
print('t1 = ', t1)
print('t2 = ', t2)
print('dur = ', spendtime)
