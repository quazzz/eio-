nums = list(map(int, input().split()))
l =  len(nums)

dp = [0] * l

dp[0] = nums[0]
dp[1] = max(dp[0] + dp[1], dp[0])

for i in range(2, l):
    dp[i] = nums[i] + max(dp[i - 2], dp[i - 1])
print(dp[-1])
