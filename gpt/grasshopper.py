n = int(input())
k = int(input())
frogs = [int(i) for i in input().split()]

dp = [0] * (n+1)
dp[0]=1

for i in range(1, n + 1):
    if i in frogs:
        continue
    for j in range(1, k+ 1):
        if i > j >= 0:
            dp[i] += dp[i - j]