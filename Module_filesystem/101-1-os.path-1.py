from os.path import *
# os.path.abspath('tmp')
# 현재경로(정확히는 파일 위치)를 Prefix로 해서 
# 입력받은 경로를 절대 경로로 바뀌서 반환한다.
print(abspath('tmp')) 
# D:\workspace\python-git\python_ruby-study\tmp
# 뭐랄까... cd 느낌이다

# os.path.basename()
# 입력받은 경로의 기본 이름을 반환한다. 
# abspath()와 반대라고 생각하면 된다.
print(basename('D:\\workspace\\python-git\\python_ruby-study\\tmp')) 
# tmp

# os.path.commoonpath(path_list)
# 공통경로를 비교로 가져온다.

l1 = ['c:\\sample\\abc', 'c:\\sample\\efg', 'c:\\sample']
l2 = ['c:\\sample123', 'c:\\sample124', 'c:\\sample125']
print(commonpath(l1)) # c:\sample
print(commonpath(l2)) # c:\

# os.path.commonprefix(path_list)
# 이건 단순 문자열 검사이다.
print(commonprefix(l2)) # c:\sample12

