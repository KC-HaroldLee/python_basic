from os import path
import time

# os.path.exists(path)
print(path.exists('D:\\workspace\\python-git\\python_ruby-study\\tmp')) # False
print(path.exists('D:\\workspace\\python-git\\python_ruby-study')) # True

print(path.exists(path.dirname('D:\\workspace\\python-git\\python_ruby-study\\tmp'))) # True

# os.path.expanduser(path)
# 사용자폴더 가져오기
print(path.expanduser('~kk4ever')) # C:\Users\kk4ever 
print(path.expanduser('~kklastchnpd')) # C:\Users\kklastchnpd

# os.path.expandvars(path)
# path안에 환경변수가 있다면 확장한다. 환경변수는 os.environ에 정의된 것을 참조한다.
print(path.expandvars('$PYTHONPATH')) # C:\Users\bamto\pythonLib\myModule
print(path.expandvars('$PYTHONPATH\\lib')) # C:\Users\bamto\pythonLib\myModule\lib







