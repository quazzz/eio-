coins = list(map(int,input().split()))
x = int(input())

dp = [0] * (len(coins) + 1)

dp[0] = 1


for coin in coins:
    for i in range(coin, x+1):
        dp[i] = dp[i - coin]
print(dp[x])
