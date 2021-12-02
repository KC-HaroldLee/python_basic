import time

t1 = time.ctime(123456789)
print('t = ', t1) 
# t1 =  Fri Nov 30 06:33:09 1973

print(time.strptime(t1))
# time.struct_time(tm_year=1973, tm_mon=11, tm_mday=30, tm_hour=6, tm_min=33, tm_sec=9, tm_wday=4, tm_yday=334, tm_isdst=-1)
print(type(time.strptime(t1)))
# <class 'time.struct_time'>

print(time.strptime(t1, ('%a %b %d %H:%M:%S %Y')))
# time.struct_time(tm_year=1973, tm_mon=11, tm_mday=30, tm_hour=6, tm_min=33, tm_sec=9, tm_wday=4, tm_yday=334, tm_isdst=-1)


t2 = time.strftime('%B %dth %A %I:%M', time.localtime())

print(time.strptime(t2, '%B %dth %A %I:%M'))
# time.struct_time(tm_year=1900, tm_mon=8, tm_mday=28, tm_hour=11, tm_min=29, tm_sec=0, tm_wday=5, tm_yday=240, tm_isdst=-1)

print(time.strptime(t2))
# ValueError: time data 'August 28th Saturday 11:30' does not match format '%a %b %d %H:%M:%S %Y'
# 포맷이 맞지 않음