#효율적인 순회방법 (시간측정!!!!)
import time

list = range(100000)

# for문으로 각 인자를 출력하는 경우
t = time.mktime(time.localtime())
for item in list :
    print(item, end = '\n')
t1 = time.mktime(time.localtime())-t
print() #개행
# join()매서드
t = time.mktime(time.localtime()) # 계속 재정의
print('\n'.join(str(item) for item in list))
t2 = time.mktime(time.localtime())-t

print("t1 = takes {0} sec".format(t1))
print("t2 = takes {0} sec".format(t2))