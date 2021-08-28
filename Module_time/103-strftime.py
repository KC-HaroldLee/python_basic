# time.strftime(format[, t])
# time.strftime(string[, format])
# sturct_time 객체를출력하고 받아들인다.

from time import localtime, strftime

print(strftime('%B %dth %A %I:%M', localtime()))
# August 28th Saturday 11:13 # type : <class 'str'>
print(strftime('%Y-%m-%d %H:%M', localtime()))
# 2021-08-28 11:13 # type : <class 'str'>
print(strftime('%y/%m/%d %H:%M:%S', localtime()))
# 21/08/28 11:13:53 # type : <class 'str'>
print(strftime('%y/%m/%d %H:%M:%S'))
# 21/08/28 11:13:53 # type : <class 'str'>
print(strftime('%x, %X', localtime ())) # 심플하군
# 08/28/21, 11:13:53 # type : <class 'str'>