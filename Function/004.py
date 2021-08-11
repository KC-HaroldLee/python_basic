members = ['nirvana','offspring','greenday']

def checkId(inputId):
    for member in members:
        if inputId==member:
            return True
        else:
            return FalseW

inputId = input("아이디를 입력하세요\n")

if checkId(inputId):
    print("있는 아이디!")
else:
    print("없어요!")
