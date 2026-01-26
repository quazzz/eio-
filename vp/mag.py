# loeme sisendi
n = int(input())
s = sorted(input())

a = ''
b = ''
for i, char in enumerate(s):
    if i % 2 != 0: 
        a += char
    else:
        b += char
print(int(''.join(a)) + int(''.join(b)))