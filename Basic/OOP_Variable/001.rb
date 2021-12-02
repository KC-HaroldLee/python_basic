class C
 def initialize(v)
   @value = v
 end
 def show()
   return @value
 end
end

c1 = C.new(10)
# p c1.@value()
p c1.show()
