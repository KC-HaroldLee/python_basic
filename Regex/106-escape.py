# escape()
# 영문자, 숫자가 아닌 문자에 대해서 백슬래시 문자를 추가한다
# 정규표현식이 필요없음

import re

str1 = '가a 나b     다c라d¼'
print(re.escape(str1)) # 가a\ 나b\ \ \ \ \ 다c라d¼