print('{0:$>5}'.format(10)) # $$$10
print('{0:$>+5}'.format(10)) # $$$10 - 양수임을 일부러 드러낼 때

print('{0:$>-5}'.format(10)) # $$$10 - 음수인 경우만
print('{0:$>-5}'.format(-10)) # $$-10 - 음수인 경우만

print('{0:$> 5}'.format(10)) # $$ 10 - 강제 공백?
print('{0:$> 5}'.format(-10)) # $$-10 강제 공백?(음수)