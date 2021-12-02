import numpy as np

b = np.array([999, 9999, 99999, 999999])
print(b.data.hex()) # e70300000f2700009f8601003f420f00

print(b.data.hex()[0:8]) # e7030000 
print(b.data.hex()[8:16]) # 0f270000
print(b.data.hex()[16:24]) # 9f860100
print(b.data.hex()[24:32]) # 3f420f00

print(hex(b[0])) # 0x3e7
print(hex(b[1])) # 0x270f
print(hex(b[2])) # 0x1869f
print(hex(b[3])) # 0xf423f

print(int('0x3e7', 16)) # 999
print(int('0x270f', 16)) # 9999
print(int('0x1869f', 16)) # 99999
print(int('0xf423f', 16)) # 999999


c = np.array([999, 9999, 99999, 999999], dtype=np.int64)
print(c.data.hex())
# e703000000000000
# 0f27000000000000
# 9f86010000000000
# 3f420f0000000000

print(hex(c[0])) # 0x3e7
print(hex(c[1])) # 0x270f
print(hex(c[2])) # 0x1869f
print(hex(c[3])) # 0xf423f