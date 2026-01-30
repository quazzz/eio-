import sys
def ristkorrutis(a,b,c,d):
    return a * d == b * c

n = int(input())
gnomes = [(int(el), i) for i, el in enumerate(input().split())]
weights = [(int(el), i) for i, el in enumerate(input().split())]
gnomes.sort()
weights.sort()
voimalik = True
for i in range(1, n):
    if not ristkorrutis(gnomes[i][0], weights[i][0], gnomes[i-1][0], weights[i-1][0]):
        voimalik = False
        break
if voimalik:
    dp = [-1] * n
    for i in range(n):
        dp[weights[i][1]] = gnomes[i][1] + 1
    print('SAAB')
    print(*dp)
else:
    print('EI SAA')

