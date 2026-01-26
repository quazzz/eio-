n = int(input())
cars= [tuple(map(int,input().split())) for _ in range(n)]

dp = [1] * n
cars.sort(key=lambda x: (x[0], -x[1]))
for i in range(n):
    for j in range(i):
        if cars[j][0] < cars[i][0] and cars[j][1] > cars[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp)) 