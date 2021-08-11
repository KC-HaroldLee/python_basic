#계산기 만들기
class Cal
  def initialize(v1, v2)
    @v1 = v1
    @v2 = v2
  end

  def add()
    return @v1+@v2
  end

  def setV1(v)
    if v.class()==Integer #복잡하게 해보기
      @v1 = v
    else
      puts("Integer가 아님")
    end
  end

  def setV2(v)
    if v.is_a?(Integer)
      @v2 = v
    else
      puts("Integer가 아님")
    end
  end

  def getV1()
    return @v1
  end

  def getV2()
    return @v2
  end

end

c1 = Cal.new(10,10)
c1.setV1(5)
p (c1.getV1)
c1.setV1('10')
p (c1.getV2)
