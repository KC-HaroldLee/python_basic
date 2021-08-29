from os import path

# os.path.split(path)
# 디렉터리/ 파일을 튜플로 변환
# 실제 파일 존재 여부는 안 봄..
print(path.split('C:\\sample\\test.txt')) # ('C:\\sample', 'test.txt')
print(type(path.split('C:\\sample\\test.txt'))) # <class 'tuple'>

# os.path.splitdrive(path)
# 드라이브를...
print(path.splitdrive('C:\\sample\\test.txt')) # ('C:', '\\sample\\test.txt')

# os.path.splitext(path)
# 확장자를...
# 이건 확장자의 의미를 파악해야할 수도 있다.
print(path.splitext('C:\\sample\\test.txt')) # ('C:\\sample\\test', '.txt')