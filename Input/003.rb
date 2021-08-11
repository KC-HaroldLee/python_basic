id = "kk4ever"
pw = "4444"

puts("아이디를 입력해주세요")
input_id = gets.chomp()

if input_id==id
  puts(input_id + "의 로그인 시도를 합니다.")
  puts("비번을 입력해주세요")
  input_pw = gets.chomp()
  if input_pw==pw
    puts("로그인 성공!")
  else #input_pw!=pw
    puts("로그인 실패!")
  end

else #input_id!=id
  puts(input_id + "은 없는 아이디입니다.")
end
