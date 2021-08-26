#순회 방법
list = ['apple','bear','cheese']

#1. 그냥 for in
print('1. for in 활용')
for item in list :
    print(item)

#2. 내장 메서드인 join()
print('2. join() 활용')
print('\n'.join(list))

#3. 리스트 내장(?)
print('3. 리스트 내장(?)을 활용')
print('\n'.join(item for item in list)) #item이 두 번 들어간다.