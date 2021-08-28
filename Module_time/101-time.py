import time
# epoch기준 (타임스탬프)
print(time.time())

# UTC기준
print(time.gmtime()) 
# time.struct_time(tm_year=2021, tm_mon=8, tm_mday=27, tm_hour=16, tm_min=56, tm_sec=37, tm_wday=4, tm_yday=239, tm_isdst=0)


# 시스템 기준 
print(time.localtime()) 
# time.struct_time(tm_year=2021, tm_mon=8, tm_mday=28, tm_hour=1, tm_min=56, tm_sec=37, tm_wday=5, tm_yday=240, tm_isdst=0)


# 타임스탬프를 struct_time 시퀀스 객체로 변환
print(time.gmtime(9154314321))
# time.struct_time(tm_year=2260, tm_mon=2, tm_mday=2, tm_hour=17, tm_min=5, tm_sec=21, tm_wday=3, tm_yday=33, tm_isdst=0)

# 반환해서 써먹기
# tm_year / tm_mon / tm_mday=27 / tm_hour=17 / tm_min=4 / tm_sec=31 / tm_wday=4 / tm_yday=239 / tm_isdst
t = time.localtime()
print(t.tm_hour)

# 변환해서 써먹기
print(time.asctime(t)) # Sat Aug 28 02:06:05 2021
print(time.mktime(t)) # 1630083987.0


