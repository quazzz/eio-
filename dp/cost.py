cost = list(map(int,input().split()))
n = len(cost)

dp = [0] * (n + 1)
dp[0] = 0
dp[1] = 1
for i in range(2, n + 1):
    firstway = cost[i - 1] + dp[i - 1]
    secondway = cost[i - 2] + dp[i - 2]
    dp[i] = min(firstway, secondway)
print(dp[n])