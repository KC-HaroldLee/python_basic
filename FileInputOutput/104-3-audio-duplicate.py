import FilePath
#타게팅 (복사할 것, 복사될 것)
copy = open(FilePath.fileFolder+'/music-copy.mp3', 'wb')
origin = open(FilePath.fileFolder+'/music.mp3', 'rb')

import os
print('복사본', os.path.getsize(FilePath.fileFolder+'/music-copy.mp3'))
print('원본', os.path.getsize(FilePath.fileFolder+'/music.mp3'))

#복사
copy.write(origin.read())
print('---복사완료---')
# 파일 크기 구하기
import os
print('복사본', os.path.getsize(FilePath.fileFolder+'/music-copy.mp3'))
print('원본', os.path.getsize(FilePath.fileFolder+'/music.mp3'))
copy.close() # 잊지말자
origin.close()