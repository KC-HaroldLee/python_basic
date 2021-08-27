#변수로 불러오기
import FilePath

f1 = open(FilePath.fileFolder+'/test.txt', 'w')

print('f1 = ', f1) # open의 정보를 알려준다.
print('f1.name', f1.name) # 경로확인 (메소드가 아니군)

print(f1.write('hello hello\nhow low')) # 입력 후 / 글자수를 반환한다.

print('close 전', f1.closed)
f1.close()
print('close 후', f1.closed)