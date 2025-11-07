import sys

n = int(sys.stdin)
arvud = []
s = sys.stdin.aplit(' ')
for i in range(n):
    arvud.append(int(s[i]))
n2 = 1 << n
for i in range(n2):
    loendur = 0
    i2 = i
    p = ''
    while i2 > 0:
        if i2 % 2 == 1:
            p += arvud[loendur] + ' '
        loendur += 1
        i2 /= 2
    print(p)
