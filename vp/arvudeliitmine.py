k,n = map(int,input().split())

mod = 10**9 + 7
dp =  [[0] * (n+1) for _ in range(k+1)]
dp[0][0] = 1


for i in range(1, k+1):
    dp[i][0] = 1
    for s in range(1,n+1):
        dp[i][s] = (dp[i][s-1] + dp[i-1][s]) % mod
print(dp[k][n])