names = ['sonic','tails','knuckles']
def checkName(str)
  for name in names
    if str == name
      puts("아이디 발견")
      return true
    else
      puts("발견하지 못함")
    end
  end
  return false
end

puts("이름을 입력")
inputName = gets.chomp()
puts("입력한 아이디는 " + inputName)

if checkName(inputName)
  puts("맞음")
else
  puts("아님")
end
puts("종료")
