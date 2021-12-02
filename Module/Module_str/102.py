# str 탐방

# capitalize()
a = 'NIRVANA is BEST'
print(a.capitalize()) # Nirvana is best

# count(keyword, [start, [end]])
b = 'an apple is paid'
print(b.count('a')) # 3
print(b.count('a', 2)) # 2
print(b.count('a', 0, 2)) # 1

# encode([encoding, [errors]])
# 파이썬3에서는 모든 것이 유니코드다.

c ='가나다'
print(c.encode('cp949')) # b'\xb0\xa1\xb3\xaa\xb4\xd9'
print(c.encode('utf-8')) # b'\xea\xb0\x80\xeb\x82\x98\xeb\x8b\xa4'

d = '가나다abc'
# print(d.encode('latin1')) # UnicodeEncodeError
# print(d.encode('한글')) # LookupError: unknown encoding

print(d.encode('latin1', 'ignore')) # b'abc'
print(d.encode('latin1', 'replace')) # b'???abc'
print(d.encode('latin1', 'xmlcharrefreplace')) # b'&#44032;&#45208;&#45796;abc'
print(d.encode('latin1', 'backslashreplace')) # b'\\uac00\\ub098\\ub2e4abc'

# endswitch(postfix, [start, [end]])
e = 'kk4ever@gmail.com'
print(e.endswith('gmail.com')) # True
print(e.endswith('gmail.com', 5)) # True
print(e.endswith('gmail.com', 5, -1)) # False
print(e.endswith('gmail.com', 5, len(e))) # True
print(e.endswith('.com', len(e)-4, len(e))) # True

# expandtabs([tabsize])
# tab을 공백으로 치환한다.

f = '[NAME]\t[PHONE.NO]\t[TEAM]'
print(f)
# [NAME]  [PHONE.NO]      [TEAM]
print(f.expandtabs())
# [NAME]  [PHONE.NO]      [TEAM]
print(f.expandtabs(1))
# [NAME] [PHONE.NO] [TEAM]
print(f.expandtabs(10))
# [NAME]    [PHONE.NO]          [TEAM]

