id = "kk4ever"
pw = "4444"

input_id = input("아이디를 입력해보쇼\n")

if input_id==id:
    print(input_id + " 로그인을 시도합니다.")
    input_pw = input("비번을 입력해보쇼\n")

    if input_pw == pw:
        print(input_id + " 로그인 성공")

    else: #input_pw != pw:
        print(input_id + " 로그인 실패")

else: #input_id!=id:
    print(input_id + "은 없는 아이디 입니다.")
