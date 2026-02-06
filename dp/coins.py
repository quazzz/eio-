coins=  [1,4,5]
target = 13

dp = [float('inf')] * (target + 1) 
dp[0] = 0
for i in range(1, target + 1):
    for coin in coins:
        subproblem = i - coin
        if subproblem < 0:
            continue
        dp[i] = min(dp[i], dp[subproblem] + 1)
print(dp[target])