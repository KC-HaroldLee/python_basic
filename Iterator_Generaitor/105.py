a = [1,2,3,4,5,6,7,8,9,10] #10개의 객체를 저장할 메모리 공간이 필요하다.
print(sum(a))

b = (i for i in range(11))
print(b)
print(sum(b))#아이템이 바로 생성되기 때문에 저장할 메모리 공간이 필요X
