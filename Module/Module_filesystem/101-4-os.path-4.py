from os import path
import time

# os.path.getatime(path)
# 최근 a엑세스 시간을 나타낸다.
# 단 기준은 epoch...
timeFloat1 = path.getatime('D:\\workspace\\python-git\\python_ruby-study')
print(timeFloat1) # 1630204834.3076525
print(time.ctime(timeFloat1)) # Sun Aug 29 11:40:34 2021 ? 그냥 지금 시간인데 ?

timeFloat2 = path.getatime('G:\\dev\\apache-jmeter-5.4.1')
print(timeFloat2) # 1627570800.0
print(time.ctime(timeFloat2)) # Fri Jul 30 00:00:00 2021

# os.path.getmtime(path)
# 최근 m수정 시간을 나타낸다.

# os.path.getctime(path)
# 생성 c시간을 나타낸다

# os.path.getsize(path)
# 파일 크기를 반환
print(path.getsize('G:\\dev\\apache-jmeter-5.4.1\\bin\\ApacheJMeter.jar')) # 13410
