houses = list(map(int,input().split()))
l = len(houses)
dp = [0] * (l + 1)

dp[-1], dp[-2] = 0, houses[-1]

for i in range(l - 2, -1, -1):
    dp[i] = max(dp[i + 2] + houses[i], dp[i+1])
print(dp[0])