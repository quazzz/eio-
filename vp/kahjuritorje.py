m,n = map(int,input().split())
maa = [list(map(int,input().split())) for _ in range(m)]
ans = -10**9

for top in range(m):
    temp = [0] * n
    for bottom in range(top, m):
        for col in range(n):
            temp[col] += maa[bottom][col]
        curr = temp[0]
        best = temp[0]
        for j in range(1, n):
            curr = max(temp[j], curr + temp[j])
            best = max(best, curr)
        ans = max(ans, best)
print(ans)