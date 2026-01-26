n = int(input())
nums = list(map(int,input().split()))

dp = [0] * (n+1)
dp[0] = 1

for i in range(1,n):
    dp[i] = max(nums[i], nums[i] + dp[i-1])
print(max(dp))