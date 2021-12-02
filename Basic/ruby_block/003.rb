['a','b','c'].each(){
  |item|puts(item.upcase)
}

array = ['a','b','c']

for eliment in array do
  puts(eliment.upcase)
end

array2 = ['1','5','52','3','52','74']
for eliment in array2 do
  if eliment.to_i > 10
    puts("10보다 큰 수 발견")
    puts(eliment)
    array2.delete(eliment)
  end
end

print("array2", array2)
puts("---------------")

array3 = ['1','5','52','3','52','74']
i = 0
array3.each(){
  |value|  print(i, ("번째 숫자는"), value, "\n")
  i = i + 1
  if value.to_i > 10
    array3.delete(value)
  end
}
print("array3", array3)
puts("---------------")
array4 = ['1','5','52','3','52','74']
array4.delete_if() do |value|
  value.to_i > 10
end
print("array4", array3)
puts("---------------")
