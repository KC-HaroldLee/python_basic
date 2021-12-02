class C
  attr_reader :value #읽기 가능한 속성으로 지정하겠다.
  attr_writer :value #읽기 가능한 속성으로 지정하겠다.
  def initialize(v)
    @value = v
  end
  def show()
    p @value
  end
end

c1 = C.new(10)
p c1.value
c1.value = 20
p c1.value
