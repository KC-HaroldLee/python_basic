import Login

input_id = input("아이디를 입력하세요\n")
if Login.checkId(input_id):
    print("로그인 성공")
else:
    print("로그인 실패")
