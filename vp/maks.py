s = int(input())

dp = [0] * (s+1)
dp[0] = 1

voimalused = [5,10,20,50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]

for voimalus in voimalused:
    for i in range(voimalus, s+1):
        dp[i] += dp[i-voimalus]
print(dp)
print(dp[s])