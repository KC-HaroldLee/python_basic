print("[중복검사]")
input_str = input("아이디를 입력하세요\n")
members = ['nirvana','greenday','goldfinger','offspring']

for member in members :
    if input_str == member:
        print(input_str + " 아이디를 찾았습니다!")
        print("종료합니다.")
        import sys
        sys.exit()
    else:
        print(input_str + " 를 계속 찾는 중입니다.")
print("해당 아이디는 존재하지 않습니다.")
