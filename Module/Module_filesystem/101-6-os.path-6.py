from os import path

# os.path.join
# 해당 os 형식에 맞게 입력받은 경로를 연결한다.
# 중간에 절대 경로 나오면 새로 씀
# 없는 것도 만들어냄
# <class 'str'>

print(path.join('G:\\dev', 'apache-jmeter-5.4.1', 'licenses'))
# G:\dev\apache-jmeter-5.4.1\licenses

print(path.join('C:\\', 'midway', 'C:\\', 'licenses'))
# C:\licenses

print(type(path.join('C:\\'))) # <class 'str'>


# os.path.normcase(path)
# 시스템에 맞게 문자열을 정규화한다.
print(path.normcase('G:/dev/apache-jmeter-5.4.1'))
# g:\dev\apache-jmeter-5.4.1


# os.path.normpath(path)
# 입력받은 경로를 정규화 한다. '.', '..'를 삭제한다.
print(path.normpath('G:/dev/apache-jmeter-5.4.1/../licenses'))
# G:\dev\licenses