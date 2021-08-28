from fractions import Fraction

fract1 = Fraction.from_float(0.5)
print(fract1) # 1/2

fract2 = Fraction.from_decimal(5)
print(fract2) # 5

fract1 = Fraction.from_float(5)
print(fract1) # 5

fract2 = Fraction.from_decimal(0.5) 
# TypeError: Fraction.from_decimal() only takes Decimals, not 0.5 (float)
