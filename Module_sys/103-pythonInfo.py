import sys

# 설치된 경로 반환 
print(sys.prefix) # C:\Users\bamto\AppData\Local\Programs\Python\Python39
print(sys.exec_prefix) # C:\Users\bamto\AppData\Local\Programs\Python\Python39

# 실행 파일 반환
print(sys.executable) # C:\Users\bamto\AppData\Local\Programs\Python\Python39\python.exe

# sys.path
# 모듈을 찾을 때 참조하는 경로
print(sys.path)
#['d:\\workspace\\python-git\\python_ruby-study\\Module_sys', 
# 'C:\\Users\\bamto\\pythonLib\\myModule', 
# 'C:\\Users\\bamto\\AppData\\Local\\Programs\\Python\\Python39\\python39.zip', 
# 'C:\\Users\\bamto\\AppData\\Local\\Programs\\Python\\Python39\\DLLs', 
# 'C:\\Users\\bamto\\AppData\\Local\\Programs\\Python\\Python39\\lib', 
# 'C:\\Users\\bamto\\AppData\\Local\\Programs\\Python\\Python39', 
# 'C:\\Users\\bamto\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages']

# sys.copyright
# sys.version
print(sys.copyright, '|', sys.version)
# All Rights Reserved. | 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]

# sys.getdefalutencoding()
print(sys.getdefaultencoding()) # utf-8


