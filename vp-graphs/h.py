from heapq import heappush, heappop
n,m = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]

dist = [[float('inf')] * m for _ in range(n)]
dist[0][0] = grid[0][0]

pq = []
heappush(pq, (grid[0][0], 0, 0))
deltas = [(0,1), (0,-1), (1,0), (-1, 0)]
while pq:
    score, x,y = heappop(pq)
    if x == n - 1 and y == m - 1:
        print(score)
        break
    if score > dist[x][y]:
        continue
    for dx, dy in deltas:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            uus_score = score + grid[nx][ny]
            if uus_score < dist[nx][ny]:
                dist[nx][ny] = uus_score
                heappush(pq, (uus_score, nx, ny))