coins = list(map(int,input().split()))
target = int(input())
n = len(coins)
dp = [0] * (target + 1)
dp[0] = 1

for i in range(n - 1, -1, -1):
    for j in range(coins[i], target + 1):
        dp[j] += dp[j - coins[i]]
    print(dp)
print(dp[target])