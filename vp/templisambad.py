k = int(input())
n = int(input())
heights = list(map(int,input().split()))

makssumma = sum(heights) + 1

dp = [-1] * makssumma
dp[0] = 0

for height in heights:
    for s in range(makssumma -1, -1, -1):
        if dp[s] != -1:
            if dp[s + height] == -1 or dp[s + height] > dp[s] + 1:
                dp[s + height] = dp[s] + 1
min_raiskamine = None
min_heights = None
tot = None
for s in range(k, makssumma):
    if dp[s] != -1:
        if min_raiskamine is None or (s - k < min_raiskamine) or (s - k == min_raiskamine and dp[s] < min_heights):
            min_raiskamine = s - k
            min_heights = dp[s]
            tot = s
print(min_heights, tot)