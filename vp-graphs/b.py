from collections import deque
m,n = map(int,input().split())
grid = [list(input()) for _ in range(m)]
visited = [[False] * n for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
max_pindala = float('-inf')
def bfs(sx, sy):
    q = deque()
    q.append((sx, sy))
    visited[sx][sy] = True
    pindala = 1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or nx >= m:
                continue
            if ny < 0:
                ny = n - 1
            elif ny >= n:
                ny = 0
            if not visited[nx][ny] and grid[nx][ny] == 'm':
                visited[nx][ny] = True
                q.append((nx, ny))
                pindala += 1
    return pindala

for i in range(m):
    for j in range(n):
        if grid[i][j] == 'm' and not visited[i][j]:
            pindala = bfs(i, j)
            max_pindala = max(max_pindala, pindala)
print(max_pindala)