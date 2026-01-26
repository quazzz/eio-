n = int(input())
arvud = list(map(int,input().split()))

dp = [0] * (n+1)
dp[0] = 0

for i in range(1,n+1):
    dp[i] = max(arvud[i - 1], dp[i-1] + arvud[i - 1])
print(dp)
maximum = max(dp)
if maximum < 0:
    print(0)
else:
    print(maximum)