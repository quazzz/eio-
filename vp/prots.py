m,n,t = map(int,input().split())

dp = [-1] * (t + 1)
dp[0] = 0

for i in range(1, t + 1):
    max_tasks = -1
    if i - m >= 0 and dp[i - m] != -1:
        max_tasks = max(max_tasks, dp[i-m] + 1)
    if i - m >= 0 and dp[i - n] != -1:
        max_tasks = max(max_tasks, dp[i - n] + 1)
    dp[i] = max_tasks

for i in range(t+1):
    if dp[t - i] != -1:
        print(dp[t - i])
        break