puts("[중복검사]")
puts("아이디를 입력하세요")
input_str = gets.chomp()
members = ['nirvana','greenday','goldfinger','offspring']

for member in members do
    if input_str == member
        puts(input_str + " 아이디를 찾았습니다!")
        puts("종료합니다.")
        exit
    else
        puts(input_str + " 를 계속 찾는 중입니다.")
    end
end

puts("해당 아이디는 존재하지 않습니다.")
