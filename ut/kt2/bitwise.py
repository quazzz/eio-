print(5 & 3)
print(6 | 3)

print(4 << 2) # 4 - 00100 10000 -> 16
print(16 >> 3) # 16 - 0010000 -> 0000010

print(13 & 1)
print(12 & 1)

mask = 1 << 2 # 00001 -> 00100 
res = 5 | mask # 5 -    |00101
                        #00101

num = 11 # 1011
maskm = 1 << 2 

res2 = maskm & num
print(res2)
