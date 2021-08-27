# 정규표현식 객체를 만들고 사용가능한 옵션들
import re
# re.I
# re.IGNORECASE 
# 대소문자를 구분하지 않고 매칭 작업을 수행합니다.
regexTxt = re.compile('\w{1,}.txt', re.I)
print(bool(regexTxt.match('sample.txt'))) # True
print(bool(regexTxt.match('SAMPLE.TXT'))) # True

# re.M
# re.MULTLINE
# ^, $을 사용할 때 여러줄을 검사. 

regex3wordsFirst = re.compile('^[가-힣]')
regex3wordsLast = re.compile('$[가-힣]')
regex3wordsMULTLINE = re.compile('[가-힣]', re.M)
str1 = """이
석
Hyun
"""
print(regex3wordsFirst.findall(str1)) # ['이']
print(regex3wordsLast.findall(str1)) # []
print(regex3wordsMULTLINE.findall(str1)) # ['이', '석']