#계산기 만들기
class Cal
  def initialize(int1, int2)
    p int1, int2
    # p (int1, int2)
    # p (int1), (int2)
    @int1 = int1
    @int2 = int2
  end

  def add()
    return @int1+@int2
  end
end

c1 = Cal.new(10,10)
p c1.add()
# p c1.substract()

c2 = Cal.new(30,20)
# c2.add()
# c2.substract()
