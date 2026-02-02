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

    while q:
        x,y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if nx < 0 or nx >= m:
                continue
            if ny >= n:
                ny = 0
            elif ny < 0:
                ny = n - 1
            
            if not visited[nx][ny] and  grid[nx][ny] == 'm':
                visited[nx][ny] = True
                q.append((nx, ny))
                pindala += 1