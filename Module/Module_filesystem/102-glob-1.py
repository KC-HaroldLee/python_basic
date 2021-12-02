import glob
import os.path
# glob.glob()path
# 경로에 해당하는 디렉/파일 리스트를 반환한다.
print(glob.glob('C:\\Users\\bamto\\Desktop\\구성하기\\Hello world\\*.lnk'))
# ['C:\\Users\\bamto\\Desktop\\구성하기\\Hello world\\Atom.lnk', 
# (...) 
# 'C:\\Users\\bamto\\Desktop\\구성하기\\Hello world\\Visual Studio Code.lnk']

# glob.igolb(path)
# 이터레이터를 반환한다. 오우...
iglob1 = glob.iglob('C:\\Users\\bamto\\Desktop\\구성하기\\Hello world\\*.lnk')
# <generator object _iglob at 0x000001D3AFD34B30>

for i in iglob1 :
    print(i)
# C:\Users\bamto\Desktop\구성하기\Hello world\Atom.lnk
# (...)
# C:\Users\bamto\Desktop\구성하기\Hello world\Visual Studio Code.lnk