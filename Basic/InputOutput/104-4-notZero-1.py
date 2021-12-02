# **를 입력하면 사전을 입력받은 것으로 판단하고 인자를 하나만 받게된다.
band = 'nirvana'
name = 'cobain'

print('{name} is {band}'.format(**locals()))