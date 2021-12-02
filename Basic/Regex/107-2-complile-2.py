# compile(pattern [,flag])
# 정규표현식 객체를 반환!
import re

regexTxt = re.compile('\w{1,}.txt')

print(bool(regexTxt.match('sample.txt'))) # True
print(bool(regexTxt.match('song.mp3'))) # False