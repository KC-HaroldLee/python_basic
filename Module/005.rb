require_relative("Login")
puts("아이디를 입력해라")
input_id = gets.chomp()

if Login.checkId(input_id)
  puts("로그인 성공")

else
  puts("로그인 실패")
end
puts("테스트 끝 ")
