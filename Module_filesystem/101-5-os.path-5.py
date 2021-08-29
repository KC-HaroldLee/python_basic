# 판별
from os import path

# path.isabs()
# 절대 경로인지(하지만 단순 문자열 검색)
print(path.isabs('G:\\dev\\apache-jmeter-5.4.1\\bin')) # True
print(path.isabs('apache-jmeter-5.4.1\\bin')) # False

# path.isfile(path)
# 파일인지 아닌지
# 경로가 없어도 False
print(path.isfile('G:\\dev\\apache-jmeter-5.4.1\\LICENSE')) # True
print(path.isfile('G:\\dev\\apache-jmeter-5.4.1\\licenses')) # False

# path.isdir(path)
# 디렉터리인지 아닌지
print(path.isdir('G:\\dev\\apache-jmeter-5.4.1\\LICENSE')) # False
print(path.isdir('G:\\dev\\apache-jmeter-5.4.1\\licenses')) # True
