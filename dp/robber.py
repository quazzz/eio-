houses = list(map(int, input().split()))
n = len(houses)
dp = [0] * (n + 1)
dp[1] = houses[0]
for i in range(2, n + 1):
    oneway = dp[i - 2] + houses[i - 1]
    dp[i] = max(oneway, dp[i - 1])
print(dp[n])