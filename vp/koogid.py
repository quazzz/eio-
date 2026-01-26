n = int(input())
p = [(int(el), i) for i, el in enumerate(input().split())]
m = [(int(el), i) for i, el in enumerate(input().split())]
p.sort()
m.sort()

for i in range(1,n):
    if p[i - 1][0] * m[i][0] != p[i][0] * m[i-1][0]:
        print('EI')
        exit()
a = [-1] * n
for i in range(n):
    a[m[i][1]] = p[i][1] + 1
print('JAH')
print(*a)


