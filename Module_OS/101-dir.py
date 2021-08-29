# os 모듈
import os

# getcwd()
# 현재 작업 디렉토리
print('현재', os.getcwd()) # 현재 D:\workspace\python-git\python_ruby-study

# chdir(path)
# 작업 디렉토리 변경
os.chdir('c:\\')
print('변경1', os.getcwd()) # 변경1 c:\

os.chdir('Intel')
print('변경2', os.getcwd()) # 변경2 c:\Intel

os.chdir('NIRVANA') # FileNotFoundError: [WinError 2] 지정된 파일을 찾을 수 없습니다: 'NIRVANA'