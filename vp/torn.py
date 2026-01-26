n = int(input())
blocks = []
for _ in range(n):
    x,y,z = map(int,input().split())
    blocks.append((min(x,y), max(x,y), z))
    blocks.append((min(x,z), max(x,z), y))
    blocks.append((min(y,z), max(y,z), x))
     
blocks.sort(key= lambda b: b[0]*b[1], reverse=True)

dp = [0] * len(blocks)
for i in range(len(blocks)):
    dp[i] = blocks[i][2]
    for j in range(i):
        if blocks[i][0] < blocks[j][0] and blocks[i][1] < blocks[j][1]:
            dp[i] = max(dp[i], dp[j] + blocks[i][2])
print(max(dp))