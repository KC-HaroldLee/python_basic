# 정규표현식 객체를 만들고 사용가능한 옵션들
import re
# re.S
# re.DOTALL
# 개행문자도 '.'로 매칭된다.
import urllib.request

web = urllib.request.urlopen('https://regexper.com/')
html = web.read()
web.close()

code = str(html).encode('utf-8').decode('cp949')

regex = re.compile('<title>(.*)</title>', re.I|re.S)
print(regex.findall(code))