import os

# os.remove(path), os.unlink(path)
# 파일을 삭제

# os.rmdir(path)
# 디렉터리 삭제, 단 디렉터리는 비어있어야한다.

# os.removedirs([path)
# 디렉터리를 연달아 삭제한다.

# os.rename(src, dst)
# 이름 변경 

# os.stat(path)
# 경로 정보를 가져온다.

# os.utime(path, times)
# 파일들을 하나씩 엑세스 시간과 수정시간을 <times>로 수정한다.

# os.walk
# 디렉터리를 순차적으로 보여준다.

# os.umask(mask)
# umask를 설정

# os.pipe()
# 파이프 생성

# os.fdopen(fa[, mode, [, bufsize]])
# 파일 디스크립터

# os.popen(command[, mode[, bufsize]])
# 인자로 전달 된 command를 수행하여 파이프를 연다.

# os.name
# 운영체제 이름을 나타낸다.

# os.environ
# 환경변수를 나타낸다.

# os.getpid()
# 현재 프로세스 아이디를 반환

# os.putenv(varname, value)
# 환경변수 <varname>을 <value>로 설정한다.

# os.strerror(code)
# 해당 되는 에러 메시지를 보여준다.
# 0 ~ 입력

# os.system(command)
# command를 실행하여 성공하여 성공하면 0 반환된다.
os.system('calc') # 계산기 켜짐...

# os.startfile(path[, operation])
# 프로그램 실행